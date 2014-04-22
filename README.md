eia-citizen
===========

環境影響評估公民版

原始網站 http://eiareport.epa.gov.tw/EIAWEB/Main.aspx?func=00

### 目錄結構 ###
* /data - 流程圖、文件、資料庫
* /web - 查詢系統 Web 端程式，以 Python Pyramid Framework 開發
* /tools - 工具程式 (例如: 資料蒐集器)

### Web 環境建置 ###
```sh
virtualenv eia-citizen
cd eia-citizen/bin
./pip install pyramid
```
