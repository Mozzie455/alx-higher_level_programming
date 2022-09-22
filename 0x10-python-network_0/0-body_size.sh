#!/bin/bash
# cURL request that displays size of the response's body
curl -sI "$1" | grep Content-Length | cut -d " " -f2-
