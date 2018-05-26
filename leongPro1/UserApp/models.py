from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20) # 姓名
    upwd = models.CharField(max_length=60) # 密码
    uemail = models.CharField(max_length=40) # 邮箱
    uaddree = models.CharField(max_length=100,null=True) # 地址
    uphone = models.CharField(max_length=11,null=True) # 电话
    ureceive = models.CharField(max_length=20,null=True) # 收件人
    uzip_code = models.CharField(max_length=6,null=True) # 邮编