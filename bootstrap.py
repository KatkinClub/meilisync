import json
import os
import yaml
from urllib.parse import urlparse

db_conn_string = os.environ["DATABASE_URL"]

parsed = urlparse(db_conn_string)

print(parsed.username)
print(parsed.password)
print(parsed.hostname)
print(parsed.path)

def pretty_print(something):
    print(json.dumps(something, indent=4))

with open("config-template.yml", "r") as file:
    conf = yaml.safe_load(file)
    pretty_print(conf)
    conf["source"]["database"] = parsed.path[1:]
    conf["source"]["host"] = parsed.hostname
    conf["source"]["user"] = parsed.username
    conf["source"]["password"] = parsed.password
    conf["meilisearch"]["api_key"] = os.environ["MEILI_MASTER_KEY"]

    with open("config.yml", "w") as to_write:
        yaml.dump(conf, to_write)
