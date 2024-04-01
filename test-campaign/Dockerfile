FROM python:3.11

COPY script/test-campaign.py /test-campaign.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install requests

ENTRYPOINT ["/entrypoint.sh"]

