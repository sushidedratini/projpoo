class ConfigurationManager:
    def __init__(self):
        self.config = {}

    def get_config(self, key):
        return self.config.get(key)

    def set_config(self, key, value):
        self.config[key] = value