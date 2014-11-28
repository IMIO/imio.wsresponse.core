# encoding: utf-8

from imio.amqp import BaseSingleMessagePublisher

from imio.wsresponse.core.base import get_rabbitmq_connection


class ResponsePublisher(BaseSingleMessagePublisher):
    logger_name = 'response_notifier'
    log_file = 'response_notifier.log'
    exchange = 'ws.response'

    def __init__(self, logging=True):
        super(ResponsePublisher, self).__init__('', logging=logging)

    @property
    def url_parameters(self):
        return get_rabbitmq_connection()

    def get_routing_key(self, message):
        return message.uid
