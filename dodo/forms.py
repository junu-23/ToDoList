from django import forms
from .models import Doit

class TodoForm(forms.ModelForm):
    class Meta:
        model = Doit
        fields = ['what', 'deadline', 'detail']  # create_date는 일반적으로 서버에서 자동으로 설정되므로 삭제

        labels = {
            "what": "할일",
            "deadline": "데드라인",
            "detail": "더보기"
        }
