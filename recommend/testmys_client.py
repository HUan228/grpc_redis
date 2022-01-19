#-*-coding:utf-8-*
import asyncio
import json
import logging

import grpc
import test_pb2_grpc
import test_pb2
import  sys


async def run(name:str) -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.UserStorageStub(channel)
        response = await stub.AddSentence(test_pb2.CommonRequest(stu_name=name))
        print(response)
        response = await stub.Queryword(test_pb2.CommonRequest(stu_name="小李"))
        print(response.user_list)

if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run(sys.argv[1]))