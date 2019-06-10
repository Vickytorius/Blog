from flask import *
from flask_sqlalchemy import *

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123456@localhost:3306/blog_new"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'suibianxie'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    #关联app与创建好的db实例的
    db.init_app(app)

    #将topic蓝图与app关联在一起
    from  .topic import topic as topic_blueprint
    app.register_blueprint(topic_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)
    return app

