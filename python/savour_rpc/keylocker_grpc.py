# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: savour_rpc/keylocker.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import savour_rpc.keylocker_pb2


class LeyLockerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def getSupportChain(self, stream: 'grpclib.server.Stream[savour_rpc.keylocker_pb2.SupportChainReq, savour_rpc.keylocker_pb2.SupportChainRep]') -> None:
        pass

    @abc.abstractmethod
    async def setSocialKey(self, stream: 'grpclib.server.Stream[savour_rpc.keylocker_pb2.SetSocialKeyReq, savour_rpc.keylocker_pb2.SetSocialKeyRep]') -> None:
        pass

    @abc.abstractmethod
    async def getSocialKey(self, stream: 'grpclib.server.Stream[savour_rpc.keylocker_pb2.GetSocialKeyReq, savour_rpc.keylocker_pb2.GetSocialKeyRep]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/savour_rpc.keylocker.LeyLockerService/getSupportChain': grpclib.const.Handler(
                self.getSupportChain,
                grpclib.const.Cardinality.UNARY_UNARY,
                savour_rpc.keylocker_pb2.SupportChainReq,
                savour_rpc.keylocker_pb2.SupportChainRep,
            ),
            '/savour_rpc.keylocker.LeyLockerService/setSocialKey': grpclib.const.Handler(
                self.setSocialKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                savour_rpc.keylocker_pb2.SetSocialKeyReq,
                savour_rpc.keylocker_pb2.SetSocialKeyRep,
            ),
            '/savour_rpc.keylocker.LeyLockerService/getSocialKey': grpclib.const.Handler(
                self.getSocialKey,
                grpclib.const.Cardinality.UNARY_UNARY,
                savour_rpc.keylocker_pb2.GetSocialKeyReq,
                savour_rpc.keylocker_pb2.GetSocialKeyRep,
            ),
        }


class LeyLockerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.getSupportChain = grpclib.client.UnaryUnaryMethod(
            channel,
            '/savour_rpc.keylocker.LeyLockerService/getSupportChain',
            savour_rpc.keylocker_pb2.SupportChainReq,
            savour_rpc.keylocker_pb2.SupportChainRep,
        )
        self.setSocialKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/savour_rpc.keylocker.LeyLockerService/setSocialKey',
            savour_rpc.keylocker_pb2.SetSocialKeyReq,
            savour_rpc.keylocker_pb2.SetSocialKeyRep,
        )
        self.getSocialKey = grpclib.client.UnaryUnaryMethod(
            channel,
            '/savour_rpc.keylocker.LeyLockerService/getSocialKey',
            savour_rpc.keylocker_pb2.GetSocialKeyReq,
            savour_rpc.keylocker_pb2.GetSocialKeyRep,
        )
