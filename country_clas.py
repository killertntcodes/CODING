from abc import ABC, abstractmethod
class country(ABC):
    def info(self):
        pass
class india(country):
        def capital(self):
            print("New Delhi")
        def language(self):
            print("Hindi")
        def type(self):
            print("India is a developing country")
class uae(country):
        def capital(self):
            print("Abu Dhabi")
        def language(self):
            print("Arabic")
        def type(self):
            print("UAE is a developed country")
uae_obj = uae()
india_obj = india()

for country in (uae_obj, india_obj):
    country.capital()
    country.language()
    country.type()