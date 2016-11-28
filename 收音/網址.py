# -*- coding: utf-8 -*-
from django.conf.urls import url
from 收音.介面.稿 import 稿

urlpatterns = [
    url(r'^稿/$', 稿.as_view()),
]
