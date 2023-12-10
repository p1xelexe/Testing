import sqlite3
import pytest
import os

DB_NAME = "mydatabase.db"
BUYER_NAME = "John Doe"
KENNEL_NAME = "New Kennel Name"
DOG_NAME = "Dog's name"

def create_tables(conn):
    cursor = conn.cursor()

    # Создание таблицы Покупатель
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Buyer (
            id INTEGER PRIMARY KEY,
            name TEXT,
            dog_id INTEGER,
            FOREIGN KEY (dog_id) REFERENCES Dog(id)
        )
    """)

    # Создание таблицы Питомник
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Kennel (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)

    # Создание таблицы Собака
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Dog (
            id INTEGER PRIMARY KEY,
            name TEXT,
            kennel_id INTEGER,
            buyer_id INTEGER,
            FOREIGN KEY (kennel_id) REFERENCES Kennel(id),
            FOREIGN KEY (buyer_id) REFERENCES Buyer(id)
        )
    """)

    conn.commit()

def db_connection():
    db_exists = os.path.isfile(DB_NAME)
    conn = sqlite3.connect(DB_NAME)

    if not db_exists:
        create_tables(conn)

    return conn



@pytest.fixture(scope='session')
def start_db():
    connection = db_connection()
    print('Initializing Database')
    yield connection
    connection.close()
    print('Finalizing Database')



def test_db_connection(start_db):
    # Ваш тест с использованием подключения к базе данных
    cursor = start_db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Проверка, что таблицы созданы
    assert ("Buyer",) in tables
    assert ("Kennel",) in tables
    assert ("Dog",) in tables


# Тесты по Insert, Select, Update, Delete 
@pytest.fixture(scope='function')
def setup_database():
    conn = sqlite3.connect(DB_NAME)
    create_tables(conn)
    yield conn
    conn.close()


def test_insert_operation(setup_database):
    cursor = setup_database.cursor()
    cursor.execute("INSERT INTO Buyer (name, dog_id) VALUES (?, ?)", (BUYER_NAME, 1))
    cursor.execute("INSERT INTO Kennel (name) VALUES (?)", (KENNEL_NAME,))
    cursor.execute("INSERT INTO Dog (name, kennel_id, buyer_id) VALUES (?, ?, ?)", (DOG_NAME, 1, None))
    cursor.execute("SELECT * FROM Buyer WHERE name=?", (BUYER_NAME,))
    
    setup_database.commit() # сохраним
    
    result = cursor.fetchone()
    
    assert result is not None
    assert result[1] == "John Doe"
    



def test_select_operation(setup_database):
    cursor = setup_database.cursor()
    cursor.execute("SELECT * FROM Dog")
    result = cursor.fetchall()
    
    assert len(result) > 0



def test_update_operation(setup_database):
    cursor = setup_database.cursor()
    cursor.execute("UPDATE Buyer SET name=? WHERE id=?", ("New Buyer Name", 1))
    cursor.execute("SELECT name FROM Buyer WHERE id=?", (1,))
    result = cursor.fetchone()
    assert result is not None


def test_delete_operation(setup_database):
    cursor = setup_database.cursor()
    cursor.execute("DELETE FROM Buyer WHERE name=?", (BUYER_NAME,))
    cursor.execute("SELECT * FROM Buyer WHERE name=?", (BUYER_NAME,))

    result = cursor.fetchone() 
    assert result is None

    
    cursor.execute("DELETE FROM Dog WHERE name=?", (DOG_NAME,))
    cursor.execute("SELECT * FROM Dog WHERE name=?", (DOG_NAME,))

    result = cursor.fetchone() 
    assert result is None

    cursor.execute("DELETE FROM Kennel WHERE name=?", (KENNEL_NAME,))
    cursor.execute("SELECT * FROM Kennel WHERE name=?", (KENNEL_NAME,))

    setup_database.commit() # сохраним

    result = cursor.fetchone() 
    assert result is None

# сделать процедуры для того чтобы покупатель мог забрать питомца с питомника
# убрать id с питомника и передать покупателю

# проверить связи и ограничений по заданию  по заданию