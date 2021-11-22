from sanic import Sanic
from apis import apis
import logging
from db import register_mysql
from sanic_openapi import openapi2_blueprint
from handler.exception import server_error_handler

logging.basicConfig(filename='access.log')

Sanic(__name__, strict_slashes=True)
app = Sanic.get_app()
app.blueprint(apis)
app.blueprint(openapi2_blueprint)
# open when debug False
# app.error_handler.add(Exception, server_error_handler)
register_mysql(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, access_log=True)
