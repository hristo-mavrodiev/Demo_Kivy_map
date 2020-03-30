import json
import requests

B = 42.661275
L = 23.379707
# query = 'ordnance%20survey%20southampton'


def match_cleanse(B, L):

    """
    Sample json request for geocoding.
    Argument addressdetails is hardcoded to 1 for returning max 1 address.
    """

    try:
        url = 'https://nominatim.openstreetmap.org/reverse?format=json&'
        lat_url = '&lat=' + str(B)
        lon_url = '&lon=' + str(L)
        # to return only 1 result, if there are many addresses found
        max_res = '&zoom=27&addressdetails=1'
        url = url + lat_url + lon_url + max_res
        r = requests.get(url)
        # print(r)
        result = r.json()
        return result['address']['postcode']
    except Exception as exe:
        print(exe)


print((match_cleanse(B, L)))
