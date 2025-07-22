from flask import Flask,request
from flask_bootstrap import Bootstrap
bootstrap=Bootstrap()
def create_app():
    app=Flask(__name__)
    bootstrap.init_app(app)
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
print('init is running.....')
    