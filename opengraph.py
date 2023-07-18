# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns a dictionary of OpenGraph metadata found in the HTML of the given URL.
    """

    URI = "https://opengraph.lewagon.com/"
    params = {"url": url}
    response = requests.get(URI, params = params)

    if response.status_code == 200:
        return response.json()['data']

    return {}


import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.github.com"))
