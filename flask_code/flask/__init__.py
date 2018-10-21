# -*- coding: utf-8 -*-
"""
    flask
    ~~~~~

    A microframework based on Werkzeug.  It's extensively documented
    and follows best practice patterns.

    :copyright: © 2010 by the Pallets team.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '1.1.dev'

# utilities we import from Werkzeug and Jinja2 that are unused
# in the module but are exported as public interface.
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from jinja2 import Markup, escape

from .app import Flask, Request, Response
# app.py 主要提供创建flask实例和对请求、响应进行处理的功能
from .config import Config
# confi.py 主要提供配置文件的功能
from .helpers import url_for, flash, send_file, send_from_directory, \
     get_flashed_messages, get_template_attribute, make_response, safe_join, \
     stream_with_context
# helpers.py 主要提供诸多辅助功能
from .globals import current_app, g, request, session, _request_ctx_stack, \
     _app_ctx_stack
# globals.py 主要提供全局变量、局部变量和上下文管理器的实例
from .ctx import has_request_context, has_app_context, \
     after_this_request, copy_current_request_context
# ctx.py 主要定义了上下文管理器的类
from .blueprints import Blueprint
# 提供蓝图的功能
from .templating import render_template, render_template_string
# templating.py 主要提供模板渲染的功能
# the signals
from .signals import signals_available, template_rendered, request_started, \
     request_finished, got_request_exception, request_tearing_down, \
     appcontext_tearing_down, appcontext_pushed, \
     appcontext_popped, message_flashed, before_render_template
# singles主要处理不同机制的信号实例
# We're not exposing the actual json module but a convenient wrapper around
# it.
from . import json
# json.py 主要提供json格式数据的解析功能

# This was the only thing that Flask used to export at one point and it had
# a more generic name.
jsonify = json.jsonify


# sessions.py 提供session的类定义 包含了cookie机制
# testing.py  定义用于测试而非生产的一些基类、函数等
# logging.py 定义了日志管理器的类和创建函数
# views.py 提供了另一种以类来定义视图函数的方式，不常用
# _compat.py 定义了对py2和py3的兼容 涉及到不同版本的对象 现在该文件中进行校验处理
#  
