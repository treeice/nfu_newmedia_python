web_translate_baidu_api
英文项目名称web_translate_baidu_api，translate意思为翻译，baidu_api意思为调用的是百度翻译平台所提供的数据库。
-------------

		
## 简介 
> **登陆相关账号后，**</br>
> **通过百度翻译平台，帮助用户翻译所需的单词或句子。**</br>
> **数据来源为百度翻译平台的api数据库和手动添加的语言类型的tsv档**</br>
> **支持以下语言类型：**</br>
> - 繁体中文(text)
> - 文言文(text)
> - 粤语(text)
> - 英文(text)
> - 中文(text)
> - 日语(text)
> - 韩语(text)
> - 法语(text)
> - 西班牙语(text)
> - 泰语(text)
> - 阿拉伯语(text)
> - 俄语(text)
> - 葡萄牙语(text)
> - 德语(text)
> - 意大利语(text)
> - 希腊语(text)
> - 荷兰语(text)
> - 波兰语(text)
> - 保加利亚语(text)
> - 爱沙尼亚语(text)
> - 丹麦语(text)
> - 芬兰语(text)
> - 捷克语(text)
> - 罗马尼亚语(text)
> - 斯洛文尼亚语(text)
> - 瑞典语(text)
> - 匈牙利(text)
> - 越南语(text)


### 输入：
> **用户选择输入的语言类型，交互界面使用到HTML之 select 元素，显示的是所选语种的中文名字，其对映值为语言代码，所以代码文件可以用找所需要的语言代码。**</br>
> **用户选择输出的语言类型，交互界面使用到HTML之 select 元素，显示的是所选语种的中文名字，其对映值为语言代码，所以代码文件可以用找所需要的语言代码。**</br>
> **用户填入的登陆id，交互界面使用到HTML5之 input 元素，代码文件可以用找所需要的数据**</br>
> **用户填入的登陆密码，交互界面使用到HTML5之 input 元素，代码文件可以用找所需要的数据**</br>
> **用户填入的需要翻译的内容，交互界面使用到HTML5之 input 元素，代码文件可以用找所需要的数据**</br>
 <input> 元素。


### 输出：
> **用户选择输入的语言类型**</br>
> **用户选择输出的语言类型**</br>
> **用户填入的需要翻译的内容**</br>
> **用户得到翻译的结果**</br>


### 从输入到输出，本组作品使用了：
#### 资料
> 由于api无翻译语言类型的资料档，
所以手动生成语言类型,的tsv档，
在文件中读入，并做成字典读出相对应的内容。




#### 模块
> -[requests](http://www.python-requests.org/en/master/)</br>
> -[hashlib](https://docs.python.org/2/library/hashlib.html)</br>
> -[json](http://www.runoob.com/json/json-tutorial.html)</br>
> -[random](http://www.runoob.com/python/func-number-random.html)</br>
#### API
> -[github](https://api.github.com/)</br>
> -[百度翻译api](http://api.fanyi.baidu.com/api/trans/product/apidoc)

#### Web App动作描述
> - 以下按web 请求（web request） - web 响应 时序说明

> - 後端伺服器启动：执行 translate.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

> - 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

> - 後端伺服器web 响应：translate.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html及一个含语言代码及语言名称的字典（见代码 enry_language_list  = l_list）产出的产生《欢迎来到翻译吧！》的HTML页面

> - 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 selsct 元素 变数名称(name)为'pick_from_language' ，'pick_to_language'  inputut 类型(type) 为"text"，变数名称(name)为'my_id'，'my_password','words'使用了HTML5的 select 元素，详见HTML模版templates/entry.html

> - 前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/translate'，以POST为方法，动作为/translate的web 请求

> - 後端服务器收到用户web 请求，匹配到@app.route('/translate', methods=['POST'])的函数 translate()

> - translate.py 中 def translate() 函数，把用户提交的数据，以flask 模块request.form['words'],['my_id'],['my_password'],['pick_from_language'],['pick_to_language']	取到Web 请求中，HTML表单变数名称words的值，存放在translate_q这Python变数下，再使用flask模块render_template 函数以templates/results.html模版为基础（输出），其中模版中need_words的值，用translate_result这变数之值，其他4项值如此类推。

> - 前端浏览器收到web 响应：模版中templates/results.html 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

### 作者成员：
treeice</br>	
capeucape</br>	
wen-ha</br>
Dahulin</br>
Leeyukyup</br>
kristina579</br>

	
