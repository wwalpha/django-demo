# Django Demo

## Environment

### Download & Install Python
[Python 3.6.4](https://www.python.org/downloads/)

### Set Python Home
```
D:\Code\Tools\Python36\Scripts
```
### Install Django and plugins
```
pip install django
pip install pep8
pip install autopep8
pip install ptvsd
pip install SQLAlchemy
```

## Development Tools
### Download & Install Visual Studio Code(VSCode)
[Visual Studio Code](https://code.visualstudio.com/download)

### Install VSCode plugins (Ctrl + Shift + X)
Find the plugins and install
* python
* vscode-icons

### Edit VSCode Setting

#### User Settings 
```js
"editor.tabSize": 2,
"editor.fontSize": 12
"workbench.iconTheme": "vscode-icons"
```

#### Workspace Settings
```js
"python.pythonPath": "D:/Code/Tools/Python36/python.exe",
"python.linting.pep8Enabled": true,
"python.linting.pylintEnabled": false,
"editor.formatOnSave": true,
```

#### Debug Settings (Ctrl+Shift+D)
* DEBUG -> Add Configuration -> python
* そのまま保存
* DEBUG -> Python:Django、歯車をクリックする
4. [args: --noreload]を削除する
5. F5(2回)で起動後、http://localhost:8000/は確認できる

###プロジェクト作成
####設定ファイルなど生成する
```
django-admin startproject Django
cd Django
python ./manage.py startapp demo
```

####モデルを定義する
python manage.py makemigrations demo

pip install PyMySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'wwalpha',
        'PASSWORD': 'session10',
        'HOST': 'alpha.cinlbecofvo4.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

python .\manage.py migrate

// テーブルからmodels生成
python manage.py inspectdb tablename > models.py

pip install ptvsd
