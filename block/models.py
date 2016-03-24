# coding: utf-8

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Block(models.Model):
    name = models.CharField(u'板块名称', max_length = 30)
    desc = models.CharField(u'板块简介', max_length = 200)
    author = models.ForeignKey(User, verbose_name = u'作者')

    create_timestamp = models.DateTimeField(u'创建时间', auto_now_add = True)
    last_update_timestamp = models.DateTimeField(u'修改时间', auto_now = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'板块'
        verbose_name_plural = u'板块'
