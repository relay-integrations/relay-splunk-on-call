from relay_sdk import Interface, WebhookServer
from quart import Quart, request, render_template_string
from collections import defaultdict

import logging
import json


def deep_dict():
    return defaultdict(deep_dict)


def deep_insert(data, key, value):
    keys = key.split(".")
    for subkey in keys[:-1]:
        data = data[subkey]
    data[keys[-1]] = value

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    # data = await request.form
    data = await request.get_json(force=True)

    logging.info("Received the following webhook payload: \n%s",
                 json.dumps(data, indent=4))

    event = deep_dict()

    # traverse the keys of the form "A.DOTTED.KEY": "VALUE"
    # and create a deep dict of the form { "a": { "dotted": { "key": "VALUE "}}}
    # lowecasing the key names
    for key, value in data.items():
        deep_insert(event, key.lower(), value)

    logging.info("Emitting event: \n%s",
                 json.dumps(event, indent=4))

    relay.events.emit(event)

    return {'success': True}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
