from bun import Bun


class TestBun:

    def test_bun_get_name(self):
        """Проверяем, что метод get_name() возвращает корректное имя булочки"""
        bun = Bun("Sesame Bun", 1.50)
        assert bun.get_name() == "Sesame Bun"

    def test_bun_get_price(self):
        """Проверяем, что метод get_price() возвращает корректную цену булочки"""
        bun = Bun("Sesame Bun", 1.50)
        assert bun.get_price() == 1.50
