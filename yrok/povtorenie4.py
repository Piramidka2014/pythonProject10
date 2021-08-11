# # Задача 2 Является ли слово палиндромом написать функцию
# def reverse(s):
#     return s[::-1]
#
# def is_palindrome(s):
#     rev = reverse(s)
#
#     # проверка на совпадение 2х строк
#     if (s == rev):
#         return True
#     return False
#
# s = "ananas"
# pol = is_palindrome(s)
# print(pol)

# # Задача 1
# def card_num(card):
#     return '*' * len(card[:-4]) + card[-4:]

# # Задача 3
# class Tomato:
#     # Статическое поле
#     states = {0: 'nothing', 1: 'flower', 2: 'green', 3: 'red'}
#     def __init__(self, index, state):
#         # Protected свойства
#         self._index = index
#         self._state = 0
#
#     # следующая стадия созревания
#     def grow (self):
#         self._change_state()
#     #созрел ли томат
#
#     def is_ripe(self):
#             if self._state == 3:
#                 return True
#             return False
# class TomatoBush:
#
#     # Создаем список из объектов класса Tomato
#     def __init__(self, num):
#         self.tomatos = [Tomato(index) for index in range(0, num-1)]
#
#     # Переводим все томаты из списка на следующий этап созревания
#     def grow_all(self):
#         for tomato in self.tomatos:
#             tomato.grow()
#
#     # Проверяем, все ли помидоры созрели
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatos])
#
#     # Собираем урожай
#     def give_away_all(self):
#         self.tomatos = []
#
