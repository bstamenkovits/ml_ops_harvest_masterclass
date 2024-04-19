import sqlite3

with sqlite3.connect('data/movielens.db') as conn:
    cursor = conn.cursor()
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # tables = cursor.fetchall()
    # for table in tables:
    #     print(table[0])

    cursor.execute("SELECT user_id FROM users;")
    movies = cursor.fetchall()
    for movie in movies:
        print(movie[0])

    

    

    # cursor.execute("PRAGMA table_info(ratings);")
    # columns = cursor.fetchall()
    # for column in columns:
    #     print(column[1])

    # cursor.execute("""
    #     SELECT column_name, data_type, is_nullable, column_default
    #     FROM INFORMATION_SCHEMA.COLUMNS
    #     WHERE table_name = 'ratings';
    # """)
    # schema = cursor.fetchall()
    # print(schema)
    

    

    
    



# Compare this snippet from src/model_api/dataloaders/dataloader.py: