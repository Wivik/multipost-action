FROM python:3.11

COPY rss-to-html.py /rss-to-html.py
COPY templates /templates

RUN pip install jinja2 feedparser

ENTRYPOINT ["/entrypoint.sh"]

