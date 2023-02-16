from utils.fmp_driver import initfmp
from utils.db_driver import dbInit

if __name__ == "__main__" :
    # Init fmp connection driver
    fmp = initfmp()
    # Init db
    db = dbInit()
    
    #Get Historical-Dividends Data
    historical_diviends = {
        "api_path": "historical-price-full/stock_dividend/AAPL?"
    }
    res = fmp.get_data(historical_diviends['api_path'])
    
    for row in res['historical'] :
        data = tuple(row.values())
        db.insert_historical_dividend(data)
        print("INSERTED: ", data)

    #Get Delisted Companies Data
    delisted_companies = {
        "api_path": "delisted-companies?page=0&"
    }
    res = fmp.get_data(delisted_companies['api_path'])

    for row in res :
        data = tuple(row.values())
        db.insert_delisted_companies(data)
        print("INSERTED: ", data)

    db.conn.close()

    #####################################################
    # to add more table 
    # # example #

    # sql = "CREATE TABLE test (name STRING PRIMARY KEY)"
    # db.add_table(sql)

    


    