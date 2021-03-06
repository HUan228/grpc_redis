# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class UserStorageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Queryword = channel.unary_unary(
                '/grpc_redis.UserStorage/Queryword',
                request_serializer=test__pb2.CommonRequest.SerializeToString,
                response_deserializer=test__pb2.QueryReply.FromString,
                )
        self.AddSentence = channel.unary_unary(
                '/grpc_redis.UserStorage/AddSentence',
                request_serializer=test__pb2.CommonRequest.SerializeToString,
                response_deserializer=test__pb2.CommonReply.FromString,
                )


class UserStorageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Queryword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSentence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserStorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Queryword': grpc.unary_unary_rpc_method_handler(
                    servicer.Queryword,
                    request_deserializer=test__pb2.CommonRequest.FromString,
                    response_serializer=test__pb2.QueryReply.SerializeToString,
            ),
            'AddSentence': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSentence,
                    request_deserializer=test__pb2.CommonRequest.FromString,
                    response_serializer=test__pb2.CommonReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_redis.UserStorage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserStorage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Queryword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_redis.UserStorage/Queryword',
            test__pb2.CommonRequest.SerializeToString,
            test__pb2.QueryReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSentence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_redis.UserStorage/AddSentence',
            test__pb2.CommonRequest.SerializeToString,
            test__pb2.CommonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
