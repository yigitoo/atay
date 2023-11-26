class Config:
    def __init__(self, config = None):
        if config is not None:
            self.config = config
        else:
            self.config = {
            "host": "localhost",
            "port": 80,
            "admins": [
                "yigitgumus"
            ],
            "GeoLocationAPIKey": "geo_location_api_key",
            "DB_URL": "*******",
            "DB_USER": "******",
            "DB_PASSWORD": "******",
            "DB_TABLE_USERS": "users",
            "DB_TABLE_STRUCTURES": "structures",
            "DB_TABLE_COMPLAINTS": "complaints"
        }

    def get_db_config(self) -> dict:
        return {
            "DB_URL": self.config["DB_URL"],
            "DB_USER": self.config["DB_USER"],
            "DB_PASSWORD": self.config["DB_PASSWORD"],
            "DB_TABLE_USERS": self.config["DB_TABLE"],
            "DB_TABLE_STRUCUTRES": self.config["DB_TABLE_STRUCUTRES"],
            "DB_TABLE_COMPLAINT": self.config["DB_TABLE_COMPLAINT"],
        }

    GetDBConfig = get_db_config

    def get_cfg(self):
        return self.config

    def set(self, key, value) -> int:
        if (key is None) or (self.config[key] is None):
            return -1
        else:
            self.config[key] = value if value is not None else self.config[key]

    def get(self, key = None):
        return self.config.get(key)

    @classmethod
    def default(cls, config: dict = None) -> dict:
        if config != None:
            return cls(config)

        return cls(config)

    def get_port(self):
        return self.config.get('port')

# Some tests
if __name__ == '__main__':
    from pprint import pprint
    cfg = Config.default()
    cfg2 = Config()
    cfg2.set('port', 123)
    pprint(cfg.config)
    pprint(cfg2.config)
    pprint(cfg2.get_port())
