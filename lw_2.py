import csv
import random

'task 1'

#
# with open('books-en.csv') as f:
#     s = csv.reader(f, delimiter=';')
#     head = next(s)
#     s = list(s)
#
# answ = len(list(filter(lambda x: len(x[1]) > 30, s)))
# print(answ)

'task 2'

# with open('books.csv') as f:
#     s = list(csv.DictReader(f, delimiter=';'))
#
# def find_string(name):
#     books = []
#     c = 0
#     for row in s:
#         try:
#             year = int(row['Дата поступления'].split()[0].split('.')[-1])
#             if ((name in row['Автор'] or name in row['Автор (ФИО)']) and
#                     (year > 2018)):
#                 c += 1
#                 books.append(f'{row['Название']}, {year}')
#         except:
#             pass
#     if c == 0:
#         print('Ничего не найдено')
#     else:
#          print('\n'.join(books))
#
# while True:
#     author = input('Введите имя автора: ')
#     if author in ['', 0]:
#         break
#     else:
#         find_string(author)

'task 3'

with open('books.csv') as f:
    s = list(csv.DictReader(f, delimiter=';'))

print(s)