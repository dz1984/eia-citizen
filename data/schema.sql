-- 環評書件資料庫
CREATE TABLE docs (
	id VARCHAR(20),
	developer VARCHAR(255),
	lat DOUBLE,
	lng DOUBLE,
	impact TEXT,
	validator INTEGER,
	file VARCHAR(100),
	PRIMARY KEY (id)
);

-- 測試資料，嶺東科技大學
INSERT INTO docs(id,filename) VALUES('1030393A','1030393A.pdf');

-- 測試結果
SELECT * FROM docs;
