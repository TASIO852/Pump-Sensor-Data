# Import the 'app' object from the 'app' module.
from app import app

# Import the 'os' module which provides a way to use operating system-dependent functionality.
import os

# Check if this script is being executed as the main module.
if __name__ == '__main__':
    
    # Check if the directory specified in 'DATA_DIR' configuration of 'app' does not exist.
    if not os.path.exists(app.config['DATA_DIR']):
        
        # Create the directory specified in 'DATA_DIR' configuration of 'app'.
        os.makedirs(app.config['DATA_DIR'])
    
    # Start the application (usually a web server).
    app.run()
