-- 環評書件資料庫
CREATE TABLE docs (
	id VARCHAR(20),                                   -- 文號
	developer VARCHAR(8) NOT NULL DEFAULT '00000000', -- 開發單位統編
	lat DOUBLE NOT NULL DEFAULT 25.038,               -- 緯度 (預設座標暫定台北市議會)
	lng DOUBLE NOT NULL DEFAULT 121.562,              -- 經度
	impact TEXT NOT NULL DEFAULT '[]',                -- 影響
	file VARCHAR(100) NOT NULL,                       -- 檔案
	PRIMARY KEY (id)
);

-- 公司資料庫 (僅限 '核准設立')
-- 資料由 gen_corps.py 產生
-- TODO: 最好再加個資本額有利排序
CREATE TABLE corps (
	id CHAR(8),
	name VARCHAR(50),
	PRIMARY KEY (id)
);
CREATE INDEX corps_idx_01 ON corps.name;

-- 測試資料，嶺東科技大學
INSERT INTO docs(id,file) VALUES('1030393A','1030393A.pdf');

-- 測試結果
SELECT * FROM docs;
