import datetime


class Estimate:

    def __init__(self, date_now):
        self.start_time = date_now
        print('Старт контекста ...')

    def __enter__(self):
        j = 0
        for i in range(1000000):
            j = i + j
        self.code_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Время запуска кода :', self.start_time)
        print('Время выполнения кода :', self.code_time)
        print('Потрачено времени :', self.code_time - self.start_time)


with Estimate(datetime.datetime.now()) as est:
    print('Работа контекста')
print('Все, кина не будет  - электричество кончилось')
