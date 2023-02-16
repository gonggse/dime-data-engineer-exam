CREATE TABLE stock_dividend (
	date DATE PRIMARY KEY,
	label STRING,
	adjDividend float64,
	dividend float64 ,
	recordDate DATE,
    paymentDate DATE,
    declarationDate DATE
)