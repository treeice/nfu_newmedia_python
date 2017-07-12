# -*- coding: utf-8 -*- 
#!/usr/bin/env Python

from flask import Flask, render_template, request, escape
import json
import hashlib
import requests
import random

app = Flask(__name__)

import language_data 
import language_data_01 
l = language_data.language_from_to()
l_01 = language_data_01.language_from_to_01()

l_list = [k for k in l.from_to.keys()]
l_list_01 = [k for k in l_01.from_to_01.keys()]

l_dict_order = {k:v for k, v in l.from_to.items()}
l_dict_order_01 = {k:v for k, v in l_01.from_to_01.items()}



@app.route('/translate', methods=['POST'])
def translate() -> 'html':
	translate_q= request.form['words']
	title = '以下是您的结果：'
	key= request.form['my_password']
	translate_appid= request.form['my_id']
	translate_salt=random.randint(0,9999999999)
	translate_q=str(translate_q)
	#下列是语言类型选框的代码
	entry_translate_from= request.form['pick_from_language']
	translate_from=l_dict_order[entry_translate_from]
	entry_translate_to= request.form['pick_to_language']
	translate_to=l_dict_order_01[entry_translate_to]

#拼接签名
	translate_sign=str(translate_appid)+translate_q+str(translate_salt)+str(key)
#为网址的参数中的签名加密md5
	m = hashlib.md5(translate_sign.encode("utf8"))
	translate_sign_md5=m.hexdigest()
#网址参数连接
	url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'  
	url_2 = 'q='+translate_q+'&from='+str(translate_from)+'&to='+str(translate_to)+'&appid='+str(translate_appid)+'&salt='+str(translate_salt)+'&sign='+translate_sign_md5
	url= url_1+url_2
#网页打开  
	r=requests.get(url)
	e=r.text
#json转码
	data = json.loads(e)
#jieguo
	if 'trans_result' in data.keys():
		translate_result=data['trans_result'][0]['dst']
	else: 
		if 'error_code' in data.keys():
			if '54000' in data['error_code']:
				translate_result='请在选框中输入文字'
			elif '52001' in data['error_code']:
				translate_result='请求超时请重试'
			elif '52002' in data['error_code']:
				translate_result='系统错误请重试'  
			elif '54003' in data['error_code']:
				translate_result='请降低您的调用频率'
			elif '58001' in data['error_code']:
				translate_result='不支持该语种的翻译'
			elif '54005' in data['error_code']:
				translate_result='请降低长query的发送频率，3s后再试'
			elif '52003' in data['error_code']:
				translate_result='未授权用户,请检查您的appid是否正确'
			elif '58000' in data['error_code']:
				translate_result='客户端IP,非法检查您填写的IP地址是否正确，可修改您填写的服务器IP地址'
			elif '54004' in data['error_code']:
				translate_result='账户余额不足,请前往管理控制台为账户充值'
			else:
				translate_result='请正确填入密钥'
	return render_template('results.html',
							the_title=title,
							need_words=translate_result,
							translate_from_language=entry_translate_from,
							translate_to_language=entry_translate_to,
							want_words=translate_q,
							)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           enry_language_list = l_list,
						   enry_language_list_01 = l_list_01,
                           the_title='欢迎来到翻译吧')

if __name__ == '__main__':
    app.run(debug=True)
              
