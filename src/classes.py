class Category:
    name: str
    description: str
    goods: list
    common_count_product: int
    common_count_category: int

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, value):
        self.__goods.append(value)

    def count_goods(self):
        return len(self.__goods)


class Product:
    name: str
    description: str
    price: float
    ct: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def count_product(self):
        return self.quantity


