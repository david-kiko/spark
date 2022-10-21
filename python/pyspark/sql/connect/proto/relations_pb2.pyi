#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import pyspark.sql.connect.proto.expressions_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Relation(google.protobuf.message.Message):
    """The main [[Relation]] type. Fundamentally, a relation is a typed container
    that has exactly one explicit relation type set.

    When adding new relation types, they have to be registered here.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMON_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    JOIN_FIELD_NUMBER: builtins.int
    UNION_FIELD_NUMBER: builtins.int
    SORT_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    SQL_FIELD_NUMBER: builtins.int
    LOCAL_RELATION_FIELD_NUMBER: builtins.int
    SAMPLE_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    DEDUPLICATE_FIELD_NUMBER: builtins.int
    UNKNOWN_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___RelationCommon: ...
    @property
    def read(self) -> global___Read: ...
    @property
    def project(self) -> global___Project: ...
    @property
    def filter(self) -> global___Filter: ...
    @property
    def join(self) -> global___Join: ...
    @property
    def union(self) -> global___Union: ...
    @property
    def sort(self) -> global___Sort: ...
    @property
    def limit(self) -> global___Limit: ...
    @property
    def aggregate(self) -> global___Aggregate: ...
    @property
    def sql(self) -> global___SQL: ...
    @property
    def local_relation(self) -> global___LocalRelation: ...
    @property
    def sample(self) -> global___Sample: ...
    @property
    def offset(self) -> global___Offset: ...
    @property
    def deduplicate(self) -> global___Deduplicate: ...
    @property
    def unknown(self) -> global___Unknown: ...
    def __init__(
        self,
        *,
        common: global___RelationCommon | None = ...,
        read: global___Read | None = ...,
        project: global___Project | None = ...,
        filter: global___Filter | None = ...,
        join: global___Join | None = ...,
        union: global___Union | None = ...,
        sort: global___Sort | None = ...,
        limit: global___Limit | None = ...,
        aggregate: global___Aggregate | None = ...,
        sql: global___SQL | None = ...,
        local_relation: global___LocalRelation | None = ...,
        sample: global___Sample | None = ...,
        offset: global___Offset | None = ...,
        deduplicate: global___Deduplicate | None = ...,
        unknown: global___Unknown | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "aggregate",
            b"aggregate",
            "common",
            b"common",
            "deduplicate",
            b"deduplicate",
            "filter",
            b"filter",
            "join",
            b"join",
            "limit",
            b"limit",
            "local_relation",
            b"local_relation",
            "offset",
            b"offset",
            "project",
            b"project",
            "read",
            b"read",
            "rel_type",
            b"rel_type",
            "sample",
            b"sample",
            "sort",
            b"sort",
            "sql",
            b"sql",
            "union",
            b"union",
            "unknown",
            b"unknown",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "aggregate",
            b"aggregate",
            "common",
            b"common",
            "deduplicate",
            b"deduplicate",
            "filter",
            b"filter",
            "join",
            b"join",
            "limit",
            b"limit",
            "local_relation",
            b"local_relation",
            "offset",
            b"offset",
            "project",
            b"project",
            "read",
            b"read",
            "rel_type",
            b"rel_type",
            "sample",
            b"sample",
            "sort",
            b"sort",
            "sql",
            b"sql",
            "union",
            b"union",
            "unknown",
            b"unknown",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["rel_type", b"rel_type"]
    ) -> typing_extensions.Literal[
        "read",
        "project",
        "filter",
        "join",
        "union",
        "sort",
        "limit",
        "aggregate",
        "sql",
        "local_relation",
        "sample",
        "offset",
        "deduplicate",
        "unknown",
    ] | None: ...

global___Relation = Relation

class Unknown(google.protobuf.message.Message):
    """Used for testing purposes only."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Unknown = Unknown

class RelationCommon(google.protobuf.message.Message):
    """Common metadata of all relations."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_INFO_FIELD_NUMBER: builtins.int
    ALIAS_FIELD_NUMBER: builtins.int
    source_info: builtins.str
    alias: builtins.str
    def __init__(
        self,
        *,
        source_info: builtins.str = ...,
        alias: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["alias", b"alias", "source_info", b"source_info"],
    ) -> None: ...

global___RelationCommon = RelationCommon

class SQL(google.protobuf.message.Message):
    """Relation that uses a SQL query to generate the output."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERY_FIELD_NUMBER: builtins.int
    query: builtins.str
    def __init__(
        self,
        *,
        query: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["query", b"query"]) -> None: ...

global___SQL = SQL

