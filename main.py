import json
import os
from src.classes import Category, Product

file = 'data/products.json'


def read_json(path: str):
    """Функция чтения json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data


def append_list_product():
    data = read_json(file)
    products = []
    goods = []
    for category in data:
        for product in category['products']:
            # products.append(Product(**product))
            goods.append(product)
    return goods


pt = append_list_product()
ct = Category("Смартфоны", "Смартфоны, как средство", pt)


