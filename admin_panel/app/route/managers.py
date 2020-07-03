from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import login_required
from models.models import Manager, Store
from db import db

managers = Blueprint('managers', __name__)

@managers.route('/create_meneger', methods=['GET','POST'])
@login_required
def create_manager():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        position = request.form.get('position')
        phone = int(request.form.get('phone'))
        s = request.form.get('store')
        stores = Store.query.filter_by(name=s).first()
        store_id = int(stores.id_store)
        try:
            manager = Manager(name=name, email=email, position=position, phone=phone, store_id=store_id)
            print(manager)
            db.session.add(manager)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))

    stores = Store.query.all()
    return render_template('manager/create_manager.html',stores=stores)


@managers.route('/update_meneger', methods=['GET', "POST"])
@login_required
def update_manager():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            m = Manager.query.get(id)
            m.name = request.form.get('name')
            m.email = request.form.get('email')
            m.position = request.form.get('position')
            m.phone = int(request.form.get('phone'))
            m.store_id = int(request.form.get('store'))
            db.session.commit()
            print(m.name, m.phone, m.id_manager)
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    else:
        q = request.args.get('q')
        m=''
        if q:
            m = Manager.query.filter(Manager.name.contains(q)).first()

        return render_template('manager/update_manager.html', m=m)

@managers.route('/delete_manager', methods=['GET','POST'])
@login_required
def delete_manager():
    if request.method == 'POST':
        try:
            id = request.form.get('id')
            m = Manager.query.get(id)
            db.session.delete(m)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('homePage.index'))
    else:
        q = request.args.get('q')
        m=''
        if q:
            m = Manager.query.filter(Manager.name.contains(q)).first()
        print(m)
        return render_template('manager/delete_manager.html', m=m)


@managers.route('/')
@login_required
def get_managers():
    s = Store.query.all()
    u = Manager.query.order_by(Manager.name).all()
    return render_template('manager/managers.html', u=u, s=s)