class Read(google.protobuf.message.Message):
    """Relation that reads from a file / table or other data source. Does not have additional
    inputs.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class NamedTable(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        UNPARSED_IDENTIFIER_FIELD_NUMBER: builtins.int
        unparsed_identifier: builtins.str
        def __init__(
            self,
            *,
            unparsed_identifier: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["unparsed_identifier", b"unparsed_identifier"],
        ) -> None: ...

    class DataSource(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class OptionsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            value: builtins.str
            def __init__(
                self,
                *,
                key: builtins.str = ...,
                value: builtins.str = ...,
            ) -> None: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
            ) -> None: ...

        FORMAT_FIELD_NUMBER: builtins.int
        SCHEMA_FIELD_NUMBER: builtins.int
        OPTIONS_FIELD_NUMBER: builtins.int
        format: builtins.str
        """Required. Supported formats include: parquet, orc, text, json, parquet, csv, avro."""
        schema: builtins.str
        """Optional. If not set, Spark will infer the schema."""
        @property
        def options(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
            """The key is case insensitive."""
        def __init__(
            self,
            *,
            format: builtins.str = ...,
            schema: builtins.str = ...,
            options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "format", b"format", "options", b"options", "schema", b"schema"
            ],
        ) -> None: ...

    NAMED_TABLE_FIELD_NUMBER: builtins.int
    DATA_SOURCE_FIELD_NUMBER: builtins.int
    @property
    def named_table(self) -> global___Read.NamedTable: ...
    @property
    def data_source(self) -> global___Read.DataSource: ...
    def __init__(
        self,
        *,
        named_table: global___Read.NamedTable | None = ...,
        data_source: global___Read.DataSource | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "data_source", b"data_source", "named_table", b"named_table", "read_type", b"read_type"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "data_source", b"data_source", "named_table", b"named_table", "read_type", b"read_type"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["read_type", b"read_type"]
    ) -> typing_extensions.Literal["named_table", "data_source"] | None: ...

global___Read = Read

class Project(google.protobuf.message.Message):
    """Projection of a bag of expressions for a given input relation.

    The input relation must be specified.
    The projected expression can be an arbitrary expression.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FIELD_NUMBER: builtins.int
    EXPRESSIONS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    @property
    def expressions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        pyspark.sql.connect.proto.expressions_pb2.Expression
    ]: ...
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        expressions: collections.abc.Iterable[pyspark.sql.connect.proto.expressions_pb2.Expression]
        | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["expressions", b"expressions", "input", b"input"],
    ) -> None: ...

global___Project = Project

class Filter(google.protobuf.message.Message):
    """Relation that applies a boolean expression `condition` on each row of `input` to produce
    the output result.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FIELD_NUMBER: builtins.int
    CONDITION_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    @property
    def condition(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression: ...
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        condition: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["condition", b"condition", "input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["condition", b"condition", "input", b"input"]
    ) -> None: ...

global___Filter = Filter

class Join(google.protobuf.message.Message):
    """Relation of type [[Join]].

    `left` and `right` must be present.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _JoinType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _JoinTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Join._JoinType.ValueType],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        JOIN_TYPE_UNSPECIFIED: Join._JoinType.ValueType  # 0
        JOIN_TYPE_INNER: Join._JoinType.ValueType  # 1
        JOIN_TYPE_FULL_OUTER: Join._JoinType.ValueType  # 2
        JOIN_TYPE_LEFT_OUTER: Join._JoinType.ValueType  # 3
        JOIN_TYPE_RIGHT_OUTER: Join._JoinType.ValueType  # 4
        JOIN_TYPE_LEFT_ANTI: Join._JoinType.ValueType  # 5
        JOIN_TYPE_LEFT_SEMI: Join._JoinType.ValueType  # 6

    class JoinType(_JoinType, metaclass=_JoinTypeEnumTypeWrapper): ...
    JOIN_TYPE_UNSPECIFIED: Join.JoinType.ValueType  # 0
    JOIN_TYPE_INNER: Join.JoinType.ValueType  # 1
    JOIN_TYPE_FULL_OUTER: Join.JoinType.ValueType  # 2
    JOIN_TYPE_LEFT_OUTER: Join.JoinType.ValueType  # 3
    JOIN_TYPE_RIGHT_OUTER: Join.JoinType.ValueType  # 4
    JOIN_TYPE_LEFT_ANTI: Join.JoinType.ValueType  # 5
    JOIN_TYPE_LEFT_SEMI: Join.JoinType.ValueType  # 6

    LEFT_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    JOIN_CONDITION_FIELD_NUMBER: builtins.int
    JOIN_TYPE_FIELD_NUMBER: builtins.int
    @property
    def left(self) -> global___Relation: ...
    @property
    def right(self) -> global___Relation: ...
    @property
    def join_condition(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression: ...
    join_type: global___Join.JoinType.ValueType
    def __init__(
        self,
        *,
        left: global___Relation | None = ...,
        right: global___Relation | None = ...,
        join_condition: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ...,
        join_type: global___Join.JoinType.ValueType = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "join_condition", b"join_condition", "left", b"left", "right", b"right"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "join_condition",
            b"join_condition",
            "join_type",
            b"join_type",
            "left",
            b"left",
            "right",
            b"right",
        ],
    ) -> None: ...

