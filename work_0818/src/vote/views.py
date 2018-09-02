from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponseRedirect
from django.urls import reverse
#HttpResponseRedirect : 클라이언트에게 HTML 파일을 전달하는 것이 아닌
#URL 주소를 전달 -> 웹 클라이언트는 받은 URL 주소로 웹서버에 재요청
#reverse 함수 : url의 별칭(name)을 이용해 URL주소를 찾는 함수 (Template 엔진의 url함수와 동일 기능 제공)

#함수 of 클래스 형태로 뷰 구현
#함수형태로 구현시 첫번째 매개변수로 request를 받아야 함. (클래스 만들 때 self 처럼)
#request : 웹 클라이언트의 요청에 대한 정보를 알고있는 매개변수
#render : html 파일 넘겨줄 때 사용 됨. html문서에서 어떤 값을 쓰고 싶으면 3번째 매개변수에 
#딕셔너리 형태로 넘겨주면 됨.

'''
def index(request):
    #render(request, html 파일경로, 템플릿에서 사용할 데이터-사전 형태)
    return render(request, 'vote/index.html', {'hello':'django 개발'})  
'''
#질문 목록 보기
def index(request):
    #list = Question.objects.all() : 데이터베이스에 저장된 모든 Question 객체를
    #                                리스트형태로 가져옴
    list = Question.objects.all()
    print(list)
    
    return render(request, 'vote/index.html',{'question_list':list})

#설문지 출력 및 투표 선택
def detail(request, question_id):
    #매개변수에 작성한 조건에 따라 모델클래스의 객체 1 개를 추출
    #매개변수이름은 모델클래스에서 작성한 변수를 사용 가능
    #내부적으로 id변수(고유 키)가 추가됨
    obj = Question.objects.get(id=question_id)
    return render(request, 'vote/detail.html',{'question':obj})

#request에는 form 태그사이의 데이터들이 존재함. (POST방식이란 정보도 들어가 있음.)
#투표처리
def vote(request):
    #request.method : 클라이언트의 요청이 GET방식인지 POST방식인지 저장한 변수
    #문자열 비교시 "GET"/"POST" 문자열과 같은지 비교 (전부 대문자로 작성)
    if request.method == "POST": #클라이언트 요청이 POST인가?
        #request.POST : POST 요청으로 온 데이터 전부를 의미함.
        #get('choice') : 그 중 한개 데이터 뽑아내기.
        #get함수가 반환하는 값은 전부 문자열. 정수 추출 원하면, 정수 변환 필요함.
        id = request.POST.get('choice')
        #pk : Choice 객체의 id변수와 동일
        obj = get_object_or_404(Choice, pk = id)
        obj.votes += 1 
        obj.save() #객체의 변경 사항을 데이터베이스(DB)에 저장 
        #obj.question : choice 객체가 연결된 Question 객체를 뜻함.
        #obj.question.question_text : choice 객체가 연결된 Question의 Question_text를 꺼내는 것.
    return HttpResponseRedirect(reverse('result', args=(obj.question.id,) ))


def result(request, question_id):
    #obj 변수 : Question 객체
    obj = get_object_or_404(Question, pk = question_id)
    return render(request,'vote/result.html',{'obj':obj})

from .forms import *
import datetime #시간에 관한 모듈 

@login_required
def registerQ(request):
    #하나의 뷰 함수는 사용자가 GET/POST 요청할 때를 구분지어서 작업
    if request.method == "GET":
        #QuestionForm 객체 생성. 사용자로부터 입력받을 변수값을 HTML
        #문서에서 처리할 수 있도록 HTML 코드로 변환 기능
        #객체를 생성한 경우, <input>태그에 값이 비어있는 상태로 사용자
        #에게 전달
        form = QuestionForm()
        return render(request, 'vote/registerQ.html', {'form':form})
    elif request.method == "POST":
        #form 객체 생성시 사용자가 입력한 데이터를 각 폼 변수에 대입
        form = QuestionForm(request.POST) #사용자가 전달했던 데이터 이용.
        
        if form.is_valid(): #해당 폼에 입력값들이 에러가 없는지 확인  True/False 반환됨.
            #form.save()
            #해당 폼에 입력값들로 모델클래스 객체를 생성 후
            #데이터베이스에 저장.
            obj = form.save(commit=False)#해당 폼에 입력값들로 모델 클래스 생성
            obj.pub_date = datetime.datetime.now() #현재시간대입
            obj.author = request.user #글쓴이 등록
            obj.save()  
            return HttpResponseRedirect(reverse('detail',args=(obj.id,))) 
