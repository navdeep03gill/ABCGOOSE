import os
from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_blueprint
from routes.thesaurus_routes import thesaurus_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'this is a secret'
    
    CORS(app, resources={r"/*": { "origins": "*"}}, supports_credentials=True)
    
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(thesaurus_blueprint, url_prefix='/thesaurus')
    #app.register_blueprint(ml_blueprint, url_prefix='/ml')
    
    return app

if __name__ == '__main__': 
    app = create_app()
    app.run(host='0.0.0.0', port=8000) #app.run(host='0.0.0.0', port=8000)
