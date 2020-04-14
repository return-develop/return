### Django可重用登录与注册系统
#### 项目环境
* Django==2.2.7
* django-ranged-response==0.2.0
* django-simple-captcha==0.5.12
* Pillow==6.2.1
* pytz==2019.3
* six==1.13.0
* sqlparse==0.3.0

#### 路由设计
URL|视图|模板|说明
-|-|-|-
index|login.views.index|index.html|主页
login|login.views.login|login.html|登录
register|login.views.register|register.html|注册
logout|login.views.logout|NAN|登出
