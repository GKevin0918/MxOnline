# -*- encoding: utf-8 -*-
# _author_ = 'Kevin'
# _date_ = '2017/8/14 下午1:40'

import xadmin
from xadmin import views

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


# xadmin配置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "Anqin Normal University"
    menu_style = "accordion"


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
