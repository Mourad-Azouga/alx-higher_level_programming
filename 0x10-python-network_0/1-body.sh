#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sI $1 | grep "HTTP/1.1 200" -A 1 | tail -n 1