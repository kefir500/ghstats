#!/usr/bin/env python


import unittest
import ghstats


class TestStats(unittest.TestCase):

    def test_cli(self):
        """
        Test command line arguments.
        """
        count = ghstats.main_cli(["kefir500/apk-icon-editor", "-l", "-d"])
        self.assertTrue(count > 0)

    def test_releases(self):
        """
        Test statistics for all releases.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, False, ghstats.get_env_token(), False)
        self.assertTrue(isinstance(stats, list))
        count = ghstats.get_stats_downloads(stats, False)
        self.assertTrue(count > 0)

    def test_release(self):
        """
        Test statistics for the latest release.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, True, ghstats.get_env_token(), False)
        self.assertTrue(isinstance(stats, dict))
        count = ghstats.get_stats_downloads(stats, False)
        self.assertTrue(count > 0)

    def test_invalid_repo(self):
        """
        Test nonexistent repository.
        """
        self.assertRaises(ghstats.GithubRepoError,
                          lambda: ghstats.download_stats("kefir500", "foobar", None, False,
                                                         ghstats.get_env_token(), True))

    def test_invalid_token(self):
        """
        Test invalid GitHub personal access token.
        """
        self.assertRaises(ghstats.GithubTokenError,
                          lambda: ghstats.download_stats("kefir500", "foobar", None, False, "FOOBAR", True))


if __name__ == "__main__":
    unittest.main()
