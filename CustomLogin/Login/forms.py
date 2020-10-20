from django import forms
from django.contrib.auth import authenticate,get_user_model

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username,password=password)

            if not user:
                raise forms.ValidationError('User Does Not Exist')
            
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
        
        return super(UserLoginForm, self).clean(*args,**kwargs)

user=get_user_model()

class UserRegisterForm(forms.ModelForm):
    email=forms.EmailField(label='Email Address')
    email2=forms.EmailField(label='Confirm Email Address')

    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=user
        fields=[
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        email2=self.cleaned_data.get('email2')

        if email!=email2:
            raise forms.ValidationError("Emails Don't Match")

        email_qs=user.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Emails Already In Use")

        return super(UserRegisterForm, self).clean(*args,**kwargs)