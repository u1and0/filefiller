# coding: utf-8
version='filefiller.py ver3.2'
'''

__UPDATE3.2__
外部ファイルから呼び出せるようにMAINも関数化


__UPDATE3.1__
一番最後にプリントしているdatetimeObjectはディレクトリ上のファイルをgrepしたものではないので
再度ファイル数をgrepする
↓
grepする部分を関数化する


__UPDATE3.0__
yieldでファイル名吐き出し
そのたびにmakefile


__UPDATE2.0__
makefileの機能追加


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
makeMiddlePoint()が不完全
	最後から2番目以前のデータを2以上消したときに288ファイルに埋めてくれない
	for文の繰り返しがいけないと思う
	while文にすべきか
'''


import numpy as np
import glob
from itertools import *
from more_itertools import *
from datetime import datetime, timedelta
import time
import matplotlib.dates as pltd




def grepfile(directory,extention):
	fullpath=glob.glob(directory+'*'+extention)   #ファイル名をリストに格納

	filename_without_extention=[i[len(directory):-1*len(extention)] for i in fullpath]   #ファイルベースネーム

	datetimeObject=[datetime.strptime(i,'%Y%m%d_%H%M%S') for i in filename_without_extention]   #要素がdatetime形式のリスト作成

	return datetimeObject


def makefile(fullpath):
	with open(fullpath,mode='w') as f:
		c='# <This is DUMMY DATA made by %s>\n'% version
		for i in range(1001):
			c+=str(i).rjust(6)+('-1000.00'.rjust(11))*3+'\n'
		c+='# <eof>\n'
		f.write(c)



# def chunks(l, n):
# 	'''
# 	l:リスト
# 	n:数字
# 	lからnずつgenerate
# 	'''
# 	for i in range(len(l)):
# 		yield l[i:i + n]

# '''chunks TEST
# ll=[1,5,23,6,3,6,7]
# print(list(chunks(ll,2)))
# # Excute Result
# # [[1, 5], [5, 23], [23, 6], [6, 3], [3, 6], [6, 7], [7]]
# '''


# def makeMiddlePoint(li,delta):
# 	'''
# 	引数:
# 		li:リスト
# 		delta:int
# 	戻り値：編集を加えた、引数と同じリスト
# 	'''
# 	for two in list(pairwise(li)):   #liの中身を2つずつにわける
# 		print(two)
# 		if two[-1]-two[0]>delta+timedelta:   #抜き出したタプルの要素の差がdelta上であれば
# 			if type(two[0])==datetime:
# 				for i in pltd.drange(two[0]+delta,two[-1],delta):
# 					li.insert(li.index(two[-1]),pltd.num2date(i))   #タプルの要素間の場所にdeltaずつ増やした値を入れる
# 					# print('insert',pltd.num2date(i))
# 					yield pltd.num2date(i)
# 			else :
# 				for i in range(two[0]+delta,two[-1],delta):
# 					li.insert(li.index(two[-1]),i)   #タプルの要素間の場所にdeltaずつ増やした値を入れる
# 					# print('insert',i)
# 					yield i






def makeMiddlePoint(li,delta):
	'''
	引数:
		li:リスト
		delta:datetime
	戻り値：twoの間に入れる値をyield
	'''
	for two in list(pairwise(li)):   #liの中身を2つずつにわける
		if two[-1]-two[0]>=delta +timedelta(minutes=1):   #抜き出したタプルの要素の差がdelta上であれば
			print('\nLack between %s and %s'% (two[0],two[1]))
			print('Substract',abs(two[0]-two[1]))
			for i in pltd.drange(two[0]+delta,two[-1],delta):
				li.insert(li.index(two[-1]),pltd.num2date(i))   #タプルの要素間の場所にdeltaずつ増やした値を入れる
				print('insert',pltd.num2date(i))

				print(li)

				yield pltd.num2date(i).strftime('%Y%m%d_%H%M%S')
	print('\nThere is No point to insert')
	print('makeMiddlePoint END\n')




def makeStartPoint(li):
	'''始点要素の作製'''
	while True :
		start=li[0]   #始点を探す
		if start.hour==0 and 0<=start.minute<5:   #始点の条件クリアでループ終了
			print('\nFirst element is',start)
			print('makeStartPoint END\n')
			break
		li.insert(0,start-timedelta(minutes=5))   #リストの最初に5分前の値をリストに格納
		print('Inserted',li[0])
		yield li[0].strftime('%Y%m%d_%H%M%S')


def makeStopPoint(li):
	'''終点要素の作製'''
	while True :
		stop=li[-1]   #終点を探す
		if stop.hour==23 and 55<=stop.minute<60:   #終点の条件クリアでループ終了
			print('\nLast element is',stop)
			print('makeStopPoint END\n')
			break
		li.append(stop+timedelta(minutes=5))   #リストの最初に5分前の値をリストに格納
		print('Appended',li[-1])
		yield li[-1].strftime('%Y%m%d_%H%M%S')




# __MAIN__________________________

def filefiller(directory,extention='.txt'):
	datetimeObject=grepfile(directory,extention)
	print('Before:Number of Files is',len(datetimeObject))   #Check number of files
	print('-'*20)
	for i in makeMiddlePoint(datetimeObject,timedelta(minutes=5)):makefile(directory+i+extention)
	print('-'*20)
	for i in makeStartPoint(datetimeObject):makefile(directory+i+extention)
	print('-'*20)
	for i in makeStopPoint(datetimeObject):makefile(directory+i+extention)
	print('-'*20)
	print('After:Number of Files is',len(grepfile(directory,extention)))   #Check number of files





'''
TEST
'''
filefiller('C:/home/gnuplot/SAout/160717/')

# '''
# TEST2
# '''
# directory='C:/home/gnuplot/SAout/160717/'
# extention='.txt'
# datetimeObject=grepfile(directory,extention)
# print('Before',len(datetimeObject))

# function=[
# 					'makeMiddlePoint(datetimeObject,timedelta(minutes=5))',
# 					'makeStartPoint()',
# 					'makeStopPoint()']
# for func in function:
# 	for filename in eval(func):
# 		pass
# 		# makefile(directory+filename+extention)

# # datetimeObject=grepfile(directory,extention)
# print('After',len(datetimeObject))



