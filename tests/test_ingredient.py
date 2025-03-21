import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type(self, ingredient_type):
        """Проверяем, что get_type() возвращает правильный тип"""
        ingredient = Ingredient(ingredient_type, "Test", 1.00)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["Ketchup", "BBQ Sauce", "Beef Patty", "Chicken Patty"])
    def test_ingredient_get_name(self, name):
        """Проверяем, что get_name() возвращает правильное имя"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 1.00)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [0.50, 0.75, 3.00, 2.50])
    def test_ingredient_get_price(self, price):
        """Проверяем, что get_price() возвращает правильную цену"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Test", price)
        assert ingredient.get_price() == price
