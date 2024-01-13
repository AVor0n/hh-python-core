from wine import Wine
from beer import Beer
from market import Market
from logger import log_execution_time
"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

# Пример использования

wine1 = Wine("Вино 1", "2022-01-01")
wine2 = Wine("Вино 2", "2022-02-01")
wine3 = Wine("Вино 3", "2022-03-01")
beer1 = Beer("Пиво 1", "2022-04-01")
beer2 = Beer("Пиво 2", "2022-05-01")

market = Market([wine1, wine2, wine3], [beer2, beer1])

print(market.has_drink_with_title("Вино 1"))
print(market.has_drink_with_title("Пиво 3"))

sorted_drinks = market.get_drinks_sorted_by_title()
for drink in sorted_drinks:
    print(drink.title)

drinks_by_date = market.get_drinks_by_production_date("2022-02-01", "2022-04-01")
for drink in drinks_by_date:
    print(drink.title)
