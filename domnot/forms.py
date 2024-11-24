from flask_wtf import FlaskForm
from wtforms import (
    DateField, StringField, SubmitField, IntegerField,
    TextAreaField, SelectField
)
from wtforms.validators import DataRequired, Optional

class OrderForm(FlaskForm):
    # timestamp = DateField(
    #     "Введите дату, если она отличается от сегодняшней",
    #     validators=[Optional()])
    company_name = SelectField(
        "Поставщик",
        choices=['Grahl', 'Baerenreiter', 'Petz'],
        validate_choice=False,
        # validators=[DataRequired(message='Обязательное поле')],
        # default='',
    )
    number = IntegerField(
        "Номер инвойса (последние 4 цифры)",
        validators=[DataRequired(message='Обязательное поле')]
    )
    weight = IntegerField(
        "Общий вес посылки",
        validators=[Optional()]
    )
    track_number = IntegerField("Трек номер",
                                validators=[Optional()])
    price = IntegerField("Стоимость посылки",
                         validators=[Optional()])
    meest_date = DateField("Дата отправки Meest",
                           validators=[Optional()])
    meest_price = IntegerField("Стоимость пересылки Meest",
                               validators=[Optional()])
    clients = StringField("Получатели посылок",
                          validators=[Optional()])
    status = SelectField("Статус посылки",
                         choices=['new order', 'send to meest',
                                  'send from meest',
                                  'in russia', 'delivered'])
    comments = TextAreaField('Комментарии',
                             validators=[Optional()])
    submit = SubmitField('Создать')
