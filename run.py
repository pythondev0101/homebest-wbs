import os
from app import create_app,db
# import subprocess

config_name = 'production'
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
