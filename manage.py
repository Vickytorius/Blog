#启动和项目管理的相关代码
from app import *
from flask_script import *
from flask_migrate import *
from app.models import *

app=create_app()

manager =Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__=="__main__":
    manager.run()