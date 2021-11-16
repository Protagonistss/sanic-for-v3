__all__ = ['MYSQL_SETTING', 'TORTOISE_ORM']

MYSQL_SETTING = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'backend',
    'charset': 'utf8'
}

TORTOISE_ORM = {
    "connections": {
        "default": "mysql://{}:{}@{}:{}/{}".format(MYSQL_SETTING.get('user'), MYSQL_SETTING.get('password'),
                                                   MYSQL_SETTING.get('host'),
                                                   MYSQL_SETTING.get('port'), MYSQL_SETTING.get('db'))},
    "apps": {
        "models": {
            "models": ["aerich.models", "models.user", "models.verify"],
            "default_connection": "default",
        }
    }
}
