環境影響評估公民版
----

#### 相關連結 ####
* 官網：[環評書件查詢系統](http://eiareport.epa.gov.tw/EIAWEB/Main.aspx?func=00)
* Hackpad：[環境影響評估公民版--從環評看土地變更](https://g0v.hackpad.com/--P8EaNXkcT11)
* 資料來源：[台灣公司資料](http://company.g0v.ronny.tw/)

#### 目錄結構 ####
* /      - Web 程式，以 Bottle Framework 開發
* /css   - CSS
* /js    - Javascript 檔案
* /views - Jinja2 版型
* /data  - 流程圖、文件、資料庫

#### 執行方式 ####
```sh
virtualenv pyenv # 先製作一份 virrualenv，確保 Python 環境衛生
cd pyenv
bin/pip install jinja2
git clone git@github.com:g0v/eia-citizen.git
cd eia-citizen
./main.py
```
