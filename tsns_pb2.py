# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tsns.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tsns.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntsns.proto\"+\n\x05Login\x12\x10\n\x08Username\x18\x01 \x01(\t\x12\x10\n\x08Password\x18\x02 \x01(\t\"A\n\x0cToggleFollow\x12\x0e\n\x06Origin\x18\x01 \x01(\t\x12\x0e\n\x06Target\x18\x02 \x01(\t\x12\x11\n\tFollowing\x18\x03 \x01(\x08\"\x1a\n\x08ListUser\x12\x0e\n\x06Origin\x18\x01 \x01(\t\"5\n\nReturnList\x12\x14\n\x0c\x43urrentUsers\x18\x01 \x01(\t\x12\x11\n\tFollowers\x18\x02 \x01(\t\"2\n\x04Post\x12\x0e\n\x06Origin\x18\x01 \x01(\t\x12\x0c\n\x04Post\x18\x02 \x01(\t\x12\x0c\n\x04Time\x18\x03 \x01(\t2\xb2\x01\n\x18TinySocialNetworkService\x12(\n\x06\x46ollow\x12\r.ToggleFollow\x1a\r.ToggleFollow\"\x00\x12*\n\x08Unfollow\x12\r.ToggleFollow\x1a\r.ToggleFollow\"\x00\x12 \n\x04List\x12\t.ListUser\x1a\x0b.ReturnList\"\x00\x12\x1e\n\x08Timeline\x12\x05.Post\x1a\x05.Post\"\x00(\x01\x30\x01\x62\x06proto3')
)




_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Username', full_name='Login.Username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Password', full_name='Login.Password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=14,
  serialized_end=57,
)


_TOGGLEFOLLOW = _descriptor.Descriptor(
  name='ToggleFollow',
  full_name='ToggleFollow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Origin', full_name='ToggleFollow.Origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Target', full_name='ToggleFollow.Target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Following', full_name='ToggleFollow.Following', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=59,
  serialized_end=124,
)


_LISTUSER = _descriptor.Descriptor(
  name='ListUser',
  full_name='ListUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Origin', full_name='ListUser.Origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=126,
  serialized_end=152,
)


_RETURNLIST = _descriptor.Descriptor(
  name='ReturnList',
  full_name='ReturnList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='CurrentUsers', full_name='ReturnList.CurrentUsers', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Followers', full_name='ReturnList.Followers', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=154,
  serialized_end=207,
)


_POST = _descriptor.Descriptor(
  name='Post',
  full_name='Post',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Origin', full_name='Post.Origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Post', full_name='Post.Post', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Time', full_name='Post.Time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=209,
  serialized_end=259,
)

DESCRIPTOR.message_types_by_name['Login'] = _LOGIN
DESCRIPTOR.message_types_by_name['ToggleFollow'] = _TOGGLEFOLLOW
DESCRIPTOR.message_types_by_name['ListUser'] = _LISTUSER
DESCRIPTOR.message_types_by_name['ReturnList'] = _RETURNLIST
DESCRIPTOR.message_types_by_name['Post'] = _POST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN,
  __module__ = 'tsns_pb2'
  # @@protoc_insertion_point(class_scope:Login)
  ))
_sym_db.RegisterMessage(Login)

ToggleFollow = _reflection.GeneratedProtocolMessageType('ToggleFollow', (_message.Message,), dict(
  DESCRIPTOR = _TOGGLEFOLLOW,
  __module__ = 'tsns_pb2'
  # @@protoc_insertion_point(class_scope:ToggleFollow)
  ))
_sym_db.RegisterMessage(ToggleFollow)

ListUser = _reflection.GeneratedProtocolMessageType('ListUser', (_message.Message,), dict(
  DESCRIPTOR = _LISTUSER,
  __module__ = 'tsns_pb2'
  # @@protoc_insertion_point(class_scope:ListUser)
  ))
_sym_db.RegisterMessage(ListUser)

ReturnList = _reflection.GeneratedProtocolMessageType('ReturnList', (_message.Message,), dict(
  DESCRIPTOR = _RETURNLIST,
  __module__ = 'tsns_pb2'
  # @@protoc_insertion_point(class_scope:ReturnList)
  ))
_sym_db.RegisterMessage(ReturnList)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), dict(
  DESCRIPTOR = _POST,
  __module__ = 'tsns_pb2'
  # @@protoc_insertion_point(class_scope:Post)
  ))
_sym_db.RegisterMessage(Post)



_TINYSOCIALNETWORKSERVICE = _descriptor.ServiceDescriptor(
  name='TinySocialNetworkService',
  full_name='TinySocialNetworkService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=262,
  serialized_end=440,
  methods=[
  _descriptor.MethodDescriptor(
    name='Follow',
    full_name='TinySocialNetworkService.Follow',
    index=0,
    containing_service=None,
    input_type=_TOGGLEFOLLOW,
    output_type=_TOGGLEFOLLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Unfollow',
    full_name='TinySocialNetworkService.Unfollow',
    index=1,
    containing_service=None,
    input_type=_TOGGLEFOLLOW,
    output_type=_TOGGLEFOLLOW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='TinySocialNetworkService.List',
    index=2,
    containing_service=None,
    input_type=_LISTUSER,
    output_type=_RETURNLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Timeline',
    full_name='TinySocialNetworkService.Timeline',
    index=3,
    containing_service=None,
    input_type=_POST,
    output_type=_POST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TINYSOCIALNETWORKSERVICE)

DESCRIPTOR.services_by_name['TinySocialNetworkService'] = _TINYSOCIALNETWORKSERVICE

# @@protoc_insertion_point(module_scope)