global___Join = Join

class Union(google.protobuf.message.Message):
    """Relation of type [[Union]], at least one input must be set."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _UnionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _UnionTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Union._UnionType.ValueType],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNION_TYPE_UNSPECIFIED: Union._UnionType.ValueType  # 0
        UNION_TYPE_DISTINCT: Union._UnionType.ValueType  # 1
        UNION_TYPE_ALL: Union._UnionType.ValueType  # 2

    class UnionType(_UnionType, metaclass=_UnionTypeEnumTypeWrapper): ...
    UNION_TYPE_UNSPECIFIED: Union.UnionType.ValueType  # 0
    UNION_TYPE_DISTINCT: Union.UnionType.ValueType  # 1
    UNION_TYPE_ALL: Union.UnionType.ValueType  # 2

    INPUTS_FIELD_NUMBER: builtins.int
    UNION_TYPE_FIELD_NUMBER: builtins.int
    @property
    def inputs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Relation]: ...
    union_type: global___Union.UnionType.ValueType
    def __init__(
        self,
        *,
        inputs: collections.abc.Iterable[global___Relation] | None = ...,
        union_type: global___Union.UnionType.ValueType = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["inputs", b"inputs", "union_type", b"union_type"],
    ) -> None: ...

global___Union = Union

class Limit(google.protobuf.message.Message):
    """Relation of type [[Limit]] that is used to `limit` rows from the input relation."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    limit: builtins.int
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["input", b"input", "limit", b"limit"]
    ) -> None: ...

global___Limit = Limit

class Offset(google.protobuf.message.Message):
    """Relation of type [[Offset]] that is used to read rows staring from the `offset` on
    the input relation.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    offset: builtins.int
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        offset: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["input", b"input", "offset", b"offset"]
    ) -> None: ...

global___Offset = Offset

class Aggregate(google.protobuf.message.Message):
    """Relation of type [[Aggregate]]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class AggregateFunction(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        ARGUMENTS_FIELD_NUMBER: builtins.int
        name: builtins.str
        @property
        def arguments(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            pyspark.sql.connect.proto.expressions_pb2.Expression
        ]: ...
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            arguments: collections.abc.Iterable[
                pyspark.sql.connect.proto.expressions_pb2.Expression
            ]
            | None = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["arguments", b"arguments", "name", b"name"]
        ) -> None: ...

    INPUT_FIELD_NUMBER: builtins.int
    GROUPING_EXPRESSIONS_FIELD_NUMBER: builtins.int
    RESULT_EXPRESSIONS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    @property
    def grouping_expressions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        pyspark.sql.connect.proto.expressions_pb2.Expression
    ]: ...
    @property
    def result_expressions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Aggregate.AggregateFunction
    ]: ...
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        grouping_expressions: collections.abc.Iterable[
            pyspark.sql.connect.proto.expressions_pb2.Expression
        ]
        | None = ...,
        result_expressions: collections.abc.Iterable[global___Aggregate.AggregateFunction]
        | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "grouping_expressions",
            b"grouping_expressions",
            "input",
            b"input",
            "result_expressions",
            b"result_expressions",
        ],
    ) -> None: ...

global___Aggregate = Aggregate

