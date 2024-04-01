#!/usr/bin/env bash

result=$(python /test-campaign.py -i "${INPUT_ID}" -d "${INPUT_DEST}")

echo "result=$result" >> ${GITHUB_OUTPUT}

