#!/bin/bash
#do you believe in magic?
curl -sI $1 -o /dev/null -w "%{http_code}"
