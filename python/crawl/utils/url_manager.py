
class UrlManager():
    """URL管理器"""
    def __init__(self):
        """初始化URL管理器"""
        self.new_urls=set() # 未爬取的URL集合
        self.old_urls=set() # 已爬取的URL集合
       

    def add_new_url(self, url):
        if url is None or len(url)==0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)
        """添加新的URL"""
    def add_new_urls(self, urls):
        """批量添加新的URL"""
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def has_new_url(self):
        """判断是否有新的URL"""
        return len(self.new_urls)>0
    def get_new_url(self):
        """获取新的URL"""
        if self.has_new_url():
            
         new_url=self.new_urls.pop()
         self.old_urls.add(new_url)
         return new_url
        else:
            return None

if __name__=="__main__":
    url_manager=UrlManager()
    url_manager.add_new_url("http://www.baidu.com")
    url_manager.add_new_urls(["http://www.baidu.com","http://www.sina.com"])
    print(url_manager.new_urls,url_manager.old_urls)

    print("#"*30)

    new_url=url_manager.get_new_url()
    print(url_manager.new_urls,url_manager.old_urls)
    print("#"*30)
    
    new_url=url_manager.get_new_url()
    print(url_manager.new_urls,url_manager.old_urls)
    print("#"*30)
    print(url_manager.has_new_url())
