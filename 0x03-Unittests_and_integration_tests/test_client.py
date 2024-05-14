#!/usr/bin/env python3
"""Test the client module."""

import unittest
from unittest.mock import patch, PropertyMock, Mock, call
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url works."""
        expected_url = "https://api.github.com/orgs/test-org/repos"
        payload = {"repos_url": expected_url}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=payload)):
            client = GithubOrgClient("test-org")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos works."""
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value="https://api.github.com/orgs/test-org/repos"):
            client = GithubOrgClient("test-org")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license works."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration tests."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = lambda url: {
            "https://api.github.com/orgs/google": Mock(
                status_code=200,
                json=lambda: cls.org_payload
            ),
            cls.org_payload["repos_url"]: Mock(
                status_code=200,
                json=lambda: cls.repos_payload
            ),
        }.get(url, Mock(status_code=404))

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after integration tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the GithubOrgClient.public_repos method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.mock_get.assert_has_calls([
            call("https://api.github.com/orgs/google"),
            call(self.org_payload["repos_url"])
        ])

    def test_public_repos_with_license(self):
        """Test the GithubOrgClient.public_repos method with a license."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock_get.assert_has_calls([
            call("https://api.github.com/orgs/google"),
            call(self.org_payload["repos_url"])
        ])


if __name__ == '__main__':
    unittest.main()
