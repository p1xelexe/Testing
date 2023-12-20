import aiosqlite

async def create_table():
    async with aiosqlite.connect("mydatabase.db") as db:
        cursor = await db.cursor()
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS mytable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column1 TEXT NOT NULL,
                column2 TEXT NOT NULL
            )
        """)
        await db.commit()

async def add_record_to_database(data):
    await create_table()

    async with aiosqlite.connect("mydatabase.db") as db:
        cursor = await db.cursor()
        await cursor.execute("INSERT INTO mytable (column1, column2) VALUES (?, ?)", data)
        await db.commit()

        return cursor.lastrowid
