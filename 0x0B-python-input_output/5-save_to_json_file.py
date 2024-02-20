#!/usr/bin/python3
"""object to a text file using json rep"""
import json


def save_to_json_file(my_obj, filename):
    """json representation"""
    with open(filename, mode='w', encoding='utf-8') as mfile:
        mfile.write(json.dumps(my_obj))
