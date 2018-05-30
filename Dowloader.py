#coding:utf-8
import urllib
import urllib2
import ssl
class Dowload(object):
    def __init__(self):
        pass
    def get_url_page(self, city, keyword, in_sg, page, region=None):
        city = urllib.quote(city)
        keyword = urllib.quote(keyword)
        '''    获取搜索职业结果页面    '''
        # url参数设置

        paras = {
            'jl': city,  # 搜索城市
            'kw': keyword,  # 搜索关键词
            'isadv': 0,  # 是否打开更详细搜索选项
            'isfilter': 0,  # 是否对结果过滤
            'sg': in_sg,
            'p': page,  # 页数
            're': region  # region的缩写，地区，2005代表海淀
        }

        #  hearder头信息设置

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Host': 'sou.zhaopin.com',
            'Referer': 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&isadv=0&isfilter=0&sg=%s&p=%s'%(paras['jl'],paras['kw'],paras['sg'],paras['p']),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'

        }

        try:
            print 'kaishi'
            request = urllib2.Request(url=header['Referer'],headers=header)
            print '请求已建立'
            #print header['Referer']
            response = urllib2.urlopen(request)


            if response.getcode() == 200:
                return response.read()
            return None
        except Exception as e:
            print e.__str__()
            return None

    def get_text_page(self,url):

        '''    获取职业详细信息页面     '''

        #  hearder头信息设置

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Host': 'jobs.zhaopin.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'

        }

        try:
            '''
            
                在试验当中发现这个url是http存在于服务器中，但是因为网站更新为https协议，
                为了少改服务器配置，服务器方会进行一部分操作，让http类url自动在客户端的浏览器里变为https访问
                则在爬虫中可自行改为https，不改会报错，在浏览器上查看network会有个有意思的发现，浏览器在访问这个http类url时，
                会访问三次，直到第三次才会成功，斜眼笑
            
            
            '''
            url = 'https'+url[4::1]
            print url

            '''
                因为这个网站是自签证证书，在python2.7.9之后加入新特性，如果用urlopen访问一个https链接时会验证
                一次ssl证书，而目标网站是
                自签证证书网站，则会报错，所以使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
            
            '''

            context = ssl._create_unverified_context()


            request = urllib2.Request(url=url,headers=header)

            response = urllib2.urlopen(request,context=context)
            print response.getcode()

            if response.getcode() == 200 :
                return response.read()
            return None
        except Exception as e :
            print e.__str__()
            return None


