 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
import json
import hashlib
import requests
import random

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a', encoding='utf8') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
		

	
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
	translate_q= request.form['words']
	title = '以下是您的结果：'
	key=('me2iM88Qkfps8cQMaOKf')
	translate_appid=20170525000049081
	translate_salt=random.randint(0,9999999999)
 

	translate_sign=str(translate_appid)+str(translate_q)+str(translate_salt)+str(key)#拼接签名
#为网址的参数中的签名加密md5
	m = hashlib.md5(translate_sign.encode("utf8"))
	translate_sign_md5=m.hexdigest()
#网址参数连接
	url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'  
	url_2 = 'q='+translate_q+'&from=auto&to=zh&appid='+str(translate_appid)+'&salt='+str(translate_salt)+'&sign='+translate_sign_md5
	url= url_1+url_2
#网页打开  
	r=requests.get(url)
	e=r.text
#json转码
	data = json.loads(e)
	translate_word=data['trans_result'][0]['dst']	
	return render_template('results.html',
							the_title=title,
							need_words=translate_word)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到翻译吧')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of theX log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
              