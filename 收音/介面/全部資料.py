from 拍字.models import 書面表
from django.http.response import JsonResponse


def 全部書面資料(request):
    return JsonResponse({
        '資料': list(書面表.objects.all().values())
    })
