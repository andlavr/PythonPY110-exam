import random
from conf import model
# print(model)

year = random.randrange(1990, 2020)  # генерируем год
pages = random.randrange(10, 500) # генерируем кол-во страниц

from faker import Faker
fake = Faker()       # создаем номер isbn
Faker.seed(0)
for _ in range(5):
    isbn_ = fake.isbn13()
    # print(isbn_)

rating = random.uniform(0, 5)  # рейтинг книги
price = random.uniform(500, 3000)  # цена книги

from faker import Faker   # генерируем имя
fake = Faker()
for _ in range(1, 4):
    author = fake.name()
    # print(f'Name: {fake.name()}')

with open('books.txt', 'r', encoding='utf8') as file_:
    for line in(file_):
        file_.read()
title = line


def generator(a):
    fields = {'title:': title, 'year:': year, 'pages:': pages, 'ISBN13': isbn_, 'rating:': rating, 'price:': price, 'author:': author }
    pk = 1
    main_spisok = {'model:': model, 'fields': fields}
    for main_spisok in range(a):
        pk = pk+1
    yield main_spisok

if __name__ == " main ":
    my_gen = generator(6)

    print(next(my_gen))