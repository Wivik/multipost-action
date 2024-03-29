#!/usr/bin/env bash

output=$(python /rss-to-html.py ${1})
echo "result=$output" >> ${GITHUB_OUTPUT}
