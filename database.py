import pyodbc


class Database:
    #  input your database name, user/pass here
    def __init__(self, drive='SQL Server', server='localhost', database='duan1_final', username='sa', password='P@ssword123456'):
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
        return result

    def viewProducts(self):
        self.cur.execute("SELECT * FROM SANPHAM")
        rows = self.cur.fetchall()
        return rows
