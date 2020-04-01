import unittest

"""
run the following command in main dir "app"
python -m tests.test_pyproj

simple "hack" to run directly from here
# import os
# import sys
# cwd = os.getcwd()
# sys.path.append(cwd + '/app/')
"""

from tr_proj import transform_epsg


class PyprojTest(unittest.TestCase):
    """
    Test for transformation between different CRS.
    """
    def test_pyproj_transformation_mercator_to_WGS84(self):
        """
        Results from EPSG.io to test:
        latitude, longtitude == North, East
        42.56789, 23.45678 <==> 2611196.81, 5246429.88
        transform_epsg('epsg:3857', 'epsg:4326', 2611196.81, 5246429.88)
        transform_epsg('epsg:4326', 'epsg:3857', 42.56789, 23.45678)
        """
        n, e = transform_epsg('epsg:3857', 'epsg:4326', 2611196.81, 5246429.88)
        self.assertEqual("{:.5f} {:.5f}".format(n, e), "42.56789 23.45678")

    def test_pyproj_transformation_WGS84_to_merc(self):
        lat, lon = transform_epsg('epsg:4326', 'epsg:3857', 42.56789, 23.45678)
        self.assertEqual("{:.2f} {:.2f}".format(lat, lon), "2611196.81 5246429.88")


if __name__ == "__main__":
    print("success")
    unittest.main()
