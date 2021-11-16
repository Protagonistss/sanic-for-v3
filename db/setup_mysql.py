from tortoise.contrib.sanic import register_tortoise
from conf.db import MYSQL_SETTING


def register_mysql(app):
    register_tortoise(app,
                      db_url='mysql://{}:{}@{}:{}/{}'.format(MYSQL_SETTING.get('user'), MYSQL_SETTING.get('password'),
                                                             MYSQL_SETTING.get('host'),
                                                             MYSQL_SETTING.get('port'), MYSQL_SETTING.get('db')),
                      modules={'models': ['models.user', 'models.verify']}, generate_schemas=False)
