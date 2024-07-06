#!/bin/bash
# Takes in a URL, sends a GET request to the url
curl -sX GET "$1" -L 200
