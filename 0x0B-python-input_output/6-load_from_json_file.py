#!/usr/bin/python3
"""creating an object from json file"""
import json


def load_from_json_file(filename):
    """the function that loads json"""
    with open(filename, mode='r', encoding='utf-8') as mfile:
        nwobj = json.loads(mfile.read())
        return nwobj
