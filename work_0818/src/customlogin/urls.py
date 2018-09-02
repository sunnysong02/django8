from django.urls.conf import path
from .views import *
from django.contrib.auth import views

#app_name : 해당 파일에서 별칭으로 등록된 url들을 호출할 때
#app_name : 별칭으로 호출해, 충돌이 생기지 않도록 설정.
app_name = 'customlogin'
#reverse('customlogin:sighup') 이렇게 작성 해줘야 함.
#{% url 'customlogin:sign'%}

urlpatterns = [
    #127.0.0.1:8000/login/signup
    path('signup/', signup, name='signup'),
    #127.0.0.1:8000/login/signin
    path('signin/', signin, name='signin'),
    path('logout/', auth_logout, name='logout'),
    
    ]