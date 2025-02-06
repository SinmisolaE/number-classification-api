# Number Classification API

## Overview
This is a simple Flask-based API that classifies numbers based on their mathematical properties. It checks whether a number is prime, perfect, Armstrong, even or odd, and returns a fun fact about the number using the Numbers API.

## Features
- Determines if a number is:
  - **Prime**
  - **Perfect**
  - **Armstrong**
  - **Even or Odd**
- Calculates the sum of the digits of the number
- Retrieves a fun fact about the number from the [Numbers API](http://numbersapi.com/)

## API Endpoint
### **GET /api/classify-number**
#### **Query Parameter:**
- `number` (required) - The number to classify

#### **Example Request:**
```sh
GET http://localhost:5000/api/classify-number?number=371
```

#### **Example Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number.",
}
```

#### **Error Response (400 Bad Request):**
```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation
### **1. Clone the Repository**
```sh
git clone <repository-url>
cd <repository-folder>
```


### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Run the API Locally**
```sh
python app.py
```
The API will now be running at `http://localhost:5000`

## Dependencies
- Flask
- Flask-CORS
- Requests

## Deployment
To deploy the API, you can use platforms like:
- Render
- Railway

## License
This project is open-source and available under the [MIT License](LICENSE).

