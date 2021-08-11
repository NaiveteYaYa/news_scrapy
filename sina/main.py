# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 22:05
# @Author  : WuxieYaYa

from scrapy import cmdline

cmdline.execute('scrapy crawl sina2 -a page=10 -a flag=0'.split())