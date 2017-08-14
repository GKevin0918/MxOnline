# -*- encoding: utf-8 -*-
# _author_ = 'Kevin'
# _date_ = '2017/8/14 下午1:40'

import xadmin

from .models import EmailVerifyRecord
from .models import Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']  # 搜索字段
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 过滤器


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']  # 搜索字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # 过滤器


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
