#!/bin/bash
# takes in a url and sends a POST
curl "$1"-sX POST -d "email=test@gmail.com&subject=I will always be here for PLD"
