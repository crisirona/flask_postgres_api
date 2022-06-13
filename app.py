from flask import Flask
from config import config
from flask_cors import CORS

#routes
from routes import Instrumento
app=Flask(__name__)

CORS(app)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])

    #blueprints
    app.register_blueprint(Instrumento.main,name='instrumentos', url_prefix='/api/instrumentos')
    

    #error handler
    app.register_error_handler(404, page_not_found)
    app.run()