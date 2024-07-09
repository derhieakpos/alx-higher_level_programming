#!/bin/bash
# sends a request to a url passed
curl -s -o /dev/null -w "%{http_code}" "$1"
