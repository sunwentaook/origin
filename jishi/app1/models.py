from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20) # 姓名
    upwd = models.CharField(max_length=60) # 密码
    uemail = models.EmailField(max_length=40, default='无') # 邮箱
    uaddree = models.CharField(max_length=100, default='无') # 地址
    uliuyan = models.CharField(max_length=200, default='无') # 留言