# -*- coding: utf-8 -*-
import scrapy
START_DATE="2020-01-22 00:00:00"
END_DATE=""
class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']
    def start_requests(self):
        for i in
        with open(r'wiki_google/querys/input.json', 'r') as f:
            querys = json.load(f)
        id=1#第几个query
        for query in querys['query']:
            pre_query=query#用来当文件名输出
            ###HTML ASCII Reference
            new_query=''
            for alpha in query:
                o=ord(alpha)
                if (o >= 33 and o <= 47) or (o >= 58 and o <= 64) or (o >= 91 and o <= 96) or (o >= 123 and o <= 126):
                    new_query+=hex(o).replace('0x','%')
                else:
                    new_query+=alpha
            query = new_query.replace(' ','+')
            ###
            path =r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%BA%B7%E5%A4%8D%E8%80%85&oq=%E5%BA%B7%E5%A4%8D%E8%80%85&rsv_pq=b4c550ab003217aa&rsv_t=e5ed%2Fkfl5kKNDlIefALe9j%2BxAGaJ3UfLlYTBMu6ABIbVMJz7hgG14d1fJMs&rqlang=cn&rsv_enter=1&rsv_dl=tb&gpc=stf%3D1583510400%2C1583510400%7Cstftype%3D2&tfflag=1'
            path = 'https://www.google.com/search?q=%s&hl=en' % query#因为服务器开出来的是english版本 所以爬english的
            # 若直接用谷歌的任意其中一个IP地址172.217.14.78会报Invalid DNS-ID（如果robot设成true直接报错终止 设成false会报warning ）是因为scrapy官方库没写好罢了
            # 当初一直坚持用IP 甚至导致本地windows crawl的时候没response是因为要统一windows和云服务器CentOS那边的界面 方便调试
        #把CentOS的DNS手动改成8.8.8.8
            yield scrapy.Request(url=path,meta={'query': query,'pre_query':pre_query,'id':id,'page':{id:1}},callback=self.parse)#  # 下一个要执行的函数为parse
            id+=1
    def parse(self, response):
        pass
