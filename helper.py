from random import randint

class Helper:

    @staticmethod
    def generate_email():
        return f"peretat+{randint(1000,9999)}@ya.ru"