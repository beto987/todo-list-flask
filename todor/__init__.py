from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():                                      
    app = Flask(__name__)                                   

    #configuracion del proyecto                         
    app.config.from_mapping(                        
        DEBUG = False,                                   
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todoList.db"                           
    )

    db.init_app(app)

    #registrar blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    return app