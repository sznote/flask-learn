from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def test():
# 	return "hello word"
app.secret_key = "mypassword"

from  tutor1.api.routes import mod
from  tutor1.site.routes import  mod

app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')

#app.register_blueprint(api.routes.api, url_prefix='/api')