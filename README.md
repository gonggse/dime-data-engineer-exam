# dime-data-engineer-exam
This is the examination for dime's data engineer position

The repo shows the process of getting FMP data and store the data.

**Repository structure**

```
./dime-data-engineer-exam/
│
├── credentials/
│   └── config.json
│
├── sql/
│   ├── delisted_companies_create.sql
│   └── historical_dividends_create.sql
│
├── utils/
│   ├── __init__.py
│   ├── db_driver.py
│   └── fmp_driver.py
│
├── requirements.txt
├── data.db
├── README.md
└── main.py
```

**Table Info**


**historical_dividends**
```
  date DATE PRIMARY KEY,
  label STRING,
  adjDividend float64,
  dividend float64 ,
  recordDate DATE,
  paymentDate DATE,
  declarationDate DATE
```

**delisted_companies**
```
  symbol STRING PRIMARY KEY,
  company STRING,
  exchange STRING,
  ipoDate DATE,
  delistedDate DATE
```



**Short Description**

- ```main.py``` is the main execution file
- ```data.db``` is a sqlite local databasee, the main db, file
- The utils module contains 2 files
  - ```/utils/db_driver.py``` is database handler
  - ```/utils/fmp_driver.py``` is FMP Api handler
- Sql Directory store the create table queries of 2 tables 
  - ```/utils/delisted_companies_create.sql``` creates ```delisted_companies``` table
  - ```/utils/fmp_driver.py``` is FMP Api handler creates ```historical_dividends``` table
- Credentials contains ```credentials/config.json``` stores Apikeys of FMP Api (didnt store as a encrypted key, in vault/secret manager because want to focus the main process part)
