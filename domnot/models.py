from datetime import datetime

from sqlalchemy.orm import relationship

from . import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    company_name = db.Column(db.String(16), nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True, default='')
    weight = db.Column(db.Integer, default=0)
    track_number = db.Column(
        db.String(16), nullable=False, unique=True, default='нет данных')
    price = db.Column(db.Integer, default=0)
    meest_price = db.Column(db.Integer, default=0)
    clients = db.Column(db.String(64), default='нет данных')
    status = db.Column(db.String(16), nullable=False, default='new order')
    comments = db.Column(db.Text, default='')
    reciever_id = db.Column(db.Integer, db.ForeignKey('reciever.id'))


class Receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    index = db.Column(db.Integer, nullable=False)
    adress = db.Column(db.String(100))
    count = db.Column(db.Integer, default=0)
    deliveries = relationship('Order')
