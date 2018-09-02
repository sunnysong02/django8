from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

# 모델클래스 정의시 models.py에 있는 Model 클래스 상속받음
class Question(models.Model):
     #질문 내용 저장할 수 있도록 함., charField라는 객체를 생성
     #저장할 속성을 models.클래스()명으로 객체 생성후 변수에 대입
     #models.CharField : 글자수 제한을 두는 문자열을 저장할 때 사용.
     #models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField('질문 문구', max_length=200)
    #models.DateTimeField() : 날짜+시간 정보를 저장할 때 사용
    pub_date = models.DateTimeField('작성일')
    #각 속성에 null변수와 blank 변수를 True 설정하면 값이 비어있어도
    #객체가 생성되도록 설정
    def __str__(self): #함수 오버라이드
        return self.question_text #객체 안의 변수접근시 self. 필요

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    #models.IntegerField() : 정수값을 저장할 때 사용
    votes = models.IntegerField(default=0)
    #models.Foreignkey : 다른 모델 클래스에와 연결고리를 만들 때 사용
    #이 때 1:n 관계를 가짐. (여러개 답변 가능..)
    #on_delete : 연결지은 모델클래스의 객체가 삭제될 경우 자신이 삭제될 것인지 
    #            명시하는 매개변수.
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    #어떤 모델 클래스랑 연결할 것인지, 삭제되면 그대로 있을 것인지 함께 사라질 것인지에 대한 옵션임.
    def __str__(self):
        return self.choice_text
    

    