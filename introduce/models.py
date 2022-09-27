from django.db import models

class AcessLog(models.Model):
    class Meta:
        db_table = "my_data"

    created_at = models.DateTimeField("접속 시간", auto_now_add=True)
    location = models.CharField("접속 경로", max_length = 50)


    def __str__(self) -> str:
        return f"{self.created_at} / {self.location}"
    



    '''
    1. default : 기본적으로 상용될 날짜를 사용자가 지정
    2. auto_now : 데이터가 수정 될 때마다 갱신됨
    3. auto_now_add : 데이터가 생성 될때 시간을 기록

    같이쓰면 오류됨
    '''
