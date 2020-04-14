from django.db import models


# Create your models here.


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    '''
    birth_date = models.DateField()
    phone = models.CharField(max_length = 128, unique=True)
    graduate_university = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    desired_position = models.CharField(max_length=128)
    desired_salary = models.CharField(max_length=128)
    '''
    c_time = models.DateTimeField(auto_now_add=True)
    
    # 人性化显示对象信息
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
