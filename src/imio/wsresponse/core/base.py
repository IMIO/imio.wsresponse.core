# encoding: utf-8

from App.config import getConfiguration


def get_config(key):
    config = getattr(getConfiguration(), 'product_config', {})
    package_config = config.get('imio.wsrequest.core')
    if package_config is None:
        raise ValueError('The config for the package is missing')
    return package_config.get(key, '')


class ResponseConsumer(object):

    @property
    def queue(self):
        client_id = get_config('client_id')
        return self.queuename.format(client_id)

    @property
    def routing_key(self):
        return get_config('routing_key')
