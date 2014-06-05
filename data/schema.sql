-- 環評書件資料庫
CREATE TABLE docs (
    id          VARCHAR(20),                                        -- 案號
    developer   VARCHAR(8) NOT NULL DEFAULT '00000000',             -- 開發單位統編
    lat         DOUBLE NOT NULL DEFAULT 25.038,                     -- 緯度 (預設座標暫定台北市議會)
    lng         DOUBLE NOT NULL DEFAULT 121.562,                    -- 經度
    impact      TEXT NOT NULL DEFAULT '[]',                         -- 影響
    file        VARCHAR(100) NOT NULL DEFAULT '',                   -- 檔案
    doctype     VARCHAR(50) NOT NULL DEFAULT '',                    -- 書件類別      
    taker       VARCHAR(50) NOT NULL DEFAULT '',                    -- 承辨人
    region      VARCHAR(50) NOT NULL DEFAULT '',                    -- 基地行政發
        -- 初審會日期
        -- 目的事業主管機關
        -- 開發計畫類別
        -- 備註
        -- 繳費日期
        -- 審查結論別
        -- 開發單位名稱
        -- 備註
        -- 繳費日期
        -- 審查結論別
        -- 開發單位名稱
        -- 委員會日期
        -- 開發規模
        -- 處理情形
        -- 基地面積






HCODE,DOCTYP,TAKER,DST,TRIA,DIRORG,DECAL,DSUNT,NOTES,SEDAT,EXTP,DEPN,COMIT,DSIZE,PORCS,DAREA

案號,書件類別,承辨人 ,基地行政區,初審會日期,目的事業主管機關,開發計畫類別,,備註,繳費日期,審查結論別,開發單位名稱,委員會日期,開發規模,處理情形,基地面積

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
