'''
Created on 2018. 8. 25.

@author: user
'''
#form : HTML 코드에서 사용할 입력 양식(<form>)을 모델클래스에 맞게 
#자동으로 만들어주는 기능 or 커스텀 입력양식을 만드는 기능을 제공함.

#class 폼클래스명(ModelForm) : 모델클래스에 관한 폼을 정의
#class 폼클래스명(Form) : HTML에서 사용할 커스텀 폼을 정의
from django.forms.models import ModelForm
#from . import models #현재 폴더(.)내에 models 파일을 임포트
from .models import Question, Choice #현재 폴더에 있는 models 파일에서 전체(*) 임포트


class QuestionForm(ModelForm):
    class Meta: #Meta클래스 정의를 통해 모델 클래스에 관한 정보를 입력
        #model : 모델클래스 명(해당 폼에 매칭할 모델클래스를 작성)
        #fields or exclude 중 하나를 선택해 사용
        #fields : 해당 모델폼을 통해 클라이언트가 입력할수잇는 데이터를 명시
        #        모델클래스의 변수명을 리스트형태로 입력
        #exclude : 모델클래스의 변수 중 명시한 변수명을 제외한 나머지 변수들을
        #         클라이언트가 작성할 수 있도록 제공(리스트형태)
        model = Question #해당 클래스가 Question 모델 클래스와 연동됨을 명시
        #사용자가 question_text 변수에 들어갈 값만 입력할 수 있도록<input>태그
        #가 생성됨.
        #fields = ['question_text']
        #pub_date를 제외시킴, 사용자가 pub_data 변수 외에 변수들을 입력할 수 있도록
        #<input>태그가 생성됨.
        exclude = ['pub_date','author']
    
#선택지 문구, 어떤 질문에 묶일 것인지, 선택할 수 있는 입력 양식    
class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['question','choice_text']
        #exclude = ['votes']