#!/bin/bash
#Sends post request to url and displaying response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
