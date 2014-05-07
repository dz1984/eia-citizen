#!/usr/local/bin/python3
#
# 需要使用 Python 3.x 執行
# 
# * 測試狀況
#   * 執行時間 76.23 秒 (測試於 MBA 2012 mid)
#   * 總筆數 1442945
#

import json
import gzip
import time
import sqlite3

# TODO: 自動上 Ronny 的 Dropbox 抓資料

conn = sqlite3.connect('database.sqlite')
conn.execute('DELETE FROM corps')
conn.commit()

insert_cnt = 0;
insert_batch = 50000;

beg_time = time.time()

for i in range(0,10): # 0~9
	filename = '%d0000000.json.gz' % i
	f = gzip.open(filename,'rb')

	ln = f.readline().decode('utf-8')
	while ln!='':
		comma_pos = ln.index(',')
		co_id       = ln[0:comma_pos]
		co_infojson = ln[comma_pos+1:]
		info = json.loads(co_infojson)
		ln = f.readline().decode('utf-8')

		# 資料差異性處理
		co_name = ''
		for k in ['公司名稱','分公司名稱','商業名稱']:
			if k in info: co_name = info[k]

		# 外資企業會有兩個名字 ['中文名','英文名']
		# 陸資企業會有討厭的結構 [['中文名','(在臺灣地區公司名稱)'],['中文名','(在大陸地區公司名稱)']]
		if type(co_name) is list:
			if type(co_name[0]) is str:
				co_name = co_name[0]
			else:
				if co_name[0][1] == '在臺灣地區公司名稱':
					co_name = co_name[0][0]
				else:
					co_name = co_name[1][0]

		if co_name != '':
			# 寫入 SQLite 3
			try:
				conn.execute('INSERT INTO corps(id,name) VALUES(?,?)',(co_id,co_name))
				insert_cnt = insert_cnt + 1

				# 分批 commit 避免資料庫 lock
				if insert_cnt%insert_batch==0:
					conn.commit()
					elapsed = time.time() - beg_time
					print('完成 %s 筆, 耗時 %.2f 秒' % (insert_cnt, elapsed))
			except sqlite3.InterfaceError as ex:
				print('%s 寫入失敗: %s (%s)' % (co_id,co_name,ex))
				print(info)
		else:
			print('%s 沒有公司名稱' % co_id)

	# end while
	f.close();

# endfor

if insert_cnt%insert_batch!=0:
	conn.commit()
	elapsed = time.time() - beg_time
	print('完成 %s 筆, 耗時 %.2f 秒' % (insert_cnt, elapsed))

conn.close()
