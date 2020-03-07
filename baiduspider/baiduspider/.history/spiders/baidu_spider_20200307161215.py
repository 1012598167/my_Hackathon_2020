# -*- coding: utf-8 -*-
import scrapy
import time,datetime
import json
START_DATE="2020-01-22 00:00:00"
END_DATE="2020-03-06 00:00:00"
def str2datetime(str):
    return datetime.datetime.strptime(str,"%Y-%m-%d %H:%M:%S")
def gettimestamp(str):
    import time,datetime
    time1=datetime.datetime.strptime(str,"%Y-%m-%d %H:%M:%S")
    secondsFrom1970=time.mktime(time1.timetuple())
    return secondsFrom1970
def gettimename(str):
    return str[0:4]+str[5:7]+str[8:10]
class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']
    
    def start_requests(self):
        date=START_DATE
        while (str2datetime(END_DATE)-str2datetime(date)).days>0:
            # path =r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%BA%B7%E5%A4%8D%E8%80%85\
            #     &oq=%E5%BA%B7%E5%A4%8D%E8%80%85&rsv_pq=b4c550ab003217aa&rsv_t=e5ed%2Fkfl5kKNDlIefALe9j%2Bx\
            #         AGaJ3UfLlYTBMu6ABIbVMJz7hgG14d1fJMs&rqlang=cn&rsv_enter=1&rsv_dl=tb&gpc=stf%3D'\
            #         +str(gettimestamp(date))+r'%2C'+str(gettimestamp(date))+r'%7Cstftype%3D2&tfflag=1'


            #path=r'http://www.baidu.com/s?wd=密切接触者&gpc=stf%3D'\
            #        +str(gettimestamp(date))+r'%2C'+str(gettimestamp(date))+r'%7Cstftype%3D2'
            path=r'http://www.baidu.com/s?wd=康复者&gpc=stf%3D'\
                    +str(gettimestamp(date))+r'%2C'+str(gettimestamp(date))+r'%7Cstftype%3D2'
            print(path)
            yield scrapy.Request(url=path,meta={'filename': gettimename(date)},callback=self.parse)
            date=str(str2datetime(date)+datetime.timedelta(days=1))
        
    def parse(self, response):
        filename = response.meta['filename']
        res_path = r'./results_recovery'#r'./results_toucher'#一定要初始化成{}!
        f_name = res_path + '/' + 'all'+ '.json'  # 要导入结果的文件名
        with open(f_name,'r', encoding='UTF-8') as f:#一定要初始化成{}!
            all_dict = json.load(f)
        
        
        fw = open(f_name, 'w', encoding='utf-8')  # 覆盖写
        #fw.write('1111111111\n')
        fields = response.xpath('.//div[contains(@class,"result")]')
        print('###########',fields,'###########')
        new_dict={}
        for i in fields:
            title=i.xpath('./h3/a//text()').extract_first().replace('\n', '')
            link=i.xpath('./h3/a//@href').extract_first()
            new_dict[title]=link
        all_dict[filename]=[new_dict]
        json.dump(all_dict,fw)
        fw.close()
        # pre_query=response.meta['pre_query']
        # id=response.meta['id']
        # page=response.meta['page']
        # fields = response.xpath('.//div[@class="ZINbbc xpd O9g5cc uUPGi"]')
        # page_value=page[id]

        # res_path = r'wiki_google/results'
        pass