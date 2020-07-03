import csv


def get_users():
    with open('create_db/users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
        return users


def get_goods():
    with open('create_db/goods.csv', 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
        return goods


def get_store():
    with open ('create_db/stores.csv', 'r') as f:
        reader = csv.DictReader(f)
        stores = [i for i in reader]
        return stores
