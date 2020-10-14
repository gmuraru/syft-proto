# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/frameworks/torch/tensors/interpreters/v1/precision.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft_proto.types.syft.v1 import id_pb2 as syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2
from syft_proto.frameworks.torch.tensors.interpreters.v1 import additive_shared_pb2 as syft__proto_dot_frameworks_dot_torch_dot_tensors_dot_interpreters_dot_v1_dot_additive__shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/frameworks/torch/tensors/interpreters/v1/precision.proto',
  package='syft_proto.frameworks.torch.tensors.interpreters.v1',
  syntax='proto3',
  serialized_options=b'\n@org.openmined.syftproto.frameworks.torch.tensors.interpreters.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCsyft_proto/frameworks/torch/tensors/interpreters/v1/precision.proto\x12\x33syft_proto.frameworks.torch.tensors.interpreters.v1\x1a!syft_proto/types/syft/v1/id.proto\x1aIsyft_proto/frameworks/torch/tensors/interpreters/v1/additive_shared.proto\"\xe5\x02\n\x14\x46ixedPrecisionTensor\x12,\n\x02id\x18\x01 \x01(\x0b\x32\x1c.syft_proto.types.syft.v1.IdR\x02id\x12\x14\n\x05\x66ield\x18\x03 \x01(\tR\x05\x66ield\x12\x14\n\x05\x64type\x18\x04 \x01(\tR\x05\x64type\x12\x12\n\x04\x62\x61se\x18\x05 \x01(\x05R\x04\x62\x61se\x12\x14\n\x05kappa\x18\x06 \x01(\x05R\x05kappa\x12\x31\n\x14precision_fractional\x18\x07 \x01(\x05R\x13precisionFractional\x12\x12\n\x04tags\x18\x08 \x03(\tR\x04tags\x12 \n\x0b\x64\x65scription\x18\t \x01(\tR\x0b\x64\x65scription\x12`\n\x05\x63hild\x18\n \x01(\x0b\x32J.syft_proto.frameworks.torch.tensors.interpreters.v1.AdditiveSharingTensorR\x05\x63hildBB\n@org.openmined.syftproto.frameworks.torch.tensors.interpreters.v1b\x06proto3'
  ,
  dependencies=[syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2.DESCRIPTOR,syft__proto_dot_frameworks_dot_torch_dot_tensors_dot_interpreters_dot_v1_dot_additive__shared__pb2.DESCRIPTOR,])




_FIXEDPRECISIONTENSOR = _descriptor.Descriptor(
  name='FixedPrecisionTensor',
  full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.field', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='field', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.dtype', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dtype', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.base', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='base', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kappa', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.kappa', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='kappa', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='precision_fractional', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.precision_fractional', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='precisionFractional', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.tags', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.description', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child', full_name='syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor.child', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='child', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=235,
  serialized_end=592,
)

_FIXEDPRECISIONTENSOR.fields_by_name['id'].message_type = syft__proto_dot_types_dot_syft_dot_v1_dot_id__pb2._ID
_FIXEDPRECISIONTENSOR.fields_by_name['child'].message_type = syft__proto_dot_frameworks_dot_torch_dot_tensors_dot_interpreters_dot_v1_dot_additive__shared__pb2._ADDITIVESHARINGTENSOR
DESCRIPTOR.message_types_by_name['FixedPrecisionTensor'] = _FIXEDPRECISIONTENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FixedPrecisionTensor = _reflection.GeneratedProtocolMessageType('FixedPrecisionTensor', (_message.Message,), {
  'DESCRIPTOR' : _FIXEDPRECISIONTENSOR,
  '__module__' : 'syft_proto.frameworks.torch.tensors.interpreters.v1.precision_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.frameworks.torch.tensors.interpreters.v1.FixedPrecisionTensor)
  })
_sym_db.RegisterMessage(FixedPrecisionTensor)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
