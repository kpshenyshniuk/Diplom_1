from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_available_buns(self):
        """Проверяем, что метод available_buns() возвращает список из 3 булочек"""
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(b.get_name() for b in buns)
        assert all(b.get_price() > 0 for b in buns)

    def test_database_available_ingredients(self):
        """Проверяем, что метод available_ingredients() возвращает список из 6 ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(i.get_name() for i in ingredients)
        assert all(i.get_price() > 0 for i in ingredients)
        assert any(i.get_type() == INGREDIENT_TYPE_SAUCE for i in ingredients)
        assert any(i.get_type() == INGREDIENT_TYPE_FILLING for i in ingredients)
