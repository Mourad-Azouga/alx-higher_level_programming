#!/bin/bash
#takes in a URL, sends a POST request
curl -sX POST $1 -d "email:test@gmail.com" -d"subject:I will always be here for PLD" -L 
