# coding=utf-8
from concurrent import futures
import redis
import grpc
import test_pb2
import test_pb2_grpc



class UserService(test_pb2_grpc.UserStorageServicer):
    def get_client(self):
        #client = redis.Redis(decode_responses=True, host="101.32.216.118")
        client = redis.Redis(decode_responses=True)
        return client


    def AddSentence(self, request, context):
        name = request.stu_name
        print(request)
        for i in range(len(name)):
            # print(len(name))
            # print(i)
            key = "autocomplete" + name[:i+1]
            print(key)
            result = self.get_client().incr(name[:i+1], 10)
            print(result)
            # result = self.get_client().zincrby(key, 10, name)
            # print(result)
        return test_pb2.CommonReply(code=0, message="success")

    def Queryword(self, request, context):
        count = 50
        prefix = request.stu_name
        key = "autocomplete" + prefix
        result = self.get_client().zrange(key, 0, count-1)
        print(result)
        return test_pb2.QueryReply(user_list=result, code=0, message="success")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_UserStorageServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
