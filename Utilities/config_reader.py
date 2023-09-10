from configparser import ConfigParser
from pathlib import Path


def config_reader(section, key):
    """
    This utility method will read all the locators from cofig.ini file
    """
    config = ConfigParser()
    current_dir = Path().absolute().parent
    config.read(f"{current_dir}/Configurations/conf.ini")
    return config.get(section, key)

