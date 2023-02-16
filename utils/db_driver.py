import sqlite3

class dbInit :
    """
    sqlite driver for collect data to data.db
    """
    
    def __init__(self) :
        try:
            conn = sqlite3.connect("data.db")    
        except Exception as e:
            print(e)

        self.conn = conn
    
    def insert_historical_dividend(self, data:tuple) -> None:
        """
        Insert historical stock dividend data to db by iterating response data from fcm API
        data(tuple) : 1 tuple = 1 row
        """

        cursor = self.conn.cursor()
        sql = """INSERT INTO historical_dividends (date, label, adjDividend, 
                                            dividend, recordDate, paymentDate, 
                                            declarationDate)
                 VALUES (?,?,?,?,?,?,?)"""
        cursor.execute(sql, data)
        self.conn.commit()

    def insert_delisted_companies(self, data:tuple) -> None:
        """
        Insert delisted companies data to db by iterating response data from fcm API
        data(tuple) : 1 tuple = 1 row
        """

        cursor = self.conn.cursor()
        sql = """INSERT INTO delisted_companies (symbol, company, exchange, 
                                            ipoDate, delistedDate)
                 VALUES (?,?,?,?,?)"""
        cursor.execute(sql, data)
        self.conn.commit()
    
    def close_conn(self) -> None:
        self.conn.close()
    
    def add_table(self, sql:str) -> None:
        """
        Add Table to database .db
        sql(str) : Add table by sql syntax "CREATE TABLE"
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)

