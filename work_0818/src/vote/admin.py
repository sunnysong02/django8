from django.contrib import admin
from .models import Question, Choice 
from django.contrib.contenttypes import fields
#동일 경로의 models 에서 클래스 가져옴.
#from .models import * #models.py 내에 있는 클래스, 함수를 전부 추가 
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question_text', 'pub_date')

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'question']    
    list_display = ('id','choice_text','votes','question')
# Register your models here.
#Question 모델 클래스를 관리자 사이트에서 접근할 수 있도록 설정
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)