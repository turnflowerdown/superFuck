import sys
from PyQt5.QtWidgets import QMainWindow,QDesktopWidget,QPushButton,QVBoxLayout,QHBoxLayout,QWidget,QRadioButton,QButtonGroup,QLabel
from PyQt5.QtCore import Qt

class MainWindow_style(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('宇宙骂人小工具')
		self.center()
		self.resize(400,200)
		self.show_btn()
		# self.statusBar()#显示状态栏
	def center(self):#设置窗口居中
		box=self.frameGeometry()#获取当前盒子的信息
		window_center=QDesktopWidget().availableGeometry().center()
		box.moveCenter(window_center)
		self.move(box.topLeft())
	def show_btn(self):#设置按钮
		self.btn1=QPushButton('设置字典')#设置字典
		self.btn2=QPushButton('设置发送速度')#设置发送速度
		self.btn3=QRadioButton('网站')#设置发送源
		self.btn4=QRadioButton('字典')#设置发送源
		self.btn5=QPushButton('发送')#开始发送
		self.btn6=QPushButton('骂人')
		hbox=QHBoxLayout()
		hbox1=QHBoxLayout()
		hbox2=QHBoxLayout()
		vbox1=QVBoxLayout()
		vbox2=QVBoxLayout()

		vbox1.addWidget(self.btn1)
		vbox1.addWidget(self.btn2)

		hbox1.addWidget(self.btn3)
		self.btn3.setChecked(True)#设置默认选中
		hbox1.addWidget(self.btn4)
		self.btn4.setEnabled(False)#设置无法选择
		vbox2.addLayout(hbox1)
		
		hbox2.addWidget(QLabel('当前状态:'))
		hbox2.addWidget(self.btn6)
		vbox2.addLayout(hbox2)
		
		vbox2.addWidget(self.btn5)
		hbox.addLayout(vbox1)
		hbox.addStretch()#设置中间的占位控件
		hbox.addLayout(vbox2)
		hbox.setContentsMargins(50,0,50,0)#设置hbox控件的外边距 左上右下
		center_window=QWidget()
		center_window.setLayout(hbox)
		self.setCentralWidget(center_window)

class SetTimeWindow_style(QWidget):
	def __init__(self):
		super().__init__()
		self.center()
		self.btn=[]
		self.btn.append(QRadioButton("0.1s"))
		self.btn.append(QRadioButton("0.5s"))
		self.btn.append(QRadioButton("1s"))
		self.btn.append(QRadioButton("2s"))
		vbox=QVBoxLayout()
		vbox.addWidget(self.btn[0])
		self.btn[0].setChecked(True)
		vbox.addWidget(self.btn[1])
		vbox.addWidget(self.btn[2])
		vbox.addWidget(self.btn[3])
		self.setLayout(vbox)
		self.setWindowTitle('选择发送间隔')
		self.setWindowFlags(Qt.WindowTitleHint|Qt.WindowCloseButtonHint|Qt.WindowStaysOnTopHint)
		self.resize(200,120)
		self.show()
	def center(self):#设置窗口居中
		box=self.frameGeometry()#获取当前盒子的信息
		window_center=QDesktopWidget().availableGeometry().center()
		box.moveCenter(window_center)
		self.move(box.topLeft())