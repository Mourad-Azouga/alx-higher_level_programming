#!/bin/bash
# takes in a URL as an argument, sends a GET request
curl -sX GET $1 -H "X-School-User-Id:98"
