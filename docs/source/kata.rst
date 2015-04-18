=================================
Pyramid katas
=================================

前提
-----------------------------

- Python 3.4.3


環境作成
-----------------------------

プロジェクト用の環境とpypaツールの準備

UNIX系 ::

   pyvenv .venv
   . .venv/bin/activate
   pip install -U pip
   pip install -U setuptools

windows (powershell) ::

   c:\python34\python c:\python34\tools\scripts\pyvenv.py .venv
   .venv\scripts\activate.ps1
   python -m pip install -U pip
   python -m pip install -U setuptools


共通::

  pip install wheel
  pip wheel wheel


WSGI
-------------------------

waitressをインストール::

  pip wheel -f wheelhouse waitress
  pip install -f wheelhouse waitress

インストール確認::

  waitress-server -h

.. literalinclude:: wsgiapp.py
   :language: python
   :caption: wsgiアプリケーション

Webアプリケーションを実行::

   waitress-serve wsgiapp.application


webob
-------------------------

webobをインストール::

  pip wheel webob -f wheelhouse
  pip install webob -f wheelhouse

.. literalinclude:: webobapp.py
   :language: python
   :caption: webobを使ったwsgiアプリケーション

.. literalinclude:: webobdecapp.py
   :language: python
   :caption: webob.dec.wsgifyを使ったwsgiアプリケーション

pyramid
----------------------------

pyramidをインストール::

  pip wheel -f wheelhouse pyramid
  pip install -f wheelhouse pyramid

.. literalinclude:: pyramidminapp.py
   :language: python
   :caption: pyramidの最小アプリケーション

pyramidアプリケーションのモジュール化
------------------------------------------------


- myapp1

  - __init__.py
  - wsgi.py
  - views.py


.. literalinclude:: myapp1/__init__.py
   :language: python
   :caption: __init__.py: アプリケーションのエントリポイント

.. literalinclude:: myapp1/views.py
   :language: python
   :caption: views.py: webアプリケーションビュー


.. literalinclude:: myapp1/wsgi.py
   :language: python
   :caption: wsgi.py: wsgiアプリケーションの生成

URLディスパッチ
------------------------------

- myapp2

  - __init__.py
  - wsgi.py
  - views.py

.. literalinclude:: myapp2/__init__.py
   :language: python
   :caption: __init__.py: add_routeでURLパターン登録

.. literalinclude:: myapp2/views.py
   :language: python
   :caption: views.py: view_configによるroute割り当て


wsgi.pyはmyapp1と同じ


HTMLテンプレート
--------------------------------

pyramid_jinja2をインストール::

  pip wheel pyramid_jinja2 -f wheelhouse
  pip install pyramid_jinja2 -f wheelhouse

- myapp3

  - __init__.py
  - wsgi.py
  - views.py
  - templates

    - index.jinja2
    - user.jinja2

.. literalinclude:: myapp3/__init__.py
   :language: python
   :caption: __init__.py: pyramid_jinja2 を include

.. literalinclude:: myapp3/views.py
   :language: python
   :caption: views.py: view_configのrendererでテンプレートを指定

.. literalinclude:: myapp3/templates/index.jinja2
   :language: html
   :caption: テンプレート

.. literalinclude:: myapp3/templates/user.jinja2
   :caption: ビューから渡された値(username) をテンプレート内で使用

データベースアクセス
--------------------------------

pyramid_sqlalchemyとpyramid_tmのインストール::

   pip wheel -f wheelhouse pyramid_sqlalchemy pyramid_tm
   pip install -f wheelhouse pyramid_sqlalchemy pyramid_tm

- myapp4

  - __init__.py
  - wsgi.py
  - models.py
  - views.py
  - templates

    - index.jinja2
    - user.jinja2

.. literalinclude:: myapp4/__init__.py
   :language: python
   :caption: __init__.py: pyramid_sqlalchemy, pyramid_tm を include

