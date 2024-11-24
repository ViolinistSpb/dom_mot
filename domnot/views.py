from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import OrderForm
from .models import Order
from .services import parsing_grahl


@app.route('/')
def index_view():
    quantity = Order.query.count()
    orders = Order.query.all()
    return render_template('index.html', orders=orders, quantity=quantity)


@app.route('/add', methods=['GET', 'POST'])
def add_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = save_form(form)
        return redirect(url_for('order_view', id=order.id))
    return render_template('add.html', form=form)


@app.route('/<int:id>')
def order_view(id):
    order = Order.query.get_or_404(id)
    return render_template('order.html', order=order)


@app.route('/add_grahl', methods=['GET', 'POST'])
def add_grahl():
    data = parsing_grahl()
    form = OrderForm(
        number=data['number'],
        track_number=data['track_number']
    )
    # form.track_number.default = data['track_number']
    # form.process()
    if form.validate_on_submit():
        order = save_form(form)
        return redirect(url_for('order_view', id=order.id))
    print('not valid')
    return render_template('add.html', form=form)


def save_form(form):
    order = Order(
        company_name=form.company_name.data,
        number=form.number.data,
        weight=form.weight.data,
        track_number=form.track_number.data,
        price=form.price.data,
        meest_price=form.meest_price.data,
        clients=form.clients.data,
        status=form.status.data,
        comments=form.comments.data
        )
    db.session.add(order)
    db.session.commit()
    return order


# @app.route('/parsing/<string:slug>', methods=['GET', 'POST'])
# def parsing_view(slug):
#     print('parsing_view')
#     form = OrderForm()
#     comments = LINKS.get(slug)
#     print(comments)
#     # form.comments = comments
#     return redirect(url_for('add_order'), form=form)
