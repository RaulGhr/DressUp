from flask import Flask
from flask_restful import Api
from flask_cors import CORS


from dbModels import db
from RoutesBlueprint import my_blueprint


class App():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        self.app.app_context().push()
        self.app.register_blueprint(my_blueprint)


        db.init_app(self.app)
        CORS(self.app)


    def run(self):
        # db.create_all()
        self.app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    app = App()
    app.run()
