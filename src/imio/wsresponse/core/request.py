# encoding: utf-8

from collective.zamqp.consumer import Consumer
from five import grok

from imio.wsresponse.core import interfaces
from imio.wsresponse.core.base import ResponseConsumer


class Request(ResponseConsumer, Consumer):
    grok.name('ws.request')
    connection_id = 'ws.request'
    exchange = 'ws.request'
    marker = interfaces.IResponse
    queuename = 'application.type.{0}'
