from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

DATA_PATH = "C:/Users/tarsi/OneDrive/Documentos/Projects/Data Science/Pump Sensor Data/data/pump_sensor_data.csv"  # caminho para o arquivo baixado

def filter_data():
    df = pd.read_csv(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Filtrando os dados
    df = df[df['timestamp'].dt.month == 4]
    df = df[((df['sensor_07'] > 20) & (df['sensor_07'] < 30)) | ((df['sensor_47'] > 20) & (df['sensor_47'] < 30))]

    # Selecionando colunas necessárias
    return df[['timestamp', 'sensor_07', 'sensor_47', 'machine_status']]

@app.route('/data', methods=['GET'])
def get_data():
    data = filter_data()
    return jsonify(data.to_dict(orient='records'))

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.json

    df = pd.DataFrame(data)

    # Organizando os dados
    df['Date'] = df['timestamp'].dt.date
    df['Time'] = df['timestamp'].dt.time
    df_melted = df.melt(id_vars=['Date', 'Time', 'machine_status'], value_vars=['sensor_07', 'sensor_47'], 
                        var_name='Sensor', value_name='Measurement')

    final_df = df_melted[['Date', 'Time', 'Sensor', 'Measurement', 'machine_status']]
    final_df = final_df.rename(columns={"machine_status": "Status"})

    print(final_df)  # Exibindo no console

    return jsonify({"message": "Data received and processed successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
