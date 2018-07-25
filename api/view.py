# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     view
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
import asyncio
import logging

import aiohttp
from pyppeteer import launch
from sanic import Sanic
from sanic.blueprints import Blueprint
from sanic.response import json
from sanic.views import HTTPMethodView

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

default_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
}


async def send_request(session, method, url, headers, **kwargs):
    """
    :type session: aiohttp.ClientSession
    :param session:
    :param method:
    :param url:
    :param headers:
    :return:
    """
    proxy = "http://115.28.253.245:9020"
    proxy_auth = aiohttp.BasicAuth("H5H22B1742467O8D", "8A992F54C2E993F3")
    count = 0
    while True:
        if count > 3:
            return ''
        try:
            resp = await session.request(method=method, url=url, headers=headers, proxy=proxy, proxy_auth=proxy_auth,
                                         **kwargs)
            data = await resp.text()
        except Exception as e:
            count += 1
            continue
        else:
            return data


class RenderJs(HTTPMethodView):
    async def post(self, request, *args, **kwargs):
        method = request.json.get('method', "GET")
        url = request.json.get('url')
        headers = request.json.get('headers', default_headers)
        script = request.json.get('script')
        cookies = request.json.get('cookies', {"_lxsdk_s": "%7C%7C0"})
        others = request.json.get('kwargs', {})
        page = None
        try:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                html = await send_request(session, method, url, headers, **others)
            page = await request.app.browser.newPage()
            await asyncio.sleep(0.2)
            await page.goto('data:text/html,{}'.format(html), options={'timeout': 20000})
            # await page.screenshot({'path': 'example.png'})
            result = await page.evaluate(script)
        except Exception as e:
            logger.exception(e)
            return json({"result": "", "code": 0})
        finally:
            if page:
                await page.close()
        return json({"result": result, "code": 1})


api_blueprint = Blueprint("api")

api_blueprint.add_route(RenderJs.as_view(), uri="/render/js", methods=["POST"])


def listeners(app):
    @app.listener('before_server_start')
    async def open_browser(app, loop):
        app.browser = await launch()

    @app.listener('before_server_stop')
    async def server_stop(app, loop):
        await app.browser.close()


def create_app():
    app = Sanic("render")
    app.blueprint(api_blueprint)
    listeners(app)
    return app
