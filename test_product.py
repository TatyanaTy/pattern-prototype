import pytest
from product import Product, ProductRegistry


def test_clone_creates_new_object():
    """Тест 1: Клон - это новый объект"""
    original = Product("Футболка", "Одежда", 999, "M", "Черный")
    cloned = original.clone()
    
    assert original is not cloned, "Клон должен быть новым объектом"
    assert original.name == cloned.name, "Имена должны совпадать"
    assert original.price == cloned.price, "Цены должны совпадать"


def test_clone_independent():
    """Тест 2: Изменения в клоне не влияют на оригинал"""
    original = Product("Ноутбук", "Электроника", 1500, "15 дюймов", "Серый")
    cloned = original.clone()
    
    cloned.name = "Ноутбук Pro"
    cloned.price = 2000
    
    assert original.name == "Ноутбук", "Оригинал не должен меняться"
    assert original.price == 1500, "Цена оригинала не должна меняться"
    assert cloned.name == "Ноутбук Pro", "Клон должен измениться"
    assert cloned.price == 2000, "Цена клона должна измениться"


def test_registry_works():
    """Тест 3: Реестр работает правильно"""
    registry = ProductRegistry()
    prototype = Product("Кроссовки", "Обувь", 4500, "42", "Белый")
    
    registry.register("sneakers", prototype)
    copied = registry.create_copy("sneakers")
    
    assert copied is not None, "Копия должна создаться"
    assert copied is not prototype, "Копия должна быть новым объектом"
    assert copied.name == "Кроссовки", "Имя должно совпадать"
    assert copied.price == 4500, "Цена должна совпадать"


def test_registry_not_found():
    """Тест 4: Обработка ошибки - прототип не найден"""
    registry = ProductRegistry()
    result = registry.create_copy("nonexistent")
    
    assert result is None, "Должен вернуться None"


def test_clone_all_attributes():
    """Тест 5: Все атрибуты копируются"""
    original = Product("Телефон", "Электроника", 50000, "6.7 дюймов", "Синий")
    cloned = original.clone()
    
    assert cloned.name == original.name
    assert cloned.category == original.category
    assert cloned.price == original.price
    assert cloned.size == original.size
    assert cloned.color == original.color
    
def test_this_will_fail():
    """Тест 6: СПЕЦИАЛЬНО ПАДАЕТ - для демонстрации CI/CD"""
    original = Product("Тест", "Тестовый", 100)
    cloned = original.clone()
    
    # ЭТОТ ТЕСТ ВСЕГДА БУДЕТ ПАДАТЬ
    assert original is cloned, "Демонстрационная ошибка для преподавателя"


