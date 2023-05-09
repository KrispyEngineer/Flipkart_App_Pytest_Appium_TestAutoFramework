from configparser import ConfigParser


class ConfReader:

    @staticmethod
    def get_config(section, key):
        config = ConfigParser()
        config.read("..\ConfigurationData\conf.ini")
        return config.get(section, key)
