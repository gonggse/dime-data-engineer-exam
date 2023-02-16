CREATE TABLE delisted_companies (
	symbol DATE PRIMARY KEY,
	companyName STRING,
	exchange STRING,
	ipoDate DATE,
    delistedDate DATE
)