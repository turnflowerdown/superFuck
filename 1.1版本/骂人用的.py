import requests
import os
import json
from lxml import etree
class Fuck:
	def __init__(self,type):
		self.headers={
			"method":"GET",
			"path":"/api.php",
			"scheme":"https",
			"accept":"*/*",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"zh-CN,zh;q=0.9",
			"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400",
			"x-requested-with":"XMLHttpRequest",
		}
		self.type=type
		if type=='骂人':
			self.url='https://nmsl.shadiao.app/api.php'
			self.headers["authority"]="nmsl.shadiao.app"
			self.headers["referer"]="https://nmsl.shadiao.app/"
		elif type=='渣男语录':
			self.url='https://api.lovelive.tools/api/SweetNothings/1/Serialization/Json'
			self.headers["path"]="/api/SweetNothings/1/Serialization/Json"
			self.headers["referer"]="https://lovelive.tools/"
			self.headers["origin"]="https://lovelive.tools"
		elif type=='毒鸡汤':
			self.url='https://8zt.cc/'
			self.headers["path"]="/"
		elif type=='彩虹屁':
			self.url='https://chp.shadiao.app/api.php'
			self.headers["authority"]="chp.shadiao.app"
			self.headers["referer"]="https://chp.shadiao.app/"
		requests.packages.urllib3.disable_warnings()#忽视ssl警告
	def run(self):
		if self.type=='渣男语录':
			response=json.loads(requests.get(url=self.url,headers=self.headers).text)["returnObj"][0]
		elif self.type=='毒鸡汤':
			response=requests.get(url=self.url,headers=self.headers).text
			tree=etree.HTML(response.replace("\\n",'').replace("\\",''))
			response=tree.xpath("//span/text()")[0].replace(' ','')
		else:
			response=requests.get(url=self.url,headers=self.headers,verify=False).text#取消验证ssl
		return response
if __name__=="__main__":
	print(Fuck('毒鸡汤').run())
	os.system('pause')