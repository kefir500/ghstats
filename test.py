#!/usr/bin/env python


import unittest
import ghstats


try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


class TestStats(unittest.TestCase):

    def test_releases(self):
        """
        Download all releases.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, False, None, True)
        self.assertTrue(isinstance(stats, list))
        count = ghstats.get_stats_downloads(stats, True)
        self.assertTrue(count > 0)

    def test_release(self):
        """
        Download latest release.
        """
        stats = ghstats.download_stats("kefir500", "apk-icon-editor", None, True, None, True)
        self.assertTrue(isinstance(stats, dict))
        count = ghstats.get_stats_downloads(stats, True)
        self.assertTrue(count > 0)

    def test_invalid(self):
        """
        Check nonexistent repository.
        """
        self.assertRaises(urllib2.HTTPError, lambda: ghstats.download_stats("kefir500", "foobar", None, False, None, True))


if __name__ == '__main__':
    unittest.main()
