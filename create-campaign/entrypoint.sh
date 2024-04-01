#!/usr/bin/env bash

python /create-campaign.py -c ${INPUT_CONTENT} -s ${INPUT_SUBJECT} -n ${INPUT_NAME-FROM} -l ${INPUT_LANG} -a ${INPUT_ADDRESS-FROM} -m ${INPUT_MAILINGLISTID}

