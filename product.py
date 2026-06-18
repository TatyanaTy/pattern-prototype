import copy


class Product:
    """Класс товара - реализация паттерна Prototype"""
    
    def __init__(self, name, category="Без категории", price=0.0, size="Стандартный", color="Белый"):
        self.name = name
        self.category = category
        self.price = price
        self.size = size
        self.color = color
    
    def clone(self):
        """Создает полную копию товара"""
        return copy.deepcopy(self)
    
    def show(self):
        """Выводит информацию о товаре"""
        print(f"Товар: {self.name}")
        print(f"  Категория: {self.category}")
        print(f"  Цена: {self.price} руб")
        print(f"  Размер: {self.size}")
        print(f"  Цвет: {self.color}")
        print("---")


class ProductRegistry:
    """Реестр прототипов - хранит и создает копии товаров"""
    
    def __init__(self):
        self.prototypes = {}
    
    def register(self, key, prototype):
        """Регистрирует прототип"""
        self.prototypes[key] = prototype
        print(f"Зарегистрирован прототип: {key}")
    
    def create_copy(self, key):
        """Создает копию по ключу"""
        if key in self.prototypes:
            print(f"Создаем копию: {key}")
            return self.prototypes[key].clone()
        else:
            print(f"Ошибка: прототип '{key}' не найден")
            return None
