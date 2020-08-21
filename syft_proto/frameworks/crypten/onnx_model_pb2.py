# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/frameworks/crypten/onnx_model.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/frameworks/crypten/onnx_model.proto',
  package='syft_proto.frameworks.torch.tensors.interpreters.v1',
  syntax='proto3',
  serialized_options=b'\n@org.openmined.syftproto.frameworks.torch.tensors.interpreters.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.syft_proto/frameworks/crypten/onnx_model.proto\x12\x33syft_proto.frameworks.torch.tensors.interpreters.v1\x1a!syft_proto/types/syft/v1/id.proto\"\x9a\x01\n\tOnnxModel\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12)\n\x10serialized_model\x18\x02 \x01(\x0cR\x0fserializedModel\x12\x12\n\x04tags\x18\x03 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scriptionBB\n@org.openmined.syftproto.frameworks.torch.tensors.interpreters.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,])




_ONNXMODEL = _descriptor.Descriptor(
  name='OnnxModel',
  full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.OnnxModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.OnnxModel.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialized_model', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.OnnxModel.serialized_model', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serializedModel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.OnnxModel.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.OnnxModel.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=293,
)

_ONNXMODEL.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
DESCRIPTOR.message_types_by_name['OnnxModel'] = _ONNXMODEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OnnxModel = _reflection.GeneratedProtocolMessageType('OnnxModel', (_message.Message,), {
  'DESCRIPTOR' : _ONNXMODEL,
  '__module__' : 'syft_proto.frameworks.crypten.onnx_model_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.frameworks.torch.tensors.interpreters.v1.OnnxModel)
  })
_sym_db.RegisterMessage(OnnxModel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)