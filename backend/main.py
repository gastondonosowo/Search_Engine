import grpc
from concurrent import futures
import proto_message_pb2 as pb2
import proto_message_pb2_grpc as pb2_grpc
from psycopg2 import connect

class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        item = []
        response = []
        message = request.message
        result = f'"{message}" '
        query = "SELECT DISTINCT title,description,web FROM T1 WHERE keywords LIKE '%"+message+"%' limit 10;"
        cursor.execute(query)
        query_res = cursor.fetchall()
        for row in query_res:
            item.append(row)
        for i in item:
            result = dict()
            result['url']= i[2]
            result['title'] = i[0]
            result['description']= i[1]
            response.append(result)
        
        return pb2.SearchResults(web=response)

def serve():# Iniciar un servidor gRPC para que los clientes puedan usar su servicio
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

conn = connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host='postgres'
       )
       
if __name__ == '__main__':
    cursor = conn.cursor()
    serve()
