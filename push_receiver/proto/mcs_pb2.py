# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mcs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tmcs.proto\x12\tmcs_proto"S\n\rHeartbeatPing\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x12\x1f\n\x17last_stream_id_received\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x03"R\n\x0cHeartbeatAck\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x12\x1f\n\x17last_stream_id_received\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x03"a\n\tErrorInfo\x12\x0c\n\x04\x63ode\x18\x01 \x02(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\'\n\textension\x18\x04 \x01(\x0b\x32\x14.mcs_proto.Extension"&\n\x07Setting\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t"A\n\rHeartbeatStat\x12\n\n\x02ip\x18\x01 \x02(\t\x12\x0f\n\x07timeout\x18\x02 \x02(\x08\x12\x13\n\x0binterval_ms\x18\x03 \x02(\x05"G\n\x0fHeartbeatConfig\x12\x13\n\x0bupload_stat\x18\x01 \x01(\x08\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x13\n\x0binterval_ms\x18\x03 \x01(\x05"\xdb\x02\n\x0b\x43lientEvent\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.mcs_proto.ClientEvent.Type\x12\x1f\n\x17number_discarded_events\x18\x64 \x01(\r\x12\x15\n\x0cnetwork_type\x18\xc8\x01 \x01(\x05\x12#\n\x1atime_connection_started_ms\x18\xca\x01 \x01(\x04\x12!\n\x18time_connection_ended_ms\x18\xcb\x01 \x01(\x04\x12\x13\n\nerror_code\x18\xcc\x01 \x01(\x05\x12\'\n\x1etime_connection_established_ms\x18\xac\x02 \x01(\x04"[\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10\x44ISCARDED_EVENTS\x10\x01\x12\x15\n\x11\x46\x41ILED_CONNECTION\x10\x02\x12\x19\n\x15SUCCESSFUL_CONNECTION\x10\x03J\x06\x08\xc9\x01\x10\xca\x01"\xff\x03\n\x0cLoginRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0e\n\x06\x64omain\x18\x02 \x02(\t\x12\x0c\n\x04user\x18\x03 \x02(\t\x12\x10\n\x08resource\x18\x04 \x02(\t\x12\x12\n\nauth_token\x18\x05 \x02(\t\x12\x11\n\tdevice_id\x18\x06 \x01(\t\x12\x13\n\x0blast_rmq_id\x18\x07 \x01(\x03\x12#\n\x07setting\x18\x08 \x03(\x0b\x32\x12.mcs_proto.Setting\x12\x1e\n\x16received_persistent_id\x18\n \x03(\t\x12\x1a\n\x12\x61\x64\x61ptive_heartbeat\x18\x0c \x01(\x08\x12\x30\n\x0eheartbeat_stat\x18\r \x01(\x0b\x32\x18.mcs_proto.HeartbeatStat\x12\x10\n\x08use_rmq2\x18\x0e \x01(\x08\x12\x12\n\naccount_id\x18\x0f \x01(\x03\x12\x39\n\x0c\x61uth_service\x18\x10 \x01(\x0e\x32#.mcs_proto.LoginRequest.AuthService\x12\x14\n\x0cnetwork_type\x18\x11 \x01(\x05\x12\x0e\n\x06status\x18\x12 \x01(\x03\x12,\n\x0c\x63lient_event\x18\x16 \x03(\x0b\x32\x16.mcs_proto.ClientEvent"\x1d\n\x0b\x41uthService\x12\x0e\n\nANDROID_ID\x10\x02J\x04\x08\x13\x10\x14J\x04\x08\x14\x10\x15J\x04\x08\x15\x10\x16"\xf6\x01\n\rLoginResponse\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0b\n\x03jid\x18\x02 \x01(\t\x12#\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x14.mcs_proto.ErrorInfo\x12#\n\x07setting\x18\x04 \x03(\x0b\x32\x12.mcs_proto.Setting\x12\x11\n\tstream_id\x18\x05 \x01(\x05\x12\x1f\n\x17last_stream_id_received\x18\x06 \x01(\x05\x12\x34\n\x10heartbeat_config\x18\x07 \x01(\x0b\x32\x1a.mcs_proto.HeartbeatConfig\x12\x18\n\x10server_timestamp\x18\x08 \x01(\x03"/\n\x11StreamErrorStanza\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x0c\n\x04text\x18\x02 \x01(\t"\x07\n\x05\x43lose"%\n\tExtension\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c"\xdd\x02\n\x08IqStanza\x12\x0e\n\x06rmq_id\x18\x01 \x01(\x03\x12(\n\x04type\x18\x02 \x02(\x0e\x32\x1a.mcs_proto.IqStanza.IqType\x12\n\n\x02id\x18\x03 \x02(\t\x12\x0c\n\x04\x66rom\x18\x04 \x01(\t\x12\n\n\x02to\x18\x05 \x01(\t\x12#\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x14.mcs_proto.ErrorInfo\x12\'\n\textension\x18\x07 \x01(\x0b\x32\x14.mcs_proto.Extension\x12\x15\n\rpersistent_id\x18\x08 \x01(\t\x12\x11\n\tstream_id\x18\t \x01(\x05\x12\x1f\n\x17last_stream_id_received\x18\n \x01(\x05\x12\x12\n\naccount_id\x18\x0b \x01(\x03\x12\x0e\n\x06status\x18\x0c \x01(\x03"4\n\x06IqType\x12\x07\n\x03GET\x10\x00\x12\x07\n\x03SET\x10\x01\x12\n\n\x06RESULT\x10\x02\x12\x0c\n\x08IQ_ERROR\x10\x03"%\n\x07\x41ppData\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t"\xf4\x02\n\x11\x44\x61taMessageStanza\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04\x66rom\x18\x03 \x02(\t\x12\n\n\x02to\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x05 \x02(\t\x12\r\n\x05token\x18\x06 \x01(\t\x12$\n\x08\x61pp_data\x18\x07 \x03(\x0b\x32\x12.mcs_proto.AppData\x12\x1b\n\x13\x66rom_trusted_server\x18\x08 \x01(\x08\x12\x15\n\rpersistent_id\x18\t \x01(\t\x12\x11\n\tstream_id\x18\n \x01(\x05\x12\x1f\n\x17last_stream_id_received\x18\x0b \x01(\x05\x12\x0e\n\x06reg_id\x18\r \x01(\t\x12\x16\n\x0e\x64\x65vice_user_id\x18\x10 \x01(\x03\x12\x0b\n\x03ttl\x18\x11 \x01(\x05\x12\x0c\n\x04sent\x18\x12 \x01(\x03\x12\x0e\n\x06queued\x18\x13 \x01(\x05\x12\x0e\n\x06status\x18\x14 \x01(\x03\x12\x10\n\x08raw_data\x18\x15 \x01(\x0c\x12\x15\n\rimmediate_ack\x18\x18 \x01(\x08"\x0b\n\tStreamAck"\x1a\n\x0cSelectiveAck\x12\n\n\x02id\x18\x01 \x03(\tB\x02H\x03'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "mcs_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"H\003"
    _globals["_HEARTBEATPING"]._serialized_start = 24
    _globals["_HEARTBEATPING"]._serialized_end = 107
    _globals["_HEARTBEATACK"]._serialized_start = 109
    _globals["_HEARTBEATACK"]._serialized_end = 191
    _globals["_ERRORINFO"]._serialized_start = 193
    _globals["_ERRORINFO"]._serialized_end = 290
    _globals["_SETTING"]._serialized_start = 292
    _globals["_SETTING"]._serialized_end = 330
    _globals["_HEARTBEATSTAT"]._serialized_start = 332
    _globals["_HEARTBEATSTAT"]._serialized_end = 397
    _globals["_HEARTBEATCONFIG"]._serialized_start = 399
    _globals["_HEARTBEATCONFIG"]._serialized_end = 470
    _globals["_CLIENTEVENT"]._serialized_start = 473
    _globals["_CLIENTEVENT"]._serialized_end = 820
    _globals["_CLIENTEVENT_TYPE"]._serialized_start = 721
    _globals["_CLIENTEVENT_TYPE"]._serialized_end = 812
    _globals["_LOGINREQUEST"]._serialized_start = 823
    _globals["_LOGINREQUEST"]._serialized_end = 1334
    _globals["_LOGINREQUEST_AUTHSERVICE"]._serialized_start = 1287
    _globals["_LOGINREQUEST_AUTHSERVICE"]._serialized_end = 1316
    _globals["_LOGINRESPONSE"]._serialized_start = 1337
    _globals["_LOGINRESPONSE"]._serialized_end = 1583
    _globals["_STREAMERRORSTANZA"]._serialized_start = 1585
    _globals["_STREAMERRORSTANZA"]._serialized_end = 1632
    _globals["_CLOSE"]._serialized_start = 1634
    _globals["_CLOSE"]._serialized_end = 1641
    _globals["_EXTENSION"]._serialized_start = 1643
    _globals["_EXTENSION"]._serialized_end = 1680
    _globals["_IQSTANZA"]._serialized_start = 1683
    _globals["_IQSTANZA"]._serialized_end = 2032
    _globals["_IQSTANZA_IQTYPE"]._serialized_start = 1980
    _globals["_IQSTANZA_IQTYPE"]._serialized_end = 2032
    _globals["_APPDATA"]._serialized_start = 2034
    _globals["_APPDATA"]._serialized_end = 2071
    _globals["_DATAMESSAGESTANZA"]._serialized_start = 2074
    _globals["_DATAMESSAGESTANZA"]._serialized_end = 2446
    _globals["_STREAMACK"]._serialized_start = 2448
    _globals["_STREAMACK"]._serialized_end = 2459
    _globals["_SELECTIVEACK"]._serialized_start = 2461
    _globals["_SELECTIVEACK"]._serialized_end = 2487
# @@protoc_insertion_point(module_scope)
