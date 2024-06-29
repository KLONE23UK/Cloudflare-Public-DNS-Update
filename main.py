from dotenv import load_dotenv
import requests
import os, sys

if os.path.exists(".env"):
    pass
else:
    print("No .env file present, make sure you created this")
    sys.exit()

load_dotenv()

try:
    os.environ["GLOBAL_KEY"]
    os.environ["ZONE_ID"]
    os.environ["RECORD_ID"]
    os.environ["EMAIL"]
    os.environ["NAME"]
except:
    print("One or all enviroment variables unaccessable. Make sure GLOBAL_KEY, ZONE_ID, RECORD_ID, EMAIL and NAME are present in .env file") 
    sys.exit()

GLOBAL_KEY = os.getenv('GLOBAL_KEY')
ZONE_ID = os.getenv('ZONE_ID')
RECORD_ID = os.getenv('RECORD_ID')
EMAIL = os.getenv('EMAIL')
NAME = os.getenv('NAME')

public_ip_url = 'https://api.ipify.org?format=json'
put_url = f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}'

get_public_ip = requests.get(public_ip_url)
public_ip_data = get_public_ip.json()
public_ip = public_ip_data['ip']

headers = {
        'X-Auth-Email': EMAIL,
        'X-Auth-Key': GLOBAL_KEY 
        }

data = {
        'content': public_ip,
        'name': NAME,
        'type': 'A',
        'id': RECORD_ID 
        }

response = requests.put(put_url, headers=headers, json = data)
data = response.json()
record_name = data['result']['name']
print(f"DNS record changed for {record_name} to {public_ip}")
