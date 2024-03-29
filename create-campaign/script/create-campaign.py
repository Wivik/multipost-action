import requests
import argparse
import os

parser = argparse.ArgumentParser(description="Create a new Infomaniak Newsletter service campaign")
parser.add_argument("-c", "--content", dest="campaign_content", help="Content for the campaign to create", required=True)
parser.add_argument("-s", "--subject", dest="campaign_subject", help="Subject for the campaign email", required=True)
parser.add_argument("-n", "--name-from", dest="campaign_email_from_name", help="Name the from field", required=True)
parser.add_argument("-l", "--lang", dest="campaign_lang", help="Lang of the content", default="en")
parser.add_argument("-a", "--address-from", dest="campaign_email_from_addr", help="Email for the from field", required=True)
parser.add_argument("-m", "--mailinglists-id", nargs='+', dest="campaign_ml_id", help="Mailing list ID (array, ex : -m 1 2 3)", type=int, required=True)
args = parser.parse_args()

campaign_content = args.campaign_content
campaign_subject = args.campaign_subject
campaign_email_from_name = args.campaign_email_from_name
campaign_lang = args.campaign_lang
campaign_email_from_addr = args.campaign_email_from_addr
campaign_ml_id = args.campaign_ml_id

url_api = "https://newsletter.infomaniak.com/api/v1/public/campaign"
client_api = os.environ.get("CLIENT_API")
client_secret = os.environ.get("CLIENT_SECRET")

# ensure the mailing list id has one or more items
if len(campaign_ml_id) == 1:
    campaign_ml_id = int(campaign_ml_id[0])

# print(mail_content)

headers = {
    'Content-Type': 'application/json',
}

payload = {
    "subject": campaign_subject,
    "email_from_name": campaign_email_from_name,
    "lang": campaign_lang,
    "email_from_addr": campaign_email_from_addr,
    "content": campaign_content,
    "mailinglistIds": campaign_ml_id
}

print(payload)

req = requests.request("POST", url = url_api , json = payload, headers = headers, auth=(client_api, client_secret))
if req.status_code == 200:
    print(req.json())
else:
    print(req.status_code)
    print(req.json())
