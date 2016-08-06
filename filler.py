# coding: utf-8
from itertools import *
from more_itertools import *
from datetime import datetime, timedelta
import time
import numpy as np
import matplotlib.dates as pltd








def fill(li,delta):
	'''
	引数:
		li:リスト
		delta:int
	戻り値：編集を加えた、引数と同じリスト
	'''
	for two in list(pairwise(li)):   #liの中身を2つずつにわける
		print(two)
		if two[-1]-two[0]>delta:   #抜き出したタプルの要素の差がdelta上であれば
			if type(two[0])==datetime:
				for i in pltd.drange(two[0]+delta,two[-1],delta):
					li.insert(li.index(two[-1]),pltd.num2date(i))   #タプルの要素間の場所にdeltaずつ増やした値を入れる
					# print('insert',pltd.num2date(i))
					yield pltd.num2date(i)
			else :
				for i in range(two[0]+delta,two[-1],delta):
					li.insert(li.index(two[-1]),i)   #タプルの要素間の場所にdeltaずつ増やした値を入れる
					# print('insert',i)
					yield i
		# else:print('OK!')
	# return li




'''TEST
'''
s=datetime(2016,5,10,12,38,12)
se=datetime(2016,5,10,12,58,1)
e=datetime(2016,5,10,13,3,24)

print(s)
print(se)
print(e)
print('_'*20)
# li=[[1,50],[0,8,10,16],[1,5,9,11,14,15][s,e]]
li=[s,se,e]
for i in fill(li,timedelta(minutes=5)):
	print('insert',i.strftime('%Y%m%d_%H%M%S'))


#実行結果
# 2016-05-10 12:38:12
# 2016-05-10 12:58:01
# 2016-05-10 13:03:24
# ____________________
# (datetime.datetime(2016, 5, 10, 12, 38, 12), datetime.datetime(2016, 5, 10, 12, 58, 1))
# insert 20160510_124312
# insert 20160510_124812
# insert 20160510_125312
# (datetime.datetime(2016, 5, 10, 12, 58, 1), datetime.datetime(2016, 5, 10, 13, 3, 24))
# insert 20160510_130301








'''
__以下は自作drange__________________________
せっかくmatplotlib.datesでdrange用意されているんだからそっちを使おう
'''




def datetime_to_epoch(d):
	return int(time.mktime(d.timetuple()))

def epoch_to_datetime(epoch):
	return datetime(*time.localtime(epoch)[:6])

def drange(end_time,start_time=epoch_to_datetime(0),step_time=timedelta(days=1)):
	'''
	__INTRODUCTION__
	start_timeからend_timeまでの日時をイテレートするジェネレータ


	__USAGE__

	```python:example
	start=datetime(2016,2,24,14,38,16)
	end=datetime(2016,3,4,14,38,17)
	step=timedelta(days=2)

	for i in drange(start,end,step):
		print(i)

	# --result--
	# 2016-02-24 14:38:16
	# 2016-02-26 14:38:16
	# 2016-02-28 14:38:16
	# 2016-03-01 14:38:16   # ←うるう年なので2/29が間に入っている
	# 2016-03-03 14:38:16
	```

	* python バージョン2.7移行に対応
	* 引数は最低2つ、オプション1つ
		* start_time:rangeで生成する最初の日時(datetime型)
		* end_time:rangeで生成する最後の日時(datetime型)
		* [オプション]step_time:rangeで生成する日時の間隔(timedelta型)
			* デフォルト値は1日間隔
			* 小数対応
				* hours=10.5←10時間30分ずつ増加)
			負の実数対応
				* hours=-1←1時間ずつ戻す。
				* ただし、start_timeよりend_timeが早い時間でないと何も返さない)
	* 戻り値はイテレータ(datetime型)


	__ACTION__

	1. start_time, end_timeをエポック時間に直す
	2. step_timeをtotal_seconds()で秒に直す
	3. np.arange()関数でエポック秒のイテレータを返し、datetime型に直してイールドする
	'''
	for i in np.arange(datetime_to_epoch(start_time),datetime_to_epoch(end_time),step_time.total_seconds()):
		yield epoch_to_datetime(i)


'''
TEST
e=datetime(1971,1,1)
s=datetime(1972,1,1)

for i in drange(s,e):
	print(i)
'''