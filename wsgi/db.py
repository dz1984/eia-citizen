import os,sqlite3

def dict_factory(cursor, row):  
    d = {}  
    for idx, col in enumerate(cursor.description):  
        d[col[0]] = row[idx]  
    return d 

con = sqlite3.connect(os.path.join(os.environ["OPENSHIFT_DATA_DIR"]+'database.sqlite'),check_same_thread=False)
con.row_factory = dict_factory
cur = con.cursor()

'''
docId = '1030393A'
cur.execute("SELECT * FROM docs WHERE id=?",(docId,))
for row in cur:
    print(row)
'''
