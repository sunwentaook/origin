import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
    """商品分类"""
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    """商品"""
    gtitle = models.CharField(max_length=20)
    # 图片位置
    gpic = models.ImageField(upload_to='/static/media/')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    # 单位
    gunit = models.IntegerField(default=500)
    # 点击量 用于排序
    gclick = models.IntegerField(default=0)
    # 简介
    gjianjie = models.CharField(max_length=200,null=True)
    gpub_date = models.DateTimeField(datetime.datetime.now(),null=True)
    gpubj_date = models.DateTimeField(null=True)
    gtype = models.ForeignKey(TypeInfo,null=True)
    def __str__(self):
        return self.gtitle.encode('utf-8')


class Gouwu(models.Model):
    uname = models.CharField(max_length=40)
    utitle = models.CharField(max_length=40)
    unumber  = models.IntegerField()
    ushu = models.IntegerField()
    uprice = models.DecimalField(max_digits=5,decimal_places=2)
    udanjia = models.DecimalField(max_digits=5,decimal_places=2)
    upic = RichTextUploadingField()

class Dingdan(models.Model):
    uname = models.CharField(max_length=40)
    utitle = models.CharField(max_length=40)
    unumber = models.IntegerField()
    ushu = models.IntegerField()
    uprice = models.DecimalField(max_digits=5, decimal_places=2)
    udanjia = models.DecimalField(max_digits=5, decimal_places=2)
    upic = RichTextUploadingField()
    dingdan = models.IntegerField()
    zongjia = models.DecimalField(max_digits=5, decimal_places=2)

class XD(models.Model):
    name = models.CharField(max_length=40)
    danhao = models.IntegerField()
    zongjia = models.DecimalField(max_digits=5, decimal_places=2)