from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/classify-number": {"origins": "*"}})


def is_armstrong_number(n):
    """ Checks if a number is an armstrong number. returns with true or false"""
    digits = [int(digit) for digit in str(n)]
    num_digits = len(digits)
    armstrong_sum = sum([digit ** num_digits for digit in digits])
    return armstrong_sum == n

def is_perfect(n):
    """Checks if a number is a perfect number. Returns true or false"""
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_prime(n):
    """Checks if a number is a prime number. Returns true or false"""
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def cal_sum(n):
    """ Calculates and returns the sum of the digits of a number"""
    return sum([int(digit) for digit in str(n)])


@app.route("/api/classify-number", methods=['GET'])
def number_classify():
    """ returns mathematical properties about a passed number along with a fun fact"""
    number = request.args.get("number")

    # instance when not a 
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400  

    fun_fact = requests.get(f"http://numbersapi.com/{number}/math").text

    properties = []
    
    number = int(number)
    
    if (is_armstrong_number(number)):
        properties.append("armstrong")

    if (number % 2) == 0:
        properties.append("even")
    else:
        properties.append("odd")


    perfect = is_perfect(number)
    prime = is_prime(number)

    sum = cal_sum(number)

    data = {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": sum,
        "fun_fact": fun_fact
    }

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
