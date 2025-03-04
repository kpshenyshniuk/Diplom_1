import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Ketchup", 0.50),
        (INGREDIENT_TYPE_SAUCE, "BBQ Sauce", 0.75),
        (INGREDIENT_TYPE_FILLING, "Beef Patty", 3.00),
        (INGREDIENT_TYPE_FILLING, "Chicken Patty", 2.50)
    ])
    def test_ingredient_returns_correct_values(self, ingredient_type, name, price):
        """Проверяем, что Ingredient корректно возвращает тип, имя и цену"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