@login_required        
def registerC(request):
    if request.method == "GET":#vote/registerC.html 을 사용
        #GET 방식 처리코드 만들기 1)폼객체 생성 2)render함수 변환
        form = ChoiceForm()
        return render(request, 'vote/registerC.html', {'form':form})
    elif request.method == "POST":
        #1)사용자 데이터를 기반으로 폼객체 생성
        form = ChoiceForm(request.POST)
        
        #2)유요한 값이 들어있는 폼인지 확인
        if form.is_valid():
            #print(request.user) #현재로그인된 유저
            #print(form.cleaned_data['question']) #Question 모델 클래스의 객체
            #print(request.POST.get('question'))
            #현재 로그인된 유저와 Question 모델 클래스 객체에 저장된
            #글쓴이 비교
            if request.user == form.cleaned_data['question'].author :

                #3)모델클래스 객체를 생성및 데이터베이스에 저장
                obj = form.save()#해당 폼에 입력값들로 모델 클래스 생성
                #4)'detail' 별칭을 가진 URL로 반환  
                return HttpResponseRedirect(reverse('detail',args=(obj.question.id,)))
            else:
                return render(request, 'vote/registerC.html', {'form':form,
                                        'error':'현재 로그인된 유저의 글이 아닙니다.'})
@login_required        
def deleteQ(request, question_id):
    #삭제할 객체 찾기
    #pk=id 동일
    obj = get_object_or_404(Question, pk=question_id)
    obj.delete() #해당 객체를 데이터베이스에서 제거
    return HttpResponseRedirect(reverse('index'))
@login_required
def deleteC(request, choice_id):
    #삭제할 객체 찾기
    #pk=id 동일
    obj = get_object_or_404(Choice, pk=choice_id)
    question_id = obj.question.id
    obj.delete() #해당 객체를 데이터베이스에서 제거
    return HttpResponseRedirect(reverse('detail', args=(question_id,)))

@login_required
def updateQ(request, question_id):
    obj = get_object_or_404(Question, pk=question_id)
    if request.method == "GET":
        #Question 객체에 저장된 값을 QuestionForm 객체를 생성할 때 입력
        #모델폼 생성자에 instance 매개변수는 이미 생성된 모델클래스의 객체를
        #넣어야 함.
        form = QuestionForm(instance = obj)
        return render(request, 'vote/updateQ.html', {'form':form})
    elif request.method == "POST":
        #이미 생성된 Question 객체에 변수값들을 클라이언트가 작성한 내용으로
        #덮어 씌움
        form = QuestionForm(request.POST, instance = obj) #사용자가 입력했던 값들이 객체에 저장.
        if form.is_valid():            
            question = form.save()
            #question = form.save(commit=False) #commit=False 없이하면 pub_data 
            #가 공란이기 때문에 에러발생. 이를 예방하기 위해 추가함.
            #question.pub_date = obj.pub_date
            #question.save()
            return HttpResponseRedirect(
                reverse('detail',args=(question.id,))) 
@login_required            
def updateC(request, choice_id):#변수 이름은 자유롭게
    obj = get_object_or_404(Choice, pk=choice_id)#Choice 모델 클래스에서 choice_id에 해당하는 놈을 obj에 담겠다.
    if request.method == "GET": #링크들어온 상태
  
        form = ChoiceForm(instance = obj)#instance = obj가 글자를 채워주는 것임
        #html 문서로 전달.
        return render(request, 'vote/updateC.html', {'data':form}) 
    elif request.method == "POST":       
        form = ChoiceForm(request.POST, instance = obj) #사용자가 입력했던 값들이 객체에 저장.
        #사용자 정보의 일부분을 꺼내고 싶을 때, 이걸 안쓰면, 데이터를 꺼내기와 저장안됨.
        if form.is_valid():            
            #form.save() #우리는 question id(외래키연결)를 추출해야 함. 왜냐면 url로 전달해야함.
            #choice_text.question.id 얻어낼 수 있음. question은 모델클래스에서 
            #지정한 변수명.
            cho = form.save()
            
            return HttpResponseRedirect(
                reverse('detail',args=(cho.question.id,))) 
            
        else:#사용자의 입력이 유효하지 않는 데이터인경우
            #다시 html문서를 전달하면서 특정변수에 에러문구 대입
            return render(request, 'vote/updateC.html', 
                          {'data':form, 'error':'유효하지 않은 입력'})    
            
            
                    