import csv


def get_managers():
    with open('create_db/managers.csv', 'r') as f:
        reader = csv.DictReader(f)
        managers = [i for i in reader]
        return managers


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
