# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns a dictionary of OpenGraph metadata found in the HTML of the given URL.
    """
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException:
        return {}


# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))
