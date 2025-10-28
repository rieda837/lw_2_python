import csv
import random
from os import write

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

# answ = []
# with open('books.csv') as f:
#     s = list(csv.reader(f, delimiter=';'))
#     for _ in range(20):
#         row = random.choice(s)
#         answ.append(row)
# f = open('lw_2_task3.txt', 'w', encoding='utf-8')
# for index, el in enumerate(answ, start=1):
#     f.write(f'{index} {el[3]}. {el[1]} - {el[6].split()[0].split('.')[-1]}')
#     f.write('\n')
# f.close()

answ = []
with open('books.csv') as f:
    s = list(csv.DictReader(f, delimiter=';'))
    for _ in range(20):
        row = random.choice(s)
        answ.append(row)
f = open('lw_2_task3.txt', 'w', encoding='utf-8')
for index, el in enumerate(answ, start=1):
    f.write(f'{index} {el['Автор']}. {el['Название']} - {el['Дата поступления'].split()[0].split('.')[-1]}')
    f.write('\n')
f.close()

'task 4'
