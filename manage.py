import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from image_service import app, db


app.config.from_object(config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

""" Manage commands
python manage.py db init -- Initialize db if not exists,
python manage.py db migrate -- create migration/add changes
python manage.py db upgrade -- run migrations.
"""

if __name__ == '__main__':
    manager.run()