.. literalinclude:: myapp4/wsgi.py
   :language: python
   :caption: __init__.py: sqlalchemy.url にデータベース接続を設定

.. literalinclude:: myapp4/models.py
   :language: python
   :caption: モデル定義

.. literalinclude:: myapp4/views.py
   :language: python
   :caption: views.py: User.query でデータベースからモデルを取得

.. literalinclude:: myapp4/templates/user.jinja2
   :caption: ビューから渡されたuserのプロパティアクセス


データベース、テーブル作成::

   >>> from myapp4 import main
   >>> import os
   >>> here = os.getcwd()
   >>> main({}, **{'sqlalchemy.url': 'sqlite:///{here}/myapp4.sqlite'.format(here=here)}
   >>> from myapp4 import models
   >>> models.BaseObject.metadata.create_all()

データ投入::

   >>> user = models.User(username="aodag")
   >>> models.Session.add(user)
   >>> models.Session.flush()
   >>> import transaction
   >>> transaction.commit()
   >>> models.User.query.all()

データ作成とフォーム
------------------------------------

pyramid_deform colanderalchemy のインストール::

  pip wheel -f wheelhouse "deform>=2.0dev" pyramid_deform colanderalchemy

- myapp5

  - __init__.py
  - wsgi.py
  - models.py
  - views.py
  - templates

    - index.jinja2
    - new_user.jinja2
    - users.jinja2
    - user.jinja2


.. literalinclude:: myapp5/__init__.py
   :language: python
   :caption: __init__.py: pyramid_deform を include

.. literalinclude:: myapp5/views.py
   :language: python
   :caption: views.py: FormViewを使ってdeformを使うビューを定義

.. literalinclude:: myapp5/templates/new_user.jinja2
   :caption: フォームの表示


レイアウトとスタイル
-----------------------------------

pyramid_layout のインストール::

  pip wheel -f wheelhouse pyramid_layout
  pip install -f wheelhouse pyramid_layout

- myapp6

  - __init__.py
  - wsgi.py
  - models.py
  - views.py
  - layouts.py
  - templates

    - base.jinja2
    - index.jinja2
    - new_user.jinja2
    - users.jinja2
    - user.jinja2

.. literalinclude:: myapp6/__init__.py
   :language: python
   :caption: __init__.py: pyramid_layout を include

.. literalinclude:: myapp6/layouts.py
   :language: python
   :caption: layouts.py: BaseLayoutを定義

.. literalinclude:: myapp6/templates/base.jinja2
   :caption: BaseLayoutで使うレイアウト

.. literalinclude:: myapp6/templates/index.jinja2
   :caption: レイアウトで提供されるテンプレートを継承する(その他のテンプレートでも同様)


スキーママイグレーション
--------------------------------------

- myapp7

  - __init__.py
  - wsgi.py
  - models.py
  - views.py
  - layouts.py
  - templates

    - base.jinja2
    - index.jinja2
    - new_user.jinja2
    - users.jinja2
    - user.jinja2


alembicのインストール::

  pip wheel -f wheelhouse alembic
  pip install -f wheelhouse alembic

マイグレーションの初期化::

  alembic init alembic

.. literalinclude:: alembic.ini
   :language: ini
   :caption: マイグレーション設定 sqlalchemy.url に接続文字列を設定する

.. literalinclude:: alembic/env.py
   :language: python
   :caption: alembic/env.py の target_schemaにアプリケーションモデルのmetadataを設定
   :lines: 18-19

初期のスキーマリビジョンを作成::

  alembic revision --autogenerate -m "first models"

スキーマをデータベースに反映::

  alembic upgrade head
  alembic history

.. literalinclude:: myapp7/models.py
   :caption: models.py: モデルに項目(birthday) 追加

追加した項目分のリビジョンを作成::

  alembic revision --autogenerate -m "user birthday"


追加したリビジョンをデータベースに反映::

  alembic upgrade head
  alembic history
