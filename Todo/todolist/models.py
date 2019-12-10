from datetime import datetime

from django.db import models
import time

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

class Informations(models.Model):
    # id = models.IntegerField('id',primary_key=True)
    text = models.CharField('事项', max_length=99)
    flag = models.BooleanField('标记', max_length=1, choices=((1, '是'), (0, '否')), default=0)
    add_date = models.DateTimeField('保存日期', default=datetime.now)
    mod_date = models.DateTimeField('最后修改日期', auto_now=True)

    class Meta:
        verbose_name = '待办事项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text+"_"+str(self.id)
