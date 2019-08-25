from flask import Flask, request
import requests
from money import Money
from decimal import Decimal

from config import APP_PORT, CURRENCY_RATE_API_URL
from schemas import ConvertCurrencySchema

app = Flask(__name__)
convert_schema = ConvertCurrencySchema()

@app.route('/convert', methods=['POST'])
def convert_currency():
    json_data = request.get_json(force=True, silent=True)
    errors = convert_schema.validate(json_data)

    if errors:
        return errors, 400

    base_currency, output_currency = json_data['currency1'], json_data['currency2']
    amount = json_data['value1']
    money_value = Money(amount=amount, currency=base_currency)

    response = requests.get(CURRENCY_RATE_API_URL, params={'base': base_currency})
    rates_response = response.json()

    output_value = Decimal(rates_response['rates'][output_currency]) * money_value
    return {**json_data,
            'value2': str(output_value.amount)
            }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=APP_PORT)
