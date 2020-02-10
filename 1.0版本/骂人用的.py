import requests
import os
class Fuck:
	def __init__(self,type):
		self.headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400'
		}
		if type=='骂人':
			self.url='https://nmsl.shadiao.app/api.php'
		else:
			self.url='https://chp.shadiao.app/api.php'
		requests.packages.urllib3.disable_warnings()#忽视ssl警告
	def run(self):
		return requests.get(url=self.url,headers=self.headers,verify=False).text#取消验证ssl
if __name__=="__main__":
	print(Fuck().run())
	os.system('pause')