from django.forms.models import ModelForm
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['type','headline','contents']
        #exclude = ['pub_date', 'author']
    #생성자 overridng 해서 posttype이 없는것 삭제    
    def __init__(self, *args, **kwargs):
        super().__init__(self,*args, **kwargs)
        #사용자가 글종류를 선택하지 않았을 때의 기본값을 없앨 때 None 씀
        self.fields['type'].empty_label = None
        self.fields['type'].label = '글종류'
        
        
        