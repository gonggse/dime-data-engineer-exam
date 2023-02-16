import sqlite3

class dbInit :
    def __init__(self) :
        try:
            conn = sqlite3.connect("data.db")    
        except Exception as e:
            print(e)

        self.conn = conn
    
    def insert_stock_dividend(self, data:tuple) -> None :
        """
        Insert stock dividend data to db by iterating response data from fcm API
        data(tuple) : 1 tuple = 1 row
        """

        cursor = self.conn.cursor()
        sql = """INSERT INTO stock_dividend (date, label, adjDividend, 
                                            dividend, recordDate, paymentDate, 
                                            declarationDate)
                 VALUES (?,?,?,?,?,?,?)"""
        cursor.execute(sql, data)
        self.conn.commit()

    def insert_delisted_companies(self, data:tuple) -> None :
        """
        Insert delisted companies data to db by iterating response data from fcm API
        data(tuple) : 1 tuple = 1 row
        """

        cursor = self.conn.cursor()
        sql = """INSERT INTO stock_dividend (symbol, campanyName, exchange, 
                                            ipoDate, delistedDate)
                 VALUES (?,?,?,?,?)"""
        cursor.execute(sql, data)
        self.conn.commit()
    
    def close_conn(self) :
        self.conn.close()
