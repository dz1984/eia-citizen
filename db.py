import sqlite3

def dict_factory(cursor, row):  
    d = {}  
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]  
    return d 

con = sqlite3.connect('data/database.sqlite')
con.row_factory = dict_factory
cur = con.cursor()

'''
docId = '1030393A'
cur.execute("SELECT * FROM docs WHERE id=?",(docId,))
for row in cur:
    print(row)
'''
