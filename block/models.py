# coding: utf-8
#from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserData(models.Model):
    userName = models.CharField(u'用户名', max_length = 30)
    userAge = models.IntegerField(u'年龄')
    userSex = models.IntegerField(u'性别', choices = ((1, '男'), (2, '女')))
    owner = models.ForeignKey(User, verbose_name = '作者')

    create_timestamp = models.DateTimeField(u'创建时间', auto_now_add = True)
    last_update_timestamp = models.DateTimeField(u'修改时间', auto_now = True)

    def __unicode__(self):
        return self.userName + ' 桑'
