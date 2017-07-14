 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    shengxiao_1 = request.form['shengxiao1']
    shengxiao_2 = request.form['shengxiao2']
    url = 'http://api.avatardata.cn/ShengXiaoPeiDui/Lookup?'
    url_2='key=b27767d0aecb4ed7b70333b213a24464&shengxiao1='+shengxiao_1+'&shengxiao2='+shengxiao_2
    url_3= url+url_2
    r=requests.get(url_3)
    gg=r.text
    gga=eval(gg)
    results_001=gga[ "result"]["shengxiao1"]
    results_002=gga[ "result"]["shengxiao2"]
    results_003=gga[ "result"]["content1"]
    results_004=gga[ "result"]["content2"]

    return render_template('C_results.html',
                           the_shengxiao1 = results_001,
                           the_shengxiao2 = results_002,
                           the_title = '欢迎来到一C组生肖匹配屋！',
                           the_content1 = results_003,
                           the_content2 = results_004,
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('C_entry.html',
                           the_title='欢迎来到一C组生肖匹配屋！')



if __name__ == '__main__':
    app.run(debug=True)
