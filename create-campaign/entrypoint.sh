#!/usr/bin/env bash

result=$(python /create-campaign.py -c "${INPUT_CONTENT}" -s "${INPUT_SUBJECT}" -n "${INPUT_NAMEFROM}" -l "${INPUT_LANG}" -a "${INPUT_ADDRESSFROM}" -m "${INPUT_MAILINGLISTID}")

echo "result=$result" >> ${GITHUB_OUTPUT}

