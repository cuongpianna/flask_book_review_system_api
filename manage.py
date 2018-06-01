from app import create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app('default')
migrate = Migrate(app,db)
manager = Manager(app)


manager.add_command('shell',Shell)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()