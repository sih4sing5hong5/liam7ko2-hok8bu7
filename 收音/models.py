from django.db import models


class 例句表(models.Model):
    漢字 = models.CharField(max_length=255)
    臺羅 = models.CharField(max_length=255)
    華語 = models.CharField(max_length=255)
    其他 = models.CharField(max_length=255, blank=True)


class 例句音檔表(models.Model):
    啥人唸的 = models.CharField(max_length=255)
    例句 = models.ForeignKey(例句表, related_name='資料')
    加入時間 = models.DateTimeField(auto_now_add=True)
    音檔 = models.FileField()
    實際唸的漢字 = models.CharField(max_length=255, blank=True)
    實際唸的臺羅 = models.CharField(max_length=255, blank=True)
