from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from models.models import Good
from db import db
from flask_login import login_required


goods = Blueprint('goods', __name__)


@goods.route('/create_good', methods=['GET', 'POST'])
@login_required
def create_goods():
    if request.method == 'POST':
        brand = request.form.get('brand')
        name = request.form.get('name')
        price = request.form.get('price')
        try:
            goods = Good(brand=brand, name=name, price=price)
            db.session.add(goods)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    form = GoodForm()
    return render_template('goods/create_goods.html', form=form)


@goods.route('/update_goods', methods=['GET', 'POST'])
@login_required
def update_goods():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            g = Good.query.get(id)
            g.brand = request.form.get('brand')
            g.name = request.form.get('name')
            g.price = request.form.get('price')
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    else:
        q = request.args.get('q')
        g=''
        if q:
            g = Good.query.filter(Good.brand.contains(q)).first()
        return render_template('goods/update_goods.html', g=g)


@goods.route('/delete_good', methods=['GET','POST'])
@login_required
def delete_good():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            g = Good.query.get(id)
            db.session.delete(g)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    else:
        q = request.args.get('q')
        g=''
        if q:
            g = Good.query.filter(Good.brand.contains(q)).first()
        return render_template('goods/delete_good.html', g=g)


@goods.route('/')
def get_goods():
    g = Good.query.order_by(Good.brand).all()
    return render_template('goods/goods.html', g=g)
