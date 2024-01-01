import sqlite3

class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect('information.db')
        self._db.row_factory = sqlite3.Row
        self._db.execute(
            'CREATE TABLE IF NOT EXISTS Comp(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), Gender VARCHAR(255), Comment TEXT)')
        self._db.commit()

    def Add(self, name, gender, comment):
        self._db.execute(
            'INSERT INTO Comp (Name, Gender, Comment) VALUES (?,?,?)', (name, gender, comment))
        self._db.commit()
        return 'Your complaint has been submitted.'

    def ListRequest(self):
        cursor = self._db.execute('SELECT * FROM Comp')
        rows = cursor.fetchall()

        result_list = []
        for row in rows:
            result_dict = dict(row)
            result_list.append(result_dict)

        return result_list