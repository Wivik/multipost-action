# newsletter-action

A set of scripts and GitHub Actions to schedule and send a Newsletter hosted at [Infomaniak](https://www.infomaniak.com/en/marketing-events/newsletter-tool) from a RSS feed using [the API](https://newsletter.infomaniak.com/docs/index.html?shell#introduction-beta). These scripts are wrapping the provider's API.

This project is not affiliated with this company.

## Content

### Prerequisites

Set a virtualenv and install the requirements.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### rss-to-html

A Python script that returns the title and HTML content from the latest entry of a RSS feed. It uses a Jinja2 template to produce a HTML formatted email.

Usage :

```bash
python rss-to-html.py <feed url>
```

Returns :

```
{'title': 'My awesome title', 'content': 'My awesome content'}
```

### create-campaign

This script initiate the newsletter campaign. Use the RSS to HTML script to provide the content and subject.

Script usage :

```
usage: create-campaign.py [-h] -c CAMPAIGN_CONTENT -s CAMPAIGN_SUBJECT -n CAMPAIGN_EMAIL_FROM_NAME [-l CAMPAIGN_LANG] -a CAMPAIGN_EMAIL_FROM_ADDR -m CAMPAIGN_ML_ID [CAMPAIGN_ML_ID ...]

Create a new Infomaniak Newsletter service campaign

options:
  -h, --help            show this help message and exit
  -c CAMPAIGN_CONTENT, --content CAMPAIGN_CONTENT
                        Content for the campaign to create
  -s CAMPAIGN_SUBJECT, --subject CAMPAIGN_SUBJECT
                        Subject for the campaign email
  -n CAMPAIGN_EMAIL_FROM_NAME, --name-from CAMPAIGN_EMAIL_FROM_NAME
                        Name the from field
  -l CAMPAIGN_LANG, --lang CAMPAIGN_LANG
                        Lang of the content
  -a CAMPAIGN_EMAIL_FROM_ADDR, --address-from CAMPAIGN_EMAIL_FROM_ADDR
                        Email for the from field
  -m CAMPAIGN_ML_ID [CAMPAIGN_ML_ID ...], --mailinglists-id CAMPAIGN_ML_ID [CAMPAIGN_ML_ID ...]
                        Mailing list ID (array, ex : -m 1 2 3)
```

Returns :

```
{'result': 'success', 'data': {'id': 1234, 'subject': 'test', 'status': {'id': 2, 'label': 'Draft'}, 'started_at': None, 'lang': 'en_GB'}}

```

### test-campaign

Send a test to a designated email address.

```
usage: test-campaign.py [-h] -i CAMPAIGN_ID -d CAMPAIGN_DEST

Send a test email for a campaign

options:
  -h, --help            show this help message and exit
  -i CAMPAIGN_ID, --id CAMPAIGN_ID
                        Campaign unique ID
  -d CAMPAIGN_DEST, --dest CAMPAIGN_DEST
                        Email to send the test
```

Returns :

{'result': 'success', 'data': 'Test sent to something@something.something'}

### send-campaign

Execute the campaign sending from the service. The delivery will be scheduled and can be viewed on the management console.

```bash
usage: send-campaign.py [-h] -i CAMPAIGN_ID

Send a test email for a campaign

options:
  -h, --help            show this help message and exit
  -i CAMPAIGN_ID, --id CAMPAIGN_ID
                        Campaign unique ID
```

Returns :

```
{'result': 'success', 'data': {'id': 1234, 'scheduled_at': {'date': '2024-03-29 17:55:25.000000', 'timezone_type': 3, 'timezone': 'Europe/Zurich'}}}
```


