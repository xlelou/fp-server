# -*- coding:utf-8 -*-

from tbag.utils.routes import route
from utils.web import WebHandler
from service.spider.spider import spider_srv
from service.proxy.proxy import proxy_srv


@route(r'/api/status/$')
class Status(WebHandler):
    """
    get current status
    """

    async def get(self, *args, **kwargs):

        proxy_status = await proxy_srv.get_all_status()
        spider_data = await spider_srv.all_status()
        ret = {
            "running_spiders": spider_data,
            "stored_proxies": proxy_status,
        }
        self.do_success(ret)
