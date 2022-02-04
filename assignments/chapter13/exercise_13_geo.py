#!/usr/bin/env python3

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Hopefully I will get through getting an API key set up and can focus on
# finding the question to Life, the universe, and everything - seeing as I
# already know the answer


def retrieve_data(address, api_key=False):
    """given an address string return a json object from the API"""
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else:
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
    # copied from geojson.py, I also need to look into figuring out more about
    # how to handle ssl certificates in production code...
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving ', url)
    try:
        uh = urllib.request.urlopen(url, context=ctx)
    except urllib.error.HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        print('Reason: ', e.reason)
    else:
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')
        return data
    return False


def parse_data(urldata):
    """get the placeID from json encoded geolocation data"""
    json_geo_data =json.loads(urldata)
    # print(json.dumps(json_geo_data, indent=2))
    location = json_geo_data['results'][0]['place_id']
    return location


def main():
    """
    prompt user for a location and print out the placeID retrieved from a
    geolocation API
    """
    while True:
        print("Enter location:")
        address = input("(leave blank to exit: )")
        if len(address) < 1:
            break
        urldata = retrieve_data(address)
        if urldata is not False:
            location_code = parse_data(urldata)
            print(location_code)
        continue


if __name__ == '__main__':
    main()
