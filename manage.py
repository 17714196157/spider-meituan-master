# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     manage
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""

from api.view import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(workers=3)
