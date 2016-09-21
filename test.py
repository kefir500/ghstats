#!/usr/bin/env python


import unittest
import ghstats


class TestStats(unittest.TestCase):

    def test_cli(self):
        """
        Test command line arguments.
        """
        count = ghstats.main_cli(["kefir500/apk-icon-editor", "-q", "-d"])
        self.assertTrue(count > 0)

    def test_releases(self):
        """
        Download all releases.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, False, ghstats.get_env_token(), False)
        self.assertTrue(isinstance(stats, list))
        count = ghstats.get_stats_downloads(stats, False)
        self.assertTrue(count > 0)

    def test_release(self):
        """
        Download latest release.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, True, ghstats.get_env_token(), False)
        self.assertTrue(isinstance(stats, dict))
        count = ghstats.get_stats_downloads(stats, False)
        self.assertTrue(count > 0)

    def test_invalid(self):
        """
        Check nonexistent repository.
        """
        self.assertRaises(ghstats.GithubRepoError,
                          lambda: ghstats.download_stats("kefir500", "foobar", None, False,
                                                         ghstats.get_env_token(), True))


if __name__ == "__main__":
    unittest.main()
