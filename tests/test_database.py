from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_available_buns_length(self):
        """Проверяем, что метод available_buns() возвращает 3 булочки"""
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_database_available_buns_have_names(self):
        """Проверяем, что у всех булочек есть названия"""
        db = Database()
        buns = db.available_buns()
        assert all(b.get_name() for b in buns)

    def test_database_available_buns_have_prices(self):
        """Проверяем, что у всех булочек цена больше 0"""
        db = Database()
        buns = db.available_buns()
        assert all(b.get_price() > 0 for b in buns)

    def test_database_available_ingredients_length(self):
        """Проверяем, что метод available_ingredients() возвращает 6 ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_database_available_ingredients_have_names(self):
        """Проверяем, что у всех ингредиентов есть названия"""
        db = Database()
        ingredients = db.available_ingredients()
        assert all(i.get_name() for i in ingredients)

    def test_database_available_ingredients_have_prices(self):
        """Проверяем, что у всех ингредиентов цена больше 0"""
        db = Database()
        ingredients = db.available_ingredients()
        assert all(i.get_price() > 0 for i in ingredients)

    def test_database_available_ingredients_have_sauces(self):
        """Проверяем, что среди ингредиентов есть хотя бы один соус"""
        db = Database()
        ingredients = db.available_ingredients()
        assert any(i.get_type() == INGREDIENT_TYPE_SAUCE for i in ingredients)

    def test_database_available_ingredients_have_fillings(self):
        """Проверяем, что среди ингредиентов есть хотя бы одна начинка"""
        db = Database()
        ingredients = db.available_ingredients()
        assert any(i.get_type() == INGREDIENT_TYPE_FILLING for i in ingredients)
