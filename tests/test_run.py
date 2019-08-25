from currency_converter.run import app
from flask import json


def test_convert_currency():
    response = app.test_client().post(
        '/convert',
        data=json.dumps({
            'currency1': 'PLN',
            'currency2': 'USD',
            'value1': 100
        })
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert 'value2' in data


def test_convert_currency_missing_field():
    response = app.test_client().post(
        '/convert',
        data=json.dumps({
            'currency2': 'USD',
            'value1': 100
        })
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert 'currency1' in data


def test_convert_currency_wrong_data_type():
    response = app.test_client().post(
        '/convert',
        data=json.dumps({
            'currency1': 1000,
            'currency2': 'USD',
            'value1': 100
        })
    )
    assert response.status_code == 400


def test_convert_currency_wrong_currency_value():
    response = app.test_client().post(
        '/convert',
        data=json.dumps({
            'currency1': 'Sierotka',
            'currency2': 'Marysia',
            'value1': -500
        })
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert 'currency1' in data
    assert 'currency2' in data
    assert 'value1' in data
