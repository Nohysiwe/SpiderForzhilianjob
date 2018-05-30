#coding:utf-8
from bs4 import BeautifulSoup
import re
class Parse(object):
    def __init__(self):
        pass

    def parse_url_page(self,response):

        '''

            解析url页面，得到页面数以及url

        '''

        if response == None:    #如果页面没打开则直接不解析，返回None
            return 0,None
        try :

            soup = BeautifulSoup(response, 'lxml', from_encoding='utf-8')

            all_ts = soup.select("div.seach_yx > span.search_yx_tj > em")
            # print all_ts

            all_ts = int(all_ts[0].get_text())

            ts_url = soup.select("table.newlist > tr > td.zwmc > div > a['style']")

            # print ts_url

            page_ts = len(ts_url)

            # print page_ts, all_ts

            pages = all_ts / page_ts

            return pages, map(lambda x: x.attrs['href'], ts_url)

        except Exception as e:
            print str(e)#如果页面内容为空，则解析时会报错，则返回空
            return 0,None

    def parse_text_page(self,response):

        '''

            解析详细职业信息页面，得到其内容

        '''
        # job_info_lis = ['职位月薪','工作地点','发布日期','工作性质','工作经验','最低学历','招聘人数','职位类别','公司名称','公司规模','公司性质','公司行业','公司主页','公司地址']    #详细页面的工作8个数据信息
        # com_info_lis = ['公司规模','公司性质','公司行业','公司主页','公司地址']    #详细页面的公司5个数据
        # all_info_dic = {}
        all_info_lis = []

        print 'kaishitext'

        if response == None :
            return None

        try:
            soup = BeautifulSoup(response, 'lxml', from_encoding='utf-8')

            job_info_tag = soup.find('ul',class_='terminal-ul clearfix')

            job_info = job_info_tag.find_all('strong')

            job_info = map(lambda x : x.get_text(),job_info)        #job详细信息

            com_info_name = soup.find('p',class_ = 'company-name-t').find('a',rel = 'nofollow').get_text()      #公司名字

            #all_info_dic['公司名称'] = com_info_name

            com_info_tag = soup.find('ul',class_ = 'terminal-ul clearfix terminal-company mt20')

            com_info = com_info_tag.find_all('strong')

            #com_info_lis_tag = com_info_tag.find_all('span')

            #com_info_lis = map(lambda x : x.get_text()[0:-1:1],com_info_lis_tag)

            com_info = map(lambda x : x.get_text(),com_info)        #公司详细信息

            if len(com_info) < 5:

                for i in job_info:
                    all_info_lis.append(i)

                all_info_lis.append(com_info_name)

                for j in range(3):
                    all_info_lis.append(com_info[j])

                all_info_lis.append(u'无')

                all_info_lis.append(com_info[-1])

            else:
                for i in job_info:
                    all_info_lis.append(i)

                all_info_lis.append(com_info_name)

                for j in range(5):
                    all_info_lis.append(com_info[j])




            # for i in range(len(job_info)):
            #     all_info_dic[job_info_lis[i]] = job_info[i]
            #
            # for i in range(len(com_info)):
            #     all_info_dic[com_info_lis[i]] = com_info[i]

            return all_info_lis

        except Exception as e:
            print str(e)
            return None




