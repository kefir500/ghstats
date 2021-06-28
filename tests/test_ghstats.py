#!/usr/bin/env python

import unittest
import sys
import os

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ghstats import ghstats  # noqa


class TestStats(unittest.TestCase):

    def test_cli(self):
        """
        Test command line arguments.
        """
        self.assertTrue(ghstats.main_cli(["kefir500", "apk-icon-editor", "-q"]) > 0)
        self.assertTrue(ghstats.main_cli(["kefir500", "apk-icon-editor", "-l", "-d"]) > 0)
        self.assertTrue(ghstats.main_cli(["kefir500", "apk-icon-editor", "-l", "-d", "-q"]) > 0)
        self.assertTrue(ghstats.main_cli(["kefir500", "apk-icon-editor", "v1.5.0"]) > 0)
        self.assertTrue(ghstats.main_cli(["kefir500/apk-icon-editor"]) > 0)

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
        with self.assertRaises(ghstats.GithubRepoError):
            ghstats.download_stats("kefir500", "foobar", None, False, ghstats.get_env_token(), True)

    def test_invalid_token(self):
        """
        Test invalid GitHub personal access token.
        """
        with self.assertRaises(ghstats.GithubTokenError):
            ghstats.download_stats("kefir500", "foobar", None, False, "FOOBAR", True)

    def test_unicode(self):
        """
        Test Unicode handling.
        """
        release = ghstats.download_stats("d3", "d3", "v3.5.0", False, ghstats.get_env_token(), False)
        try:
            ghstats.get_release_downloads(release)
        except UnicodeEncodeError:
            self.fail("Could not handle Unicode release statistics.")

    def test_exits(self):
        """
        Test if functions halt the script.
        """
        with self.assertRaises(SystemExit) as cm:
            ghstats.main_cli(["-h"])
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm:
            ghstats.error("Test")
        self.assertNotEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit):
            ghstats.main_cli(["kefir500/foobar"])


if __name__ == "__main__":
    unittest.main()
