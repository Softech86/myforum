# coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserData(models.Model):
    userName = models.CharField(u'名字', max_length = 30)
    userDesc = models.CharField(u'描述', max_length = 1000)
    #author = models.ForeignKey(User, verbose_name = '负责人')

    create_timestamp = models.DateTimeField(u'创建时间', auto_now_add = True)
    last_update_timestamp = models.DateTimeField(u'修改时间', auto_now = True)

    class Meta:
        verbose_name = u'建设者板块'
        verbose_name_plural = u'建设者们板块'
