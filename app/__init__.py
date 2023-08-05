# Import the Flask class from the flask module.
from flask import Flask
# Import the os module which provides a way to use operating system-dependent functionality.
import os

# Create an instance of the Flask class. 
# The argument `__name__` determines the root path for the application 
# to enable it to locate resources such as templates and static files.
app = Flask(__name__)

# Configure the app using settings from 'config.py'.
app.config.from_pyfile('config.py')

# Import routes (probably the view functions or URL handlers) from the current package.
# The '.' indicates the current package.
from . import routes
