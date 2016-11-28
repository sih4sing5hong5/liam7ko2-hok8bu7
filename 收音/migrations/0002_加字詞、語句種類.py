# -*- coding: utf-8 -*-
from csv import DictReader
from os.path import join, dirname, abspath

from django.db import migrations
from curses.ascii import isupper
from 臺灣言語工具.基本物件.公用變數 import 標點符號


def _加教育部例句(apps, schema_editor):
    例句表 = apps.get_model("收音", "例句表")

    with open(join(dirname(abspath(__file__)), '..', '語料', '例句.csv')) as 檔:
        讀檔 = DictReader(檔)
        for row in 讀檔:
            漢字 = row['例句'].strip()
            音標 = row['例句標音'].strip()
            華語 = row['華語翻譯'].strip()
            if 華語 == '':
                華語 = 漢字
            if isupper(音標[0]) and 音標[-1] in 標點符號:
                例句表.objects.create(漢字=漢字, 臺羅=音標, 華語=華語)


class Migration(migrations.Migration):

    dependencies = [
        ('收音', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(_加教育部例句),
    ]
