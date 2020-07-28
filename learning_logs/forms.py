# -*- coding: utf-8 -*-

'''
@Time    : 2020/7/28 20:28
@Author  : Wanhao Zhang
@Contact : 1809721229@qq.com 
@FileName: forms.py
@Software: PyCharm
 
'''
from django import forms

from .models import Topic
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}