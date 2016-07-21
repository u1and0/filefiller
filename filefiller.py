# coding: utf-8
'''
## filefiller.py ver1.0

__UPDATE1.0__
First commit

__USAGE__
directoryにはtxtファイルが詰まったディレクトリ名(最後に/必須)
extentionには拡張子
以上を入れてbuild

__INTRODUCTION__
あるディレクトリ内のtxtファイル(ファイル名=yyyymmdd_HHMMSS.txt)が00時00分～00時04分に始まり、23時55分～23時59分に終わるようにファイルを追加していく

__ACTION__
変数セット
datetimeObjectというリスト作成
datetimeObjectが5分間隔に並ぶように以下を行う
	makeStartPoint()
	makeMiddlePoint()
	makeStopPoint()
__TODO__
None
'''


import numpy as np
import datetime
d=datetime
import glob


directory='C:/home/gnuplot/SAout/160717/'
extention='.txt'


# __MAKE LIST__________________________
fullpath=glob.glob(directory+'*'+extention)   #ファイル名をリストに格納

filename_without_extention=[i[len(directory):-1*len(extention)] for i in fullpath]   #ファイルベースネーム

datetimeObject=[d.datetime.strptime(i,'%Y%m%d_%H%M%S') for i in filename_without_extention]   #要素がdatetime形式のリスト作成

datetimeObjectHourmin=[int(i.strftime('%H%M')) for i in datetimeObject]   #要素が"時間と分"のリスト作成



def chunks(l, n):
	'''
	l:リスト
	n:数字
	lからnずつgenerate
	'''
	for i in range(len(l)):
		yield l[i:i + n]

'''chunks TEST
ll=[1,5,23,6,3,6,7]
print(list(chunks(ll,2)))
# Excute Result
# [[1, 5], [5, 23], [23, 6], [6, 3], [3, 6], [6, 7], [7]]
'''




def makeMiddlePoint():
	'''リスト内2個組で差分が6分未満になるように要素を作製'''
	for two in chunks(datetimeObject,2):   #リストの2組ずつgenerate
		if two[-1]-two[0]>=d.timedelta(minutes=6):
			print(two[-1],two[0],two[-1]-two[0])
			where=datetimeObject.index(two[-1])
			time=two[0]+d.timedelta(minutes=5)
			datetimeObject.insert(where,time)   #調べた2くくりの要素間に+5分した要素を追加
			print('Inserted',time,'next to',two[0])
		# elif two[-1]-two[0]<d.timedelta(minutes=4):break
	print('\nInsert element End\n')





def makeStartPoint():
	'''始点要素の作製'''
	while True :
		start=datetimeObject[0]   #始点を探す
		if start.hour==0 and 0<=start.minute<5:   #始点の条件クリアでループ終了
			print('\nFirst element is',start)
			print('Insert start END\n')
			break
		datetimeObject.insert(0,start-d.timedelta(minutes=5))   #リストの最初に5分前の値をリストに格納
		print('Inserted',datetimeObject[0])


def makeStopPoint():
	'''終点要素の作製'''
	while True :
		stop=datetimeObject[-1]   #始点を探す
		if stop.hour==23 and 55<=stop.minute<60:   #始点の条件クリアでループ終了
			print('\nLast element is',stop)
			print('insert stop END\n')
			break
		datetimeObject.append(stop+d.timedelta(minutes=5))   #リストの最初に5分前の値をリストに格納
		print('Appended',datetimeObject[-1])





# __MAIN__________________________
print('Before',datetimeObject,len(datetimeObject))
makeStartPoint()
makeMiddlePoint()
makeStopPoint()
print('After',datetimeObject,len(datetimeObject))










