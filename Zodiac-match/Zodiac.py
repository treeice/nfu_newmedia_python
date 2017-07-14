# -*- coding: utf-8 -*-
import urllib.request, json

def get_shengxiao(shengxiao_code):
    try:
        with open('shengxiao.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if shengxiao_code in line:
                    shengxiao_name = line.split('=')[1].strip()
        #生肖配对api            
        url = ('http://api.avatardata.cn/ShengXiaoPeiDui/Lookup?key=b27767d0aecb4ed7b70333b213a24464&shengxiao1={name}&shengxiao2={name}'.format(name=shengxiao_name))

        response = urllib.request.urlopen(url)
        shengxiao_html = response.read()
        json_data = json.loads(shengxiao_html)
        
        data = json_data['Avatardata'][0]
        '''
        #配对情况
        shengxiao_brf = data['suggestion']['shengxiao']['brf']
        shengxiao_txt = data['suggestion']['shengxiao']['txt']
        '''
        #生肖1
        shengxiao1 = data['suggestion']['shengxiao1']['brf']
        
        #生肖2
        shengxiao2 = data['suggestion']['shengxiao2']['brf']
        
        #title
        title = data['suggestion']['title']['brf']
        
        #content1
        content1 = data['suggestion']['content1']['brf']
        
        #content2
        content2 = data['suggestion']['content2']['brf']
        
        #error_code
        error_code = data['suggestion']['error_code']['brf']
        
        #reason
        reason = data['suggestion']['reason']['brf']
        
        
        
        return [shengxiao,shengxiao1,shengxiao2,title,content1,content2,error_code,reason]


    except NameError :
        print('不存在此配对')