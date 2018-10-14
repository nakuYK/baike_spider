#总调度程序
import url_manager,html_downloader,html_outputer,html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloder()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                #取出url
                new_url=self.urls.get_new_url()
                print('craw %d : %s' % (count,new_url))
                #下载对应页面
                html_cont=self.downloader.download(new_url)
                #进行解析，得到新的urls和数据data
                new_urls,new_data=self.parser.parser(new_url,html_cont)
                #将新的urls补充进url管理器
                self.urls.add_new_urls(new_urls)
                #数据保存
                self.outputer.collect_data(new_data)
                #爬取100个页面
                if count==100:
                    break
                count=count+1
            except:
                #抛出异常：爬取失败
                print("craw failed")
        #调用outputer中的方法输出数据
        self.outputer.output_html()


if __name__=="__main__":
    root_url="https://baike.baidu.com/item/Python"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
