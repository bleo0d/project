import logging

logger = logging.getLogger(__name__)

class Menu:
    def __init__(self , title):
        self.title = title

    def show(self):
        for i , title in enumerate(self.title, start=1):
            print(f"{i}. {title}")
        while True:
            try:
                choice_a_punct = int(input("выберете пункт: "))

                if choice_a_punct < 1 or choice_a_punct > len(self.title):
                    logging.warning(" неверный пункт в меню, выбери от 1 до 4")
                    print("Ошибка введите число от 1 до 4")
                    continue

                return choice_a_punct

            except ValueError:
                logging.exception(" вы ввели букву а не число")
                print("Ошибка, вы ввели букву а не число")
