# -*- coding: utf-8 -*-

'''
@Time    : 2020/7/26 18:44
@Author  : Wanhao Zhang
@Contact : 1809721229@qq.com 
@FileName: urls.py
@Software: PyCharm
 
'''

# 定义 learning_logs 的URL模式
from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic')
]