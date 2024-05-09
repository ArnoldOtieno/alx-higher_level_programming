#!/bin/bash
#Displaying all the http methods the server will accept
curl -sI | grep "Allow" | cut -d " " -f 2-