class Sort(google.protobuf.message.Message):
    """Relation of type [[Sort]]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _SortDirection:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SortDirectionEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Sort._SortDirection.ValueType],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SORT_DIRECTION_UNSPECIFIED: Sort._SortDirection.ValueType  # 0
        SORT_DIRECTION_ASCENDING: Sort._SortDirection.ValueType  # 1
        SORT_DIRECTION_DESCENDING: Sort._SortDirection.ValueType  # 2

    class SortDirection(_SortDirection, metaclass=_SortDirectionEnumTypeWrapper): ...
    SORT_DIRECTION_UNSPECIFIED: Sort.SortDirection.ValueType  # 0
    SORT_DIRECTION_ASCENDING: Sort.SortDirection.ValueType  # 1
    SORT_DIRECTION_DESCENDING: Sort.SortDirection.ValueType  # 2

    class _SortNulls:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SortNullsEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Sort._SortNulls.ValueType],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SORT_NULLS_UNSPECIFIED: Sort._SortNulls.ValueType  # 0
        SORT_NULLS_FIRST: Sort._SortNulls.ValueType  # 1
        SORT_NULLS_LAST: Sort._SortNulls.ValueType  # 2

    class SortNulls(_SortNulls, metaclass=_SortNullsEnumTypeWrapper): ...
    SORT_NULLS_UNSPECIFIED: Sort.SortNulls.ValueType  # 0
    SORT_NULLS_FIRST: Sort.SortNulls.ValueType  # 1
    SORT_NULLS_LAST: Sort.SortNulls.ValueType  # 2

    class SortField(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        EXPRESSION_FIELD_NUMBER: builtins.int
        DIRECTION_FIELD_NUMBER: builtins.int
        NULLS_FIELD_NUMBER: builtins.int
        @property
        def expression(self) -> pyspark.sql.connect.proto.expressions_pb2.Expression: ...
        direction: global___Sort.SortDirection.ValueType
        nulls: global___Sort.SortNulls.ValueType
        def __init__(
            self,
            *,
            expression: pyspark.sql.connect.proto.expressions_pb2.Expression | None = ...,
            direction: global___Sort.SortDirection.ValueType = ...,
            nulls: global___Sort.SortNulls.ValueType = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["expression", b"expression"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "direction", b"direction", "expression", b"expression", "nulls", b"nulls"
            ],
        ) -> None: ...

    INPUT_FIELD_NUMBER: builtins.int
    SORT_FIELDS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    @property
    def sort_fields(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Sort.SortField
    ]: ...
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        sort_fields: collections.abc.Iterable[global___Sort.SortField] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["input", b"input", "sort_fields", b"sort_fields"],
    ) -> None: ...

global___Sort = Sort

class Deduplicate(google.protobuf.message.Message):
    """Relation of type [[Deduplicate]] which have duplicate rows removed, could consider either only
    the subset of columns or all the columns.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_FIELD_NUMBER: builtins.int
    COLUMN_NAMES_FIELD_NUMBER: builtins.int
    ALL_COLUMNS_AS_KEYS_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    @property
    def column_names(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    all_columns_as_keys: builtins.bool
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        column_names: collections.abc.Iterable[builtins.str] | None = ...,
        all_columns_as_keys: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "all_columns_as_keys",
            b"all_columns_as_keys",
            "column_names",
            b"column_names",
            "input",
            b"input",
        ],
    ) -> None: ...

global___Deduplicate = Deduplicate

class LocalRelation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ATTRIBUTES_FIELD_NUMBER: builtins.int
    @property
    def attributes(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        pyspark.sql.connect.proto.expressions_pb2.Expression.QualifiedAttribute
    ]:
        """TODO: support local data."""
    def __init__(
        self,
        *,
        attributes: collections.abc.Iterable[
            pyspark.sql.connect.proto.expressions_pb2.Expression.QualifiedAttribute
        ]
        | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["attributes", b"attributes"]
    ) -> None: ...

global___LocalRelation = LocalRelation

class Sample(google.protobuf.message.Message):
    """Relation of type [[Sample]] that samples a fraction of the dataset."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Seed(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SEED_FIELD_NUMBER: builtins.int
        seed: builtins.int
        def __init__(
            self,
            *,
            seed: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["seed", b"seed"]) -> None: ...

    INPUT_FIELD_NUMBER: builtins.int
    LOWER_BOUND_FIELD_NUMBER: builtins.int
    UPPER_BOUND_FIELD_NUMBER: builtins.int
    WITH_REPLACEMENT_FIELD_NUMBER: builtins.int
    SEED_FIELD_NUMBER: builtins.int
    @property
    def input(self) -> global___Relation: ...
    lower_bound: builtins.float
    upper_bound: builtins.float
    with_replacement: builtins.bool
    @property
    def seed(self) -> global___Sample.Seed: ...
    def __init__(
        self,
        *,
        input: global___Relation | None = ...,
        lower_bound: builtins.float = ...,
        upper_bound: builtins.float = ...,
        with_replacement: builtins.bool = ...,
        seed: global___Sample.Seed | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["input", b"input", "seed", b"seed"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "input",
            b"input",
            "lower_bound",
            b"lower_bound",
            "seed",
            b"seed",
            "upper_bound",
            b"upper_bound",
            "with_replacement",
            b"with_replacement",
        ],
    ) -> None: ...

global___Sample = Sample
