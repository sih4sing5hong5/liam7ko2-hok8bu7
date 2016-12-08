# 唸稿服務
[![Build Status](https://travis-ci.org/sih4sing5hong5/liam7ko2-hok8bu7.svg?branch=master)](https://travis-ci.org/sih4sing5hong5/liam7ko2-hok8bu7)

```
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip # 設置環境檔
pip install -r requirements.txt
python digital.py migrate
gunicorn digital.wsgi
```
