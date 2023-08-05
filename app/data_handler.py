# Import the pandas library and give it the alias 'pd'.
import pandas as pd

# Define a function to load data from a file and filter it based on specific conditions.
def load_and_filter_data(file_path):
    # Load the CSV file into a pandas DataFrame.
    data = pd.read_csv(file_path)
    
    # Convert the 'timestamp' column to datetime format.
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    
    # Filter the data to only include records from the month of April.
    data = data[data['timestamp'].dt.month == 4]
    
    # Further filter the data to only include records from the year 2018.
    data = data[data['timestamp'].dt.year == 2018]
    
    # Filter the data based on the values of 'sensor_07' and 'sensor_47' columns.
    # It includes records where 'sensor_07' or 'sensor_47' values are between 20 and 30.
    filtered_data = data[((data['sensor_07'] > 20) & (data['sensor_07'] < 30)) |
                         ((data['sensor_47'] > 20) & (data['sensor_47'] < 30))]
    
    # Convert the 'timestamp' column back to string format.
    filtered_data['timestamp'] = filtered_data['timestamp'].astype(str)
    
    # Return the filtered data with selected columns.
    return filtered_data[['timestamp', 'sensor_07', 'sensor_47', 'machine_status']]

# Define a function to organize the data based on specific formatting and conditions.
def organize_data(incoming_data):
    # Create an empty list to store the processed records.
    processed_data = []
    
    # Loop through each record in the incoming data.
    for record in incoming_data:
        # Convert the 'timestamp' from string to datetime format.
        timestamp = pd.to_datetime(record['timestamp'])
        
        # Extract the date and time components from the timestamp.
        date = timestamp.strftime('%Y-%m-%d')
        time = timestamp.strftime('%H:%M:%S')
        
        # Get the machine status from the record.
        status = record['machine_status']
        
        # Check and process the 'sensor_07' data if its value is between 20 and 30.
        if 20 < record['sensor_07'] < 30:
            processed_data.append({'Data': date, 'Hora': time, 'Sensor': 'sensor_07', 'Medição': record['sensor_07'], 'Status': status})
        
        # Check and process the 'sensor_47' data if its value is between 20 and 30.
        if 20 < record['sensor_47'] < 30:
            processed_data.append({'Data': date, 'Hora': time, 'Sensor': 'sensor_47', 'Medição': record['sensor_47'], 'Status': status})
    
    # Convert the processed data list into a pandas DataFrame and return it.
    return pd.DataFrame(processed_data)
