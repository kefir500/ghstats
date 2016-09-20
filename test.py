#!/usr/bin/env python


import unittest
import ghstats
import os


class TestStats(unittest.TestCase):

    def test_releases(self):
        """
        Download all releases.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, False, ghstats.get_env_token(), True)
        self.assertTrue(isinstance(stats, list))
        count = ghstats.get_stats_downloads(stats, True)
        self.assertTrue(count > 0)

    def test_release(self):
        """
        Download latest release.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, True, ghstats.get_env_token(), True)
        self.assertTrue(isinstance(stats, dict))
        count = ghstats.get_stats_downloads(stats, True)
        self.assertTrue(count > 0)

    def test_invalid(self):
        """
        Check nonexistent repository.
        """
        self.assertRaises(ghstats.GithubRepoError,
                          lambda: ghstats.download_stats("kefir500", "foobar", None, False,
                                                         ghstats.get_env_token(), True))

    def test_envtoken(self):
        """
        Check GitHub token environment variable.
        """
        os.environ["GITHUB_TOKEN"] = "foobar"
        token = ghstats.get_env_token()
        self.assertEqual(token, "foobar")


if __name__ == '__main__':
    unittest.main()
