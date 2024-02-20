#!/usr/bin/python3
"""json string to object"""
import json


def from_json_string(my_str):
    """returns an object"""
    return json.loads(my_str)
