-- 環評書件資料庫
CREATE TABLE docs (
    id          VARCHAR(20),                                        -- 案號
    developer   VARCHAR(8) NOT NULL DEFAULT '00000000',             -- 開發單位統編
    lat         DOUBLE NOT NULL DEFAULT 25.038,                     -- 緯度 (預設座標暫定台北市議會)
    lng         DOUBLE NOT NULL DEFAULT 121.562,                    -- 經度
    impact      TEXT NOT NULL DEFAULT '[]',                         -- 影響
    file        VARCHAR(100) NOT NULL DEFAULT '',                   -- 檔案
    PRIMARY KEY (id)
);

-- 環評書件一覽
CREATE TABLE lists (
    id          VARCHAR(20),                -- 案號
    agency      VARCHAR(100),               -- 環評機關
    name        VARCHAR(100),               -- 名稱
    doctype     VARCHAR(80),                -- 類別
    taker       VARCHAR(30),                -- 承辦人
    status      VARCHAR(50),                -- 審查進度
    notes       VARCHAR(150)                -- 說明
    PRIMARY KEY (id)
);

-- 環評書件明細
CREATE TABLE details (
    id              VARCHAR(20),            -- 案號
    doctype         VARCHAR(80),            -- 書件類別
    devunit         VARCHAR(80),            -- 開發單位名稱
    region          VARCHAR(50),            -- 基地行政區
    devcategory     VARCHAR(50),            -- 開發計畫類別
    area            DOUBLE,                 -- 基地面積
    size            DOUBLE,                 -- 開發規模
    unit            VARCHAR(30),            -- 開發規模單位
    taker           VARCHAR(30),            -- 承辨人
    agency          VARCHAR(100),           -- 目的事業主管機關
    senddate        VARCHAR(10),            -- 繳費日期
    status          VARCHAR(50),            -- 處理情形
    examinedate     VARCHAR(10),            -- 初審會日期
    examinestatus   VARCHAR(30),            -- 審查結論別
    committeedate   VARCHAR(10),            -- 委員會日期
    notes           VARCHAR(150)            -- 備註
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
