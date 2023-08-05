import unittest
import requests
import pandas as pd
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

class TestAPI(unittest.TestCase):

    def test_get_data(self):
        response = requests.get(f"{BASE_URL}/get_data")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        if len(data) > 0:
            sample = data[0]

            # Garantindo que o dado filtrado contém os campos esperados
            self.assertIn('timestamp', sample)
            self.assertIn('sensor_07', sample)
            self.assertIn('sensor_47', sample)
            self.assertIn('machine_status', sample)

            # Garantindo que a filtragem por data foi correta
            timestamp = datetime.strptime(sample['timestamp'], "%Y-%m-%dT%H:%M:%S.%f")
            self.assertEqual(timestamp.month, 4)  # Abril

            # Garantindo que os valores de sensor estão corretos
            self.assertTrue(20 < sample['sensor_07'] < 30 or 20 < sample['sensor_47'] < 30)

    def test_receive_data(self):
        sample_data = {
            'timestamp': "2018-04-01T00:00:01.000",
            'sensor_07': 25,
            'sensor_47': 22,
            'machine_status': "NORMAL"
        }

        response = requests.post(f"{BASE_URL}/post_data", json=[sample_data])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Data received and processed successfully!"})

if __name__ == "__main__":
    unittest.main()
