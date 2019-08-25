from marshmallow import Schema, fields, validates, ValidationError
from utils import currencies


class ConvertCurrencySchema(Schema):
    currency1 = fields.Str(required=True)
    currency2 = fields.Str(required=True)
    value1 = fields.Decimal(required=True, as_string=True)

    @validates('currency1')
    def currency1_validation(self, value):
        self.validate_currency(value)

    @validates('currency2')
    def currency2_validation(self, value):
        self.validate_currency(value)

    @validates('value1')
    def value_validation(self, value):
        if value < 0:
            raise ValidationError(f' Value1 must be greater than 0!')

    def validate_currency(self, value):
        if value not in currencies:
            raise ValidationError(f'Invalid currency: {value}')
