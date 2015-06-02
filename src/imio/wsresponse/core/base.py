# encoding: utf-8

from App.config import getConfiguration
from collective.zamqp.interfaces import IBrokerConnection
from five import grok
from pika import ConnectionParameters
from pika import PlainCredentials
from zope.component import getUtility


def get_config(key):
    config = getattr(getConfiguration(), 'product_config', {})
    package_config = config.get('imio.wsrequest.core')
    if package_config is None:
        raise ValueError('The config for the package is missing')
    return package_config.get(key, '')


def get_rabbitmq_connection():
    connection = getUtility(IBrokerConnection, name='ws.response')
    credentials = PlainCredentials(
        connection.username,
        connection.password,
        erase_on_connect=False,
    )
    parameters = ConnectionParameters(
        connection.hostname,
        connection.port,
        connection.virtual_host,
        credentials=credentials,
        heartbeat=True)
    parameters.heartbeat = connection.heartbeat
    return parameters


class ResponseConsumer(object):

    @property
    def queue(self):
        client_id = get_config('client_id')
        return self.queuename.format(client_id)

    @property
    def routing_key(self):
        return get_config('routing_key')


class Validator(grok.Adapter):

    def __init__(self, context):
        self.context = context

    def validate(self):
        raise NotImplementedError()
