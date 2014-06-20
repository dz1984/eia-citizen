import csv, sqlite3

CSV_FOLDER = 'csv'
if __name__ == '__main__':
    conn = sqlite3.connect("database.sqlite")
    conn.text_factory = str
    curs = conn.cursor()

    # import lists dataset
    with open("%s/%s" % (CSV_FOLDER,'lists.csv')) as f:
        reader = csv.DictReader(f)

        # insert data to sqlite db
        for row in reader:
            curs.execute("INSERT INTO lists (Id,Agency, Name, DocType,Taker,Status, Notes) VALUES(?,?,?,?,?,?,?);",[row['Id'],row['Agency'],row['Name'],row['DocType'],row['Taker'],row['Status'],row['Notes']])
            conn.commit()

    details_fields = ['Id', 'DocType', 'DevUnit', 'Region', 'DevCategory','Area','Size', 'Unit', 'Taker', 'Agency', 'SendDate','Status','ExamineDate', 'ExamineStatus', 'CommitteeDate', 'Notes']

    # import details dataset
    with open("%s/%s" % (CSV_FOLDER,'details.csv')) as f:
        reader = csv.DictReader(f)

        for row in reader:
            curs.execute("INSERT INTO details (Id, DocType,DevUnit,Region,DevCategory, Area, Size, Unit, Taker, Agency, SendDate,Status,ExamineDate, ExamineStatus, CommitteeDate, Notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",[row[fieldName] for fieldName in details_fields])
            conn.commit()

    pass
