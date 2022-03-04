#!/usr/bin/env python
# posts an event to Splunk On-Call from Relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

URLBase = relay.get(D.endpointURL).rstrip("/")
routingKey = relay.get(D.routingKey).lstrip("/")

url = f"{URLBase}/{routingKey}"

try:
  entity_id = relay.get(D.entityID)
except:
  entity_id = ""

eventPayload = {
  'message_type': 'INFO',
  'entity_id': entity_id,
  'entity_display_name': relay.get(D.entityDisplayName),
  'state_message': relay.get(D.stateMessage),
}

r = requests.post(url, json=eventPayload)

print('Emitted event to Splunk On-Call REST API, got response: ', r.text)

r.raise_for_status()
