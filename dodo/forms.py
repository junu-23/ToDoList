from django import forms
from .models import Doit

class TodoForm(forms.ModelForm):
    class Meta:
        model = Doit
        fields = ['what', 'deadline', 'detail']
        #  create_date는 일반적으로 서버에서 자동으로 설정되므로 삭제
        labels = {
            "what": "할일",
            "deadline": "데드라인",
            "detail": "더보기"
        }
#레이블은 폼 필드의 이름이나 설명을 나타내는 텍스트입니다.
# 사용자가 입력할 내용을 이해하도록 돕기 위해 필드와 함께 표시됩니다.

#필드는 사용자가 데이터를 입력할 수 있는 입력 공간입니다.
#입력 필드는 실제 데이터를 수집하는 부분입니다.
#역할: 유효성검사(get,post) (데이터 유효한가, 데이터형식(길이)) / 데이터 입력