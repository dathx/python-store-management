import pyodbc


class Database:
    def __init__(self, drive='SQL Server', server='localhost', database='', username='', password=''):
        self.drive = drive
        self.server = server
        self.database = database
        self.username = username
        self.password = password

        # creating database connection
        connection_string = (
            f"DRIVER={self.drive};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password};"
        )
        self.con = pyodbc.connect(connection_string)
        self.cur = self.con.cursor()

    def login(self, username, password):
        sql_select_query = "SELECT * FROM NHANVIEN WHERE MANV=? AND MATKHAU=?"
        self.cur.execute(sql_select_query, (username, password))
        result = self.cur.fetchall()
        print(result)
        return result
