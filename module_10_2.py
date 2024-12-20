# импорт из модуля threading класса Thread для создания потока(ов)
from threading import Thread
# импорт из модуля time функции sleep
from time import sleep

# объявление класса Knight наследованного от Thread
class Knight(Thread):
    
    # метод инициализации героя в классе
    def __init__(self, name, power):
        self.lancelot = name
        self.power = power
        super().__init__()

    # метод реализации битвы с врагами
    def run(self):
        print(f'{self.lancelot}, на нас напали!')
        # объявление количества врагов
        enemy = 100
        # объявление начала битвы с врагами
        day = 0
        # цикл while проверки остатка врагов и количества дней битвы
        while enemy > 0:
            # убыль врагов в зависимости от силы героя
            enemy -= self.power
            # увелиение количества дней битвы
            day += 1
            # пауза выполнение цикла
            sleep(1)
            print(f'{self.lancelot} сражается {day}, осталось {enemy} воинов')
        # когда враг разбит
        print(f'{self.lancelot} одержал победу спустя {day} дней(дня)!')


# исходные данные
# обращение к классу Knight
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# метод запуск потоков
first_knight.start()
second_knight.start()

# метод join для останова выполненного потока
first_knight.join()
second_knight.join()

print('Все враги повержены!')