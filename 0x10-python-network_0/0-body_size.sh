#!/bin/bash
#displayig size of the body of URL response
curl -s "$1" | wc -c
