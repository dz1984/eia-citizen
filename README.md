環境影響評估公民版
----

#### 相關連結 ####

* 官網：[環評書件查詢系統](http://eiareport.epa.gov.tw/EIAWEB/Main.aspx?func=00)
* Hackpad：[環境影響評估公民版--從環評看土地變更](https://g0v.hackpad.com/--P8EaNXkcT11)
* 資料來源：[台灣公司資料](http://company.g0v.ronny.tw/)

#### 目錄結構 ####

* /libs   - 程式庫(Bottle Framework)
* /views  - Jinja2 版型
* /routes - Web程式
* /data   - 流程圖、文件、資料庫
* /admin  - 管理工具

#### 產生資料庫 ####

```sh
$ data/initdb.sh
```

#### 執行方式 ####

```sh
$ virtualenv pyenv # 先製作一份 virrualenv，確保 Python 環境衛生
$ cd pyenv
$ bin/pip install jinja2
$ git clone git@github.com:g0v/eia-citizen.git
$ cd eia-citizen
$ ./main.py
```
