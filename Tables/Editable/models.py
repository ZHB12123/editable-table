from django.db import models

# Create your models here.
class MicroServiceInfo(models.Model):
    mirror_env =  models.CharField(max_length=100, default=None, help_text="环境名称")
    micro_service = models.CharField(max_length=100, default=None, help_text="微服务名称")
    ip_address = models.CharField(max_length=100, default=None, help_text="微服务运行服务器ip")
    root_passwd = models.CharField(max_length=100, default=None, help_text="root用户密码")
    hispace_passwd = models.CharField(max_length=100, default=None, help_text="hispace用户密码")
    ops = models.CharField(max_length=100, default=None, help_text="测试部署负责人")
    dev = models.CharField(max_length=100, default=None, help_text="开发负责人")
    version = models.CharField(max_length=100, default=None, help_text="版本号")
    branch = models.CharField(max_length=100, default=None, help_text="分支")
    