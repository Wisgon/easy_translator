import requests


def translate(word):
    return word


def get_config():
    with open("server/config.json", "r") as f:
        config = f.read()
    return config


def set_config(config):
    with open("server/config.json", "w") as f:
        f.write(config)


if __name__ == "__main__":
    result = translate("dirt")
    print(result)
