from burger import Burger
from bun import Bun
from ingredient import Ingredient
from unittest.mock import Mock


class TestBurger:

    def test_burger_set_buns(self):
        """Проверяем, что можно установить булочку в бургер"""
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Sesame Bun"
        burger.set_buns(bun)
        assert burger.bun.get_name() == "Sesame Bun"

    def test_burger_add_ingredient(self):
        """Проверяем, что можно добавить ингредиент в бургер"""
        burger = Burger()
        ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_burger_remove_ingredient(self):
        """Проверяем, что можно удалить ингредиент из бургера"""
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert ingredient1 not in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_burger_get_price(self):
        """Проверяем, что цена бургера считается корректно"""
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 2.00
        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 1.00
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 1.50
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_price = (2.00 * 2) + 1.00 + 1.50
        assert burger.get_price() == expected_price

    def test_move_ingredient(self):
        """Проверяем, что можно изменить порядок ингредиентов в бургере"""
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)  # Перемещаем первый ингредиент на третье место

        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_burger_get_receipt(self):
        """Проверяем, что чек бургера формируется корректно"""
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Sesame Bun"
        burger.set_buns(bun)
        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = "Cheese"
        ingredient1.get_type.return_value = "FILLING"
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = "Lettuce"
        ingredient2.get_type.return_value = "VEGGIE"
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.get_price = Mock(return_value=5.50)
        expected_receipt = """(==== Sesame Bun ====)
= filling Cheese =
= veggie Lettuce =
(==== Sesame Bun ====)

Price: 5.5"""
        assert burger.get_receipt() == expected_receipt
