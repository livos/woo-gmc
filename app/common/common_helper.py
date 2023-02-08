import yaml


def load_settings():
    settings = None
    with open("./settings.yaml", "r") as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    return settings
