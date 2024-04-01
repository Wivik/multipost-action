FROM python:3.11

COPY script/create-campaign.py /create-campaign.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install requests

ENTRYPOINT ["/entrypoint.sh"]

