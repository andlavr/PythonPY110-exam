import json
import random
from conf import model
from faker import Faker
# print(model)


def main():
    '''в функции задаем стартовый номер книги, записвает условие генератора и создаем список'''
    my_num = int(input("Введите целое число от 1 до 100"))
    pk = 1
    if 1 <= my_num <= 100:
        if my_num >= pk:
            pk = my_num
            number_of_books = 100
            library_list = []

            for book_ in range(pk, number_of_books+1):
                x_ = next(generator(book_))
                library_list.append(x_)


                with open('JSON_books.json', 'w') as file:
                    json.dump(library_list, file, indent=4, ensure_ascii=False)

def generator(book_= 1):
    all_books_ = {'model:': model,
                  'pk:': book_,
                  'fields': {
                      'title:': title(),
                      'year:': year(),
                      'pages:': pages(),
                      'ISBN13': isbn_(),
                      'rating:': rating(),
                      'price:': price(),
                      'author:': author()
                  }
                  }
    yield all_books_

def title():
    '''Достаем из файла название книги '''
    with open('books.txt', 'r', encoding='utf8') as file_:
        for line in(file_):
            row_ = file_.readlines()
            row_ = [y.strip() for y in row_]
            row_random = random.choice(row_)
    title = row_random

    return title

def year():
    """"Генерируем год"""
    year = random.randrange(1990, 2020)
    return year

def pages():
    """"Генерируем кол-во страниц"""
    pages = random.randint(10, 500)
    return pages

def isbn_():
    """"Создаем номер isbn"""
    fake = Faker()
    Faker.seed(0)
    for _ in range(5):
        isbn_ = fake.isbn13()
    return isbn_

def rating():
    """"Рейтинг книги"""
    rating = round(random.uniform(0, 5), 3)
    return rating

def price():
    """"Цена книги"""
    price = round(random.uniform(500, 3000), 2)
    return price

def author():
    """"Генерируем имя автора книги"""
    count_ = random.randint(1, 3)
    for _ in range(count_):
        fake = Faker()
        author = fake.name()
    return author
    # print(f'Name: {fake.name()}')

if __name__ == '__main__':
    main()
    print(main())
