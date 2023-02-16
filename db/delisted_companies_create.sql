CREATE TABLE delisted_companies (
	symbol STRING PRIMARY KEY,
	company STRING,
	exchange STRING,
	ipoDate DATE,
    delistedDate DATE
)