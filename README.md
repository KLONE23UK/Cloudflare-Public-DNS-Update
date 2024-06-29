# Cloudflare Public DNS Update

## Description

Uses [ipify](https://www.ipify.org/) to get your public ip and [Cloudflare API](https://developers.cloudflare.com/api/) to update a DNS record.


## Instructions

**Note; you will need an existing record in order to change it. Does not create records**

Create .env file and add your [GLOBAL_KEY](https://dash.cloudflare.com/profile/api-tokens), [ZONE_ID](https://developers.cloudflare.com/fundamentals/setup/find-account-and-zone-ids/), [RECORD_ID](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records), EMAIL and NAME in the same direcotry as main.py

```python
GLOBAL_KEY="<GLOBAL_KEY>"
ZONE_ID="<ZONE_ID>"
RECORD_ID="<RECORD_ID>"
EMAIL="<EMAIL>"
NAME="<NAME>"
```
Run the script and you'll see the DNS record has changed

```
» python3 main.py
DNS record changed for <NAME> to <public ip>
```

## Additions

See [Overwrite DNS Record](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record) for list of options availabe that can be updated. Add these to the **data** dictionary.

```python
data = {
    'content': public_ip,
    'name': NAME,
    'type': 'A',
    'id': RECORD_ID,
    'comment': 'Updated automatically via script'
}
```


