# Importing necessary modules and functions from Flask library
from flask import jsonify, request, render_template

# Importing 'app' object that represents the Flask web server
from . import app

# Importing specific functions from the 'data_handler' module 
# to manage and manipulate the dataset
from .data_handler import load_and_filter_data, organize_data

# Importing the function 'validate_post_data' from the 'validator' module 
# to check the integrity of the incoming data
from .validator import validate_post_data

# Defining a route for the root URL of the application.
# When a user visits this URL, they will be presented with the 'index.html' page.
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Defining an API endpoint '/get_data' to be accessed via GET requests.
# This endpoint returns a filtered version of the dataset based on specific criteria.
@app.route('/get_data', methods=['GET'])
def get_data():
    # Using the function 'load_and_filter_data' to retrieve a filtered version of the data
    filtered_data = load_and_filter_data(app.config['DATA_BASE'])

    # Saving the filtered data to a CSV file at a location specified in the Flask app's configuration
    filtered_data.to_csv(app.config['GET_DATA_PATH'], index=False)

    # Returning the filtered data as a JSON response to the client
    return jsonify(message='Dados carregados na pagina com sucesso', data=filtered_data.to_dict(orient='records'))

# Defining another API endpoint '/post_data' to be accessed via POST requests.
# This endpoint accepts the filtered dataset, restructures it, and then saves the results.
@app.route('/post_data', methods=['POST'])
def post_data():
    # Calling the 'get_data' function to fetch the filtered data from the dataset
    response_from_get = get_data()
    
    # Extracting the JSON data from the response
    incoming_data = response_from_get.json['data']

    # Validating the received data using the 'validate_post_data' function
    if not validate_post_data(incoming_data):
        return jsonify(message='Dados inválidos'), 415

    try:
        # Organizing the validated data using the 'organize_data' function
        organized_data = organize_data(incoming_data)

        # Saving the organized data to a CSV file, the path for which is defined in the app's configuration
        organized_data.to_csv(app.config['POST_DATA_PATH'], index=False)

        # Returning a success message and the organized data as a JSON response to the client
        return jsonify(message='Dados organizados no banco com sucesso (Um arquivo foi criado no diretório data do projeto)', data=organized_data.to_dict(orient='records'))

    # Handling exceptions that might occur during data organization and saving
    except Exception as e:
        # Returning the exception message to the client as an error response
        return str(e), 400
