#!/usr/bin/env python
import os

from flask_script import Manager, Shell

from app import create_app, db

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
manager = Manager(app)
db.create_all(app=app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def run_tests():
    pass


if __name__ == "__main__":
    manager.run()
