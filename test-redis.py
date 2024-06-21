import redis
from time import sleep

client = redis.Redis(host='127.0.0.1')

client.set('Language', 'Python')
print(client.get('Language'))

client.set('Language', 'Python', ex=5)
print(client.get('Language'))
# sleep(3)
print(client.ttl('Language'))

client.sadd('pythonlist', 'value1', 'value2', 'value3')
client.sadd('pythonlist', 'value5', 'value6', 'value7')
print(client.smembers('pythonlist'))
client.sadd('redislist', 'value10', 'value5', 'value1', 'value17', 'value18')
print("sinter", client.sinter('pythonlist', 'redislist'))
print("sunion", client.sunion('pythonlist', 'redislist'))
print(client.scard('pythonlist'))

client.hset('Person', 'Name', 'Person1')
client.hset('Person', 'Health', '600')
client.hset('Person', 'Mana', '200')
print(client.hgetall('Person'))
