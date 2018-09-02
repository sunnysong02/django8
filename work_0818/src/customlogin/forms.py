'''
Created on 2018. 8. 26.

@author: user
'''
#모델클래스를 기반으로 입력양식 제공할 것임. 그래서 모델을 상속받자
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    #UserForm(instance = obj)
    #print(kwargs) -> {'instnace':obj}
    def __init__ (self, *args, **kwargs):#**매개변수로 언급되지 않은 것을 넣었을 때 들어가는 공간
        #ModelForm.__init____(*args, **kwargs)
        super().__init__(*args, **kwargs)
        #객체 .fields[키값] : 해당 폼 클래스에서 설정한 fields, 변수에
        #입력되는 설정값들을 수정,읽기 할 수 있음.
        #객체.fields[키값].label : <label>태그에 들어갈 문구를 저장한 변수
        self.fields['password_check'].label = "패스워드 확인"
    #모델클래스와 유사하게 xxxxField클래스의 객체를 변수에 저장해 새로운
    #<input>  태그를 생성할 수 있음.
    password_check = forms.CharField(max_length=200,
                                    widget=forms.PasswordInput() ) #필요한 변수 생성
    
    class Meta:
        model = User
        #모델 클래스에서 사용되는 변수들 한테, 위젯을 적용시킬때 사용하는 변수
        widgets ={
            'password':forms.PasswordInput(),
            'email':forms.EmailInput(),
            }            
        fields = ['username','password','email', 'password_check']
    #로그인에 사용할 입력양식
class LoginForm(ModelForm):
    class Meta:
        model = User
        #widgets : 각 변수에 입력 스타일을 설정할 때 사용하는 변수
        #키 : 변수명      값 : xxxxInput 클래스 객체 
        widgets ={
            'password':forms.PasswordInput(),         
            } 
        fields = ['username','password']
        
    