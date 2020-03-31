"""
Functions from https://github.com/pyproj4/pyproj for Geographical coordinates transformation.

"""

from pyproj import Proj, transform


def transform_epsg(from_epsg: str, target_epsg: str, lat_n: float, lon_e: float):
    """
    Transforming coordinates between two EPSG codes.
    Input:
    ----------
    from_proj  -source EPSG code 'epsg:3857'
    target_proj - target EPSG code - 'epsg:4326'
    lat_n - latitude/North -coordinates to transform
    lon_e - lontitude/East

    Output:
    lat_n_tr, lon_e_tr - tuple with transformed coordinates
    """
    source_proj = Proj(from_epsg)
    target_proj = Proj(target_epsg)
    lat_n_tr, lon_e_tr, = transform(source_proj, target_proj, lat_n, lon_e)
    return lat_n_tr, lon_e_tr,


if __name__ == "__main__":
    print(transform_epsg('epsg:3857', 'epsg:4326', 2611196.81, 5246429.88))
    print(transform_epsg('epsg:4326', 'epsg:3857', 42.56789, 23.45678))
