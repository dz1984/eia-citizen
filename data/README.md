## 工具程式 ##

### initdb.sh ###
產生 database.sqlite 結構，並且把舊的改名為 database.sqlite.old

### showdb.sh ###
把 database.sqlite 裡面的部分資料顯示出來

### gen_corps.py ###
自動產生統編 > 公司名稱的對照表資料，<br/>
執行前需要先取得 Ronny 的 00000000.json.gz ~ 90000000.json.gz，<br/>
此工具需要用 Python 3.x 執行
