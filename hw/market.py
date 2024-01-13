from logger import log_execution_time

class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {}
        self.beers = {}
        if wines:
            for wine in wines:
                self.wines[wine.title] = wine
        if beers:
            for beer in beers:
                self.beers[beer.title] = beer

    @log_execution_time
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.wines or title in self.beers


    @log_execution_time
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        sorted_drinks = sorted(drinks, key=lambda drink: drink.title)
        return sorted_drinks

    @log_execution_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        filtered_drinks = list(filter(lambda drink: from_date <= drink.production_date <= to_date, drinks))
        return filtered_drinks
