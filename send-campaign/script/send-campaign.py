import requests
import argparse
import os

parser = argparse.ArgumentParser(description="Send a test email for a campaign")
parser.add_argument("-i", "--id", dest="campaign_id", help="Campaign unique ID", required=True)
args = parser.parse_args()

campaign_id = args.campaign_id

url_api = "https://newsletter.infomaniak.com/api/v1/public/campaign/{id}/send".format(id=campaign_id)
client_api = os.environ.get("CLIENT_API")
client_secret = os.environ.get("CLIENT_SECRET")

# print(mail_content)

headers = {
    'Content-Type': 'application/json',
}

req = requests.request("POST", url = url_api ,headers = headers, auth=(client_api, client_secret))
if req.status_code == 200:
    print(req.json())
else:
    print(req.status_code)
    print(req.json())
