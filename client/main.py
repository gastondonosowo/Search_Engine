from flask import Flask, request, render_template  

import grpc
import redis
import re

import proto_message_pb2 as pb2_grpc
import proto_message_pb2_grpc as pb2

import time

app = Flask(__name__)
#r_actual = 0
r = redis.Redis(host="redis1", port=6379, db=0)
r.config_set('maxmemory-policy', 'allkeys-lru')
r.flushall()
a="""
r1 = redis.Redis(host="redis2", port=6380, db=0)
r1.config_set('maxmemory-policy', 'allkeys-lru')
r1.flushall()

r2 = redis.Redis(host="redis3", port=6381, db=0)
r2.config_set('maxmemory-policy', 'allkeys-lru')
r2.flushall()
"""
class SearchClient(object):

    def __init__(self):
        self.host = 'servidor'
        self.server_port = '50051'

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        self.stub = pb2.SearchStub(self.channel)

    def get_url(self, message):
        message = pb2_grpc.Message(message=message)
        stub = self.stub.GetServerResponse(message)
        return stub

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    client = SearchClient()
    search = request.args['search']
    cache = r.get(search)
   # cache1 = r1.get(search)
   # cache2 = r2.get(search)
    #if cache == None and cache1 == None and cache2 == None:
    if cache == None:
        item = client.get_url(message=search)
        r.set(search, str(item))
        #if r_actual == 0:
         #   r.set(search, str(item))
            #r_actual += 1
#        elif r_actual == 1:
 #           r1.set(search, str(item))
  #          r_actual += 1
   #     else:
    #        r2.set(search, str(item))
     #       r_actual = 0

        return render_template('index.html', datos = item, procedencia = "Datos sacados de PostgreSQL")
    
    else:
        if cache != None:
            item = cache.decode("utf-8")
            return render_template('index.html', datos = item, procedencia = "Datos sacados de Redis1")
 #       elif cache1 != None:
#            item = cache1.decode("utf-8")
  #          return render_template('index.html', datos = item, procedencia = "Datos sacados de Redis2")
  #      else:
  #          item = cache2.decode("utf-8")
  #3          return render_template('index.html', datos = item, procedencia = "Datos sacados de Redis3")
if __name__ == '__main__':
    time.sleep(25)