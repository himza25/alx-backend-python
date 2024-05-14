#!/usr/bin/env python3
"""
Unittests for client.py
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"payload": True})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property"""
        mock_org.return_value = {"repos_url": "http://some_url/repos"}
        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, "http://some_url/repos")
        mock_org.assert_called_once()

    @patch(
        'client.get_json',
        return_value=[{"name": "repo1"}, {"name": "repo2"}]
    )
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method"""
        mock_public_repos_url.return_value = "http://some_url/repos"
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://some_url/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures"""
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.get_patcher_effect
        )
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class fixtures"""
        cls.get_patcher.stop()

    @staticmethod
    def get_patcher_effect(url):
        """Side effect for requests.get"""
        if url == "https://api.github.com/orgs/google":
            return Mock(**{"json.return_value": TEST_PAYLOAD[0][0]})
        if url == "https://api.github.com/orgs/google/repos":
            return Mock(**{"json.return_value": TEST_PAYLOAD[0][1]})
        return Mock(**{"json.return_value": {}})

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license argument"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
