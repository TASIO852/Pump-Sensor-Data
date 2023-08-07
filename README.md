# Complete Technical Challenge Documentation

## 1. **Data Request Service (GET API)**

### The. **Data Reading and Filtering**

- **File:** `data_handler.py`
- **Functions:** To read the file, filter data according to the challenge criteria (April 2018, sensors 07 and 47, values between 20 and 30), and prepare the answer.

### B. **GET API**

- **Methodology:** Respond with the filtered data in JSON format via GET request and display it in the interface (The route is in the `routes.py` file).

## 2. **Data Reception Service (POST API)**

### The. **Data Reception**

- **File:** `data_handler.py`
- **Functions:** To send the data via POST to the DATA directory simulating a DB that pass through a `validador.py` and then are organized and after that a CSV file is created with the data

### B. **Data Organization**

- **Processing:** Organize the data in a Pandas DataFrame with specific columns (Date, Time, Sensor, Measurement, Status), and display it in the console (The route is in the `routes.py` file).

## 3. **Advanced User Interface ╰(*°▽°*)╯**

### The. **API Call Interface**

- HTML structure with header, body, buttons, and results table.
- JavaScript/jQuery with front-end functions and event handlers.
- Styling with CSS.

### B. **HTML Results**

- Control panel with POST, GET buttons and table to present GET data.
- Styling with separate CSS file.

## 4. **Folder Structure**

- **Organization:** Files are clearly organized, making execution and maintenance easier, as shown in the folder structure below.

```
Pump Sensor Data
├─ app
│  ├─ static
│  │  └─ css
│  │     └─ styles.css
│  ├─ templates
│  │  └─ index.html
│  ├─ validator.py
│  ├─ config.py
│  ├─ data_handler.py
│  ├─ routes.py
│  └─ __init__.py
├─ data
│   └─ pump_sensor_data.csv
├─ docs
│   └─ Prueba Técnica Desarrollador Python Semi SR _ ENGLISH.pdf
├─ tests
│   └─ test.py
├─ .gitignore
├─ main.py
├─ README.md
├─ requirements.txt
 
```

## 5. **Installation and running instructions**

- **Pre-config:** In the `config.py` file, put the paths your computer has for the code to work
- **Dependencies:** List of all necessary libraries in the `requirements.txt` file, for installation via PIP.
- **Execution:** After everything is installed, run the `main.py` file and in your browser go to `"http://localhost:5000` and have fun (❁´◡`❁).

## Conclusion

This documentation covers both the technical challenge and additional components designed to stand out. The main focus remains on developing the APIs for querying and loading data, but also includes an advanced user interface with HTML, JavaScript/jQuery, and CSS. These extras demonstrate a more complex and complete approach, offering additional functionality that goes beyond the proposed challenge.
