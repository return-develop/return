from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "", 'autofocus': ''}))
    # 用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ""}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    # gender = (
    #     ('male', "男"),
    #     ('female', "女"),
    # )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="设置密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="输入邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # sex = forms.ChoiceField(label='性别', choices=gender)
    # captcha = CaptchaField(label='验证码')
