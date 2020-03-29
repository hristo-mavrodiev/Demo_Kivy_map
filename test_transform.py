from pyproj import Proj, transform


def transform_epsg(from_proj: str, target_proj: str, x1: float, x2: float):
    """
    Transforming coordinates between two EPSG codes.
    Input:
    ----------
    from_proj  -source EPSG code 'epsg:3857'
    target_proj - target EPSG code - 'epsg:4326'
    x1,x2 -coordinates to transform

    Output:
    x2, y2 - tuple
    """
    from_proj = Proj('epsg:3857')
    target_proj = Proj('epsg:4326')
    x1, y1 = -11705274.6374, 4826473.6922
    x2, y2 = transform(from_proj, target_proj, x1, y1)
    return (x2, y2)
