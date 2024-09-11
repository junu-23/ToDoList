from django.db import models

class Doit(models.Model):
    what = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    deadline = models.CharField(max_length=30, blank=True, null=True)  #default='' -> null=True
    detail = models.TextField(blank=True, null=True)  #default='' -> null=True
    is_done = models.BooleanField(default=False)  # 완료 여부
    #  what, deadline, detail, create_date : 필드

    def __str__(self):
        return self.what
    #  print(instance) 또는 Django 관리 페이지에서 인스턴스가 나열될 때,
    #  __str__ 메소드에서 반환된 what 필드의 값이 출력됩니다. 예를 들어, what 필드에 "Buy groceries"라는 값이 들어있다면,
    #  이 모델 인스턴스를 출력할 때 "Buy groceries"가 표시됩니다.
