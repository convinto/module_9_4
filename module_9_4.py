from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = lambda x, y: list(x) == list(y)    #лямбда
res = list(map(result, first, second))
print(res)  #пример работы кода



def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:    #создание файла и добавление в него данных
            for i in data_set:
                file.write(str(i) + '\n')
        return
    return write_everything

#пример работы кода
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)


#пример работы кода
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
