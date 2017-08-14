# -*- encoding: utf-8 -*-
# _author_ = 'Kevin'
# _date_ = '2017/8/14 下午1:40'

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
