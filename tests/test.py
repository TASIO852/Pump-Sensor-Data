import requests

def get_and_post_data():
    get_url = "http://localhost:5000/data"
    post_url = "http://localhost:5000/receive"
    
    # Fazendo a solicitação GET
    response = requests.get(get_url)
    if response.status_code != 200:
        print("Erro na solicitação GET:", response.text)
        return

    # Verificando se os dados recebidos estão no formato esperado
    data = response.json()
    for record in data:
        if not all(key in record for key in ['timestamp', 'sensor_07', 'sensor_47', 'machine_status']):
            print("Dados recebidos não estão no formato esperado.")
            return

        # Fazendo a solicitação POST com cada registro
        post_response = requests.post(post_url, json=record)
        if post_response.status_code != 200:
            print("Erro na solicitação POST:", post_response.text)
        else:
            print(post_response.text)

if __name__ == "__main__":
    get_and_post_data()
