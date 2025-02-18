from sqlalchemy.orm import sessionmaker
from main import Publisher, Book, Shop, Sale, Stock

def add_objects(engine):
    session = sessionmaker(bind=engine)
    session = session()

    Publisher1 = Publisher(name="Пушкин")
    Publisher2 = Publisher(name="Лермонтов")
    Publisher3 = Publisher(name="Достоевский")

    session.add_all([Publisher1, Publisher2, Publisher3])
    session.commit()
    print(Publisher1.id, Publisher2.id, Publisher3.id)

    Book1 = Book(title="Война и мир", id_publisher=Publisher1.id)
    Book2 = Book(title="Капитанская дочка", id_publisher=Publisher1.id)
    Book3 = Book(title="Руслан и Людмила", id_publisher=Publisher1.id)  
    Book4 = Book(title="Евгений Онегин", id_publisher=Publisher1.id)    

    Book5 = Book(title="Герой нашего времени", id_publisher=Publisher2.id)
    Book6 = Book(title="Княжна Мери", id_publisher=Publisher2.id)  
    
    Book7 = Book(title="Преступление и наказание", id_publisher=Publisher3.id)
    session.add_all([Book1, Book2, Book3, Book4, Book5, Book6, Book7])
    session.commit()
    print(Book1.id, Book2.id, Book3.id, Book4.id, Book5.id, Book6.id, Book7.id)

    Shop1 = Shop(name="Буквоед")
    Shop2 = Shop(name="Лабиринт")
    session.add_all([Shop1, Shop2])
    session.commit()
    print(Shop1.id, Shop2.id)

    Stock11 = Stock(id_book=Book1.id, id_shop=Shop1.id, count=15)
    Stock12 = Stock(id_book=Book2.id, id_shop=Shop1.id, count=10)
    Stock13 = Stock(id_book=Book3.id, id_shop=Shop1.id, count=20)
    Stock14 = Stock(id_book=Book4.id, id_shop=Shop1.id, count=5)
    Stock15 = Stock(id_book=Book5.id, id_shop=Shop1.id, count=10)
    Stock16 = Stock(id_book=Book6.id, id_shop=Shop1.id, count=15)
    Stock17 = Stock(id_book=Book7.id, id_shop=Shop1.id, count=10)
    session.add_all([Stock11, Stock12, Stock13, Stock14, Stock15, Stock16, Stock17])
    session.commit()
    print(Stock11.id, Stock12.id, Stock13.id, Stock14.id, Stock15.id, Stock16.id, Stock17.id)

    Stock21 = Stock(id_book=Book1.id, id_shop=Shop2.id, count=10)
    Stock22 = Stock(id_book=Book2.id, id_shop=Shop2.id, count=20)
    Stock23 = Stock(id_book=Book3.id, id_shop=Shop2.id, count=20)
    Stock24 = Stock(id_book=Book4.id, id_shop=Shop2.id, count=15)
    Stock25 = Stock(id_book=Book5.id, id_shop=Shop2.id, count=14)
    Stock26 = Stock(id_book=Book6.id, id_shop=Shop2.id, count=12)
    Stock27 = Stock(id_book=Book7.id, id_shop=Shop2.id, count=8)
    session.add_all([Stock21, Stock22, Stock23, Stock24, Stock25, Stock26, Stock27])
    session.commit()
    print(Stock21.id, Stock22.id, Stock23.id, Stock24.id, Stock25.id, Stock26.id, Stock27.id)

    Sales = [(600, '2024-01-01', 1), 
             (500, '2024-01-02', 4), 
             (700, '2024-01-03', 5),
             (800, '2024-01-04', 7),
             (900, '2024-01-05', 9),
             (1000, '2024-01-06', 11),
             (1200, '2024-01-07', 13),
             (1300, '2024-01-08', 14)
             ]
    
    for sale in Sales:
        Stock_data = session.query(Stock).filter(Stock.id == sale[2]).first()
        if Stock_data:
            Sale_result = Sale(price=sale[0], date_sale=sale[1], id_stock=sale[2], count=1)
            Stock_data.count = Stock_data.count - Sale_result.count
            session.add_all([Sale_result])
    session.commit()
    print("Записи успешно добавлены")