import multiprocessing
from database import Database
import time
from datetime import datetime

query_insert_1 = {
    "query_1": "INSERT INTO person VALUES('Zoirjon',31,'jalilov@gmail.com',974774445)",
    "query_2": "INSERT INTO person VALUES('Zaxro',13,'zaxro@gmail.com',975551111)",
    "query_3": "INSERT INTO person VALUES('Zumrad',20,'zumrad@gmail.com',900077007)",
    "query_4": "INSERT INTO person VALUES('Zinnura',18,'zinnur@gmail.com',984001000)",
    "query_5": "INSERT INTO person VALUES('Zarina',35,'zari@gmail.com',999244445)",
}

query_insert_2 = {
    "query_6": "INSERT INTO car VALUES('BMW','Black',100.000,2024)",
    "query_7": "INSERT INTO car VALUES('Nissan','Blue',50.000,2020)",
    "query_8": "INSERT INTO car VALUES('Audi','Rad',25.000,2010)",
    "query_9": "INSERT INTO car VALUES('GM','Yellow',10.000,2006)",
    "query_10": "INSERT INTO car VALUES('Mers','Green',250.000,2023)",
}

query_insert_3 = {
    "query_11": "INSERT INTO phone VALUES('Iphone',1000,'Black',512)",
    "query_12": "INSERT INTO phone VALUES('Iphone',900,'Blue',128)",
    "query_13": "INSERT INTO phone VALUES('Galaxy',700,'Rad',256)",
    "query_14": "INSERT INTO phone VALUES('RedMe',500,'White',128)",
    "query_15": "INSERT INTO phone VALUES('Nokia',150,'Silver',64)",
}


def insert_data(query, query_type):
    print(Database.connect(query, query_type))


def process():
    query_1 = "INSERT INTO person VALUES('Zoirjon',31,'jalilov@gmail.com',974774445)",
    query_2 = "INSERT INTO person VALUES('Zaxro',13,'zaxro@gmail.com',975551111)",
    query_3 = "INSERT INTO person VALUES('Zumrad',20,'zumrad@gmail.com',900077007)",
    query_4 = "INSERT INTO person VALUES('Zinnura',18,'zinnur@gmail.com',984001000)",
    query_5 = "INSERT INTO person VALUES('Zarina',35,'zari@gmail.com',999244445)",
    query_6 = "INSERT INTO car VALUES('BMW','Black',100.000,2024)",
    query_7 = "INSERT INTO car VALUES('Nissan','Blue',50.000,2020)",
    query_8 = "INSERT INTO car VALUES('Audi','Rad',25.000,2010)",
    query_9 = "INSERT INTO car VALUES('GM','Yellow',10.000,2006)",
    query_10 = "INSERT INTO car VALUES('Mers','Green',250.000,2023)",
    query_11 = "INSERT INTO phone VALUES('Iphone',1000,'Black',512)",
    query_12 = "INSERT INTO phone VALUES('Iphone',900,'Blue',128)",
    query_13 = "INSERT INTO phone VALUES('Galaxy',700,'Rad',256)",
    query_14 = "INSERT INTO phone VALUES('RedMe',500,'White',128)",
    query_15 = "INSERT INTO phone VALUES('Nokia',150,'Silver',64)",

    query_type_1 = "INSERT"
    query_type_2 = "INSERT"
    query_type_3 = "INSERT"
    query_type_4 = "INSERT"
    query_type_5 = "INSERT"
    query_type_6 = "INSERT"
    query_type_7 = "INSERT"
    query_type_8 = "INSERT"
    query_type_9 = "INSERT"
    query_type_10 = "INSERT"
    query_type_11 = "INSERT"
    query_type_12 = "INSERT"
    query_type_13 = "INSERT"
    query_type_14 = "INSERT"
    query_type_15 = "INSERT"

    process1 = multiprocessing.Process(target=insert_data, args=query_1),
    process2 = multiprocessing.Process(target=insert_data, args=query_2),
    process3 = multiprocessing.Process(target=insert_data, args=query_3),
    process4 = multiprocessing.Process(target=insert_data, args=query_4),
    process5 = multiprocessing.Process(target=insert_data, args=query_5),
    process6 = multiprocessing.Process(target=insert_data, args=query_6),
    process7 = multiprocessing.Process(target=insert_data, args=query_7),
    process8 = multiprocessing.Process(target=insert_data, args=query_8),
    process9 = multiprocessing.Process(target=insert_data, args=query_9),
    process10 = multiprocessing.Process(target=insert_data, args=query_10),
    process11 = multiprocessing.Process(target=insert_data, args=query_11),
    process12 = multiprocessing.Process(target=insert_data, args=query_12),
    process13 = multiprocessing.Process(target=insert_data, args=query_13),
    process14 = multiprocessing.Process(target=insert_data, args=query_14),
    process15 = multiprocessing.Process(target=insert_data, args=query_15),

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()
    process10.start()
    process11.start()
    process12.start()
    process13.start()
    process13.start()
    process14.start()
    process15.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()
    process9.join()
    process10.join()
    process11.join()
    process12.join()
    process13.join()
    process14.join()
    process15.join()


if __name__ == "__main__":
    print(datetime.now())
    process()
    print(datetime.now())
