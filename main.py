from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import Adding_data
import config 

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Book(Base):
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    id_publisher = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    publisher = relationship("Publisher")

class Shop(Base):
    __tablename__ = 'shop'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Stock(Base):
    __tablename__ = 'stock'
    
    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id'), nullable=False)
    id_shop = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer, default=0)
    book = relationship("Book")
    shop = relationship("Shop")

class Sale(Base):
    __tablename__ = 'sale'
    
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    date_sale = Column(Date, nullable=False)
    id_stock = Column(Integer, ForeignKey('stock.id'), nullable=False)
    stock = relationship("Stock")
    count = Column(Integer, default=0)

def connect_to_postgres():
    engine = create_engine(config.connection_string)
    return engine

def init_db(engine, operation: int):
    if operation == 1:
        Base.metadata.create_all(engine)
    elif operation == 2:
        Base.metadata.drop_all(engine)

def user_request(engine):
    session = sessionmaker(bind=engine)
    session = session()

    variable = input("Введите Фамилию автора или  id_publisher: --> : ")
    result = session.query(Book.title, Shop.name, Sale.count, Sale.date_sale).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)
    
    if variable.isdigit(): 
        sales = result.filter(Publisher.id == int(variable)).all()
    else:
        sales = result.filter(Publisher.name == variable).all() 
    for a, b, c, d in sales: 
        print(f"{a: <40} | {b: <10} | {c: <8} | {d.strftime('%d-%m-%Y')}") 
        
if __name__ == '__main__':
    greate_delete = input("Создать таблицы: 1, Удалить таблицы: 2. ---> ")
    engine = connect_to_postgres()
    if greate_delete == "1":
        init_db(engine, 1)
        Adding_data.add_objects(engine)
        user_request(engine)
    elif greate_delete == "2":
        init_db(engine, 2)
    else:
        print("Неверный ввод")
        
