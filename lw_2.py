import csv
import random
from os import write
import xml.dom.minidom as mdom

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

# answ = []
# with open('books.csv') as f:
#     s = list(csv.DictReader(f, delimiter=';'))
#     for _ in range(20):
#         row = random.choice(s)
#         answ.append(row)
# f = open('lw_2_task3.txt', 'w', encoding='utf-8')
# for index, el in enumerate(answ, start=1):
#     f.write(f'{index} {el['Автор']}. {el['Название']} - {el['Дата поступления'].split()[0].split('.')[-1]}')
#     f.write('\n')
# f.close()

'task 4'

# import xml.dom.minidom as minidom
#
# xml_file = open('currency.xml')
# xml_data = xml_file.read()
#
# dom  = minidom.parseString(xml_data) # dom = document object module
# dom.normalize()
#
# elements1 = dom.getElementsByTagName('Name')
# elements2= dom.getElementsByTagName('CharCode')
# dict = {}
# sp1 = []
# sp2 = []
#
# def lis(elem, sp):
#     for node in elem:
#         for child in node.childNodes:
#                 if child.nodeType == 3:
#                         sp.append(child.data)
#     return sp
#
#
# sp1 = lis(elements1, sp1)
# sp2 = lis(elements2, sp2)
#
# for i in range(len(sp1)):
#     dict[sp1[i]] = sp2[i]
#
# print(dict)

'extra'

# with open('books.csv') as f:
#     s = csv.reader(f, delimiter=';')
#     head = next(s)
#     s = list(s)
#
# s2 = sorted(s, key=lambda x: int(x[8]), reverse=True)
# print(head)
# for i in range(20):
#     print(s2[i][1], s2[i][8])
