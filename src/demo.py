from bottle import default_app, response, route
import os
import json
import redis


REDIS_HOST = os.environ['REDIS_HOST']
redis_db = redis.Redis(host=REDIS_HOST, port=6379, db=0)


@route('/redis-check')
def redis_check():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    info = redis_db.info()
    if info is not None:
        return redis_db.info()
    response.status = 500
    return 'Failed Redis Connection'    


@route('/add/<key>=<value>')
def add(key, value):
    redis_db.set(key, value)
    return f'Key-Value: {key}:{value} has been added.'


@route('/remove/<key>')
def remove(key):
    value = redis_db.get(key)
    if value is not None:
        redis_db.delete(key)
        return f'{key}:{value} has been deleted.'
    return f'Key:{key} not found.'


@route('/list/keys')
def list_keys():
    redis_keys = [key.decode('utf-8') for key in redis_db.keys('*')]
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(redis_keys)


@route('/list/key-values')
def list_key_values():
    redis_keys = [key.decode('utf-8') for key in redis_db.keys('*')]
    key_values = dict()
    for key in redis_keys:
        value = redis_db.get(key)
        key_values[key] = value.decode('utf-8')
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(key_values)


app = default_app()
