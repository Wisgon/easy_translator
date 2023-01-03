import requests
import json


def get_config(key):
    with open("server/config.json", "r") as f:
        config = json.loads(f.read())
    return config.get(key)


def set_config(key, value):
    config = get_config()
    config[key] = value
    with open("server/config.json", "w") as f:
        f.write(json.dumps(config))


if __name__ == "__main__":
    pass
