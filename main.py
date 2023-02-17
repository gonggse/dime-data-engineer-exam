from utils.fmp_driver import initfmp
from utils.db_driver import dbInit

if __name__ == "__main__" :
    # Init database driver the database file (data.db) will be automatically created
    db = dbInit()

    # Create delisted companies table
    with open("./sql/delisted_companies_create.sql") as f :
        delisted_companies_create_sql = f.read()
    db.add_table(delisted_companies_create_sql)

    # Create historical devidends table
    with open("./sql/historical_dividends_create.sql") as f :
        historical_dividends_create_sql = f.read()
    db.add_table(historical_dividends_create_sql)

    # Init fmp connection driver
    fmp = initfmp()
    
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

    # Close db
    db.conn.close()
    


    