from pathlib import Path
import yaml

TEMP_ETSY_CREDS_PATH = Path('etsy_creds.yaml')
ETSY_CONFIG_PATH = Path('etsy_api_config.yaml')


def get_creds():
    with open(TEMP_ETSY_CREDS_PATH, 'r') as f:
        creds = yaml.safe_load(f)

    return creds


def get_api_config():
    with open(ETSY_CONFIG_PATH, 'r') as f:
        config = yaml.safe_load(f)

    return config
