# Define a function to validate the post data.
def validate_post_data(data):

    # Check if the data is None or if it's not of type list.
    if data is None or not isinstance(data, list):
        return False

    # Ensure that every record in the data list contains all the specified keys.
    # The `all` function returns True only if all the conditions inside are True.
    return all(
        # Check if every required key exists in the current record.
        all(key in record for key in ['timestamp', 'sensor_07', 'sensor_47', 'machine_status'])
        for record in data
    )
