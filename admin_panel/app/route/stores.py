from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import login_required
from models.models import Store
from db import db


stores = Blueprint('stores', __name__)

@stores.route('/create_stores', methods=['GET', 'POST'])
@login_required
def create_stores():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        address = request.form.get('address')
        try:
            s = Store(name=name, city=city, address=address)

            db.session.add(s)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))

    return render_template('store/create_stores.html')


@stores.route('/update_store', methods=['GET', 'POST'])
@login_required
def update_stores():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            s = Store.query.get(id)
            s.name = request.form.get('name')
            s.city = request.form.get('city')
            s.address = request.form.get('address')
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    else:
        q = request.args.get('q')
        s=''
        if q:
            s = Store.query.filter(Store.name.contains(q)).first()
        return render_template('store/update_store.html', s=s)

@stores.route('/delete_store', methods=['GET','POST'])
@login_required
def delete_stores():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            s = Store.query.get(id)
            db.session.delete(s)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    else:
        q = request.args.get('q')
        s=''
        if q:
            s = Store.query.filter(Store.name.contains(q)).first()
        return render_template('store/delete_store.html', s=s)


@stores.route('/')
def get_stores():
    s = Store.query.order_by(Store.name).all()
    return render_template('store/stores.html', s=s)
