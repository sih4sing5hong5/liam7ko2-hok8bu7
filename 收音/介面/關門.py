from django.http.response import HttpResponse, HttpResponseForbidden


def 登入無(request):
    try:
        if request.user.socialaccount_set.exists():
            return HttpResponse('有登入！！')
    except:
        pass
    return HttpResponseForbidden()


def 關門(request):
    return HttpResponse('登入成功！！可以回到原本的網頁存檔！！')
