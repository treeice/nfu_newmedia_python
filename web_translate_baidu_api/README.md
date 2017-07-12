web_translate_baidu_api
英文项目名称web_translate_baidu_api，web是网页端，translate意思为翻译，baidu_api意思为调用的是百度翻译平台所提供的数据库。
-------------

		
## 简介 
> **登陆相关账号后，**</br>
> **通过百度翻译平台HTTP接口对外提供多语种互译服务，帮助用户翻译所需的单词或句子。**</br>
> **数据来源为百度翻译平台的api数据库和手动添加的所支持的翻译语言类型的tsv档**</br>
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
> **用户选择输入的源语言的语言类型，交互界面使用到HTML之 select 表单元素，显示的是所选语种的中文名字，其对映值为语言代码，所以代码文件可以用找所需要的语言代码。**</br>
> **用户选择输出的目标语言的语言类型，交互界面使用到HTML之 select 表单元素，显示的是所选语种的中文名字，其对映值为语言代码，所以代码文件可以用找所需要的语言代码。**</br>
> **用户填入的登陆id，交互界面使用到HTML之 input 表单元素中的输入类型：text，获取登陆百度翻译平台的账号，以获取API的使用权**</br>
> **用户填入的登陆密码，交互界面使用到HTML之 input 表单元素中的输入类型：text，获取登陆百度翻译平台的相对应账号的密码，以获取API的使用权**</br>
> **用户填入的需要翻译的内容，交互界面使用到HTML之 input 表单元素中的输入类型：text，代码文件获得所需翻译的文字及其内容**</br>
> **详细见[templates/entry.html](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/templates/entry.html)**</br>




### 输出：
> **用户选择输入的源语言的语言类型**</br>
> **用户选择输出的目标语言的语言类型**</br>
> **用户填入的所需翻译的内容**</br>
> **用户得到翻译的结果**</br>
> **详细见[templates/results.html](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/templates/results.html)**</br> 


### 从输入到输出，本组作品使用了：
#### 资料
> 由于api无翻译语言类型的资料档，
所以手动生成语言类型,的tsv档，
在文件中读入，并做成字典读出相对应的内容。





#### 模块
> -[requests](http://www.python-requests.org/en/master/)</br>
> -[hashlib](https://docs.python.org/2/library/hashlib.html)</br>
> -[json](http://www.runoob.com/json/json-tutorial.html)</br>
> -[random](http://www.runoob.com/python/func-number-random.html)
#### API
> -[github](https://api.github.com/)</br>
> -[百度翻译api](http://api.fanyi.baidu.com/api/trans/product/apidoc)

#### Web App动作描述

> - 以下是web请求前的准备工作

> - 1. 在网页[百度翻译平台](http://api.fanyi.baidu.com/api/trans/product/apidoc)中，手动复制出所有的支持语言列表，保存成两个tsv档，一份是28个源语言的语言类型和一份27个目标语言的语言类型，保存到本地的data文件夹中。分别存在data文件夹中的[data/language_data.tsv](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/data/language_data.tsv)和[data/language_data_01.tsv](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/data/language_data_01.tsv)。

> - 2. 在[language_data.py](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/language_data.py)和[language_data_01.py](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/language_data_01.py)中定义两个类language_from_to ()和language_from_to_01 (),读取[data/language_data.tsv](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/data/language_data.tsv)和[data/language_data_01.tsv](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/data/language_data_01.tsv)两个数据档，并分别把数据返回一个语言类型的字典，建立以语言类型的中文说明为键，相对应的英文简称为值的字典self.from_to和self.from_to_01(见代码self.from_to = {d['language_from']:d['language_to'] for d in list_dict_language}和self.from_to_01 = {d['language_from']:d['language_to'] for d in list_dict_language})

> - 3. 在[translate.py](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/translate.py)中导入两个读取data文件夹中语言列表的类[language_data.py](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/language_data.py)和[language_data_01.py](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/language_data_01.py)，使用自定义函数读取语言类型的字典(见代码l = language_data.language_from_to()和l_01 = language_data_01.language_from_to_01()）并把两个语言类型的字典中的键提取出来，放入[templates/entry.html](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/templates/entry.html)中作为源语言的语言类型和目标语言的语言类型的选择列表(见代码l_list = [k for k in l.from_to.keys()]和l_list_01 = [k for k in l_01.from_to_01.keys()])，并生成两个语言类型的字典(见代码l_dict_order = {k:v for k, v in l.from_to.items()}和l_dict_order_01 = {k:v for k, v in l_01.from_to_01.items()})，把用户选择的源语言语言类型和目标语言的语言类型作为键，用这两个字典读值，得到两个语言类型相对应简称，用于代码文件中来形成调用API的网址。

> - 以下按web 请求（web request） - web 响应 时序说明

> - 後端伺服器启动：执行 translate.py 启动後端伺服器，等待web 请求。启动成功应出现： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

> - 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

> - 後端伺服器web 响应：translate.py 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版templates/entry.html及一个含语言代码及语言名称的字典（见代码 enry_language_list  = l_list）产出的产生《欢迎来到翻译吧！》的HTML页面

> - 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 selsct 表单元素 变数名称(name)为'pick_from_language' ，'pick_to_language'  input 类型(type) 为"text"，变数名称(name)为'my_id'，'my_password','words'使用了HTML的 select 表单元素，详见HTML模版templates/entry.html

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
见[_team_.tsv](https://github.com/treeice/nfu_newmedia_python/blob/master/web_translate_baidu_api/_team_/_team_.tsv)

	
