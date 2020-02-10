import sys
from time import sleep
from 样式 import MainWindow_style,SetTimeWindow_style
from 操作 import Loop
from PyQt5.QtWidgets import QFileDialog,QWidget,QMessageBox
from queue import Queue
from threading import Thread
class MainWindow(MainWindow_style):
	def __init__(self):
		super().__init__()
		self.connect()
		self.init()
		self.show()
		self.list=['骂人','彩虹屁','渣男语录','毒鸡汤']
		self.i=0
	
	def init(self):#初始化参数
		self.dirs=None#字典
		self.time=0.1#时间间隔
		self.timewindow=None
		self.loop=None
		self.thread=None
		self.queue=Queue()
	def connect(self):#连接槽
		self.btn1.clicked.connect(self.open_file)
		self.btn2.clicked.connect(self.setTime)
		self.btn3.clicked.connect(self.setType)
		self.btn4.clicked.connect(self.setType1)
		self.btn5.clicked.connect(self.run)
		self.btn6.clicked.connect(self.change)
	
	#以下为槽函数
	def open_file(self):
		filepath,filetype=QFileDialog.getOpenFileName(self,'选择字典',sys.path[0],"文本文件(*.txt);;所有文件(*)")
		if filepath:
			with open(filepath,'r',encoding='utf8') as f:
				self.dirs=f.read().split('\n')
			self.btn4.setEnabled(True)#设置可使用字典发送
	
	def setTime(self):
		self.timewindow=SetTimeWindow(self)
	
	def setType(self):
		self.btn6.setText(self.list[self.i])
		self.btn6.setEnabled(True)
	def setType1(self):
		self.btn6.setText('字典发送')
		self.btn6.setEnabled(False)

	def run(self):
		if self.btn5.text()=='发送':
			self.btn5.setText('停止')
			while self.queue.empty()==False:
				self.queue.get()
			self.btn6.setEnabled(False)
			if self.btn3.isChecked():#网站发送
				self.loop=Loop('网站',self.time,self.queue,self.btn6.text(),self.dirs)
			else:
				self.loop=Loop('字典',self.time,self.queue,self.dirs)
			self.thread=Thread(target=self.loop.run,name='loop_run',args=())
			self.thread.start()
			sleep(0.1)
			if self.thread.is_alive()==False:
				QMessageBox.warning(self,'Message','请检查网络连接',QMessageBox.Yes)
				self.btn5.setText('发送')
				self.btn6.setEnabled(True)
		else:
			self.btn5.setText('发送')
			self.btn6.setEnabled(True)
			self.queue.put(1)
	
	def change(self):
		# if self.btn6.text()=='骂人':
			# self.btn6.setText('夸人')
		# elif self.btn6.text()=='夸人':
			# self.btn6.setText('骂人')
		# else:
			# self.btn6.setText('字典发送')
		self.i=self.i+1
		self.i=self.i%len(self.list)
		self.btn6.setText(self.list[self.i])
	
	def closeEvent(self,event):#重写关闭窗口操作
		#关闭子窗口
		self.queue.put(1)
		if self.timewindow:
			self.timewindow.close()
		
class SetTimeWindow(SetTimeWindow_style):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		self.list=[0.1,0.5,1,2]
		for i in range(0,4):
			if self.btn[i].text()[0:-1]==str(self.parent.time):
				self.btn[i].setChecked(True)
	def closeEvent(self,event):
		for i in range(0,4):
			if self.btn[i].isChecked():
				self.parent.time=self.list[i]
				break