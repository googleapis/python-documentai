# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

from google.protobuf import field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1",
    manifest={
        "RawDocument",
        "GcsDocument",
        "GcsDocuments",
        "GcsPrefix",
        "BatchDocumentsInputConfig",
        "DocumentOutputConfig",
    },
)


class RawDocument(proto.Message):
    r"""Payload message of raw document content (bytes).

    Attributes:
        content (bytes):
            Inline document content.
        mime_type (str):
            An IANA MIME type (RFC6838) indicating the nature and format
            of the
            [content][google.cloud.documentai.v1.RawDocument.content].
    """

    content: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GcsDocument(proto.Message):
    r"""Specifies a document stored on Cloud Storage.

    Attributes:
        gcs_uri (str):
            The Cloud Storage object uri.
        mime_type (str):
            An IANA MIME type (RFC6838) of the content.
    """

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GcsDocuments(proto.Message):
    r"""Specifies a set of documents on Cloud Storage.

    Attributes:
        documents (MutableSequence[google.cloud.documentai_v1.types.GcsDocument]):
            The list of documents.
    """

    documents: MutableSequence["GcsDocument"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GcsDocument",
    )


class GcsPrefix(proto.Message):
    r"""Specifies all documents on Cloud Storage with a common
    prefix.

    Attributes:
        gcs_uri_prefix (str):
            The URI prefix.
    """

    gcs_uri_prefix: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchDocumentsInputConfig(proto.Message):
    r"""The common config to specify a set of documents used as
    input.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_prefix (google.cloud.documentai_v1.types.GcsPrefix):
            The set of documents that match the specified Cloud Storage
            ``gcs_prefix``.

            This field is a member of `oneof`_ ``source``.
        gcs_documents (google.cloud.documentai_v1.types.GcsDocuments):
            The set of documents individually specified
            on Cloud Storage.

            This field is a member of `oneof`_ ``source``.
    """

    gcs_prefix: "GcsPrefix" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="GcsPrefix",
    )
    gcs_documents: "GcsDocuments" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="GcsDocuments",
    )


class DocumentOutputConfig(proto.Message):
    r"""Config that controls the output of documents. All documents
    will be written as a JSON file.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_output_config (google.cloud.documentai_v1.types.DocumentOutputConfig.GcsOutputConfig):
            Output config to write the results to Cloud
            Storage.

            This field is a member of `oneof`_ ``destination``.
    """

    class GcsOutputConfig(proto.Message):
        r"""The configuration used when outputting documents.

        Attributes:
            gcs_uri (str):
                The Cloud Storage uri (a directory) of the
                output.
            field_mask (google.protobuf.field_mask_pb2.FieldMask):
                Specifies which fields to include in the output documents.
                Only supports top level document and pages field so it must
                be in the form of ``{document_field_name}`` or
                ``pages.{page_field_name}``.
        """

        gcs_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        field_mask: field_mask_pb2.FieldMask = proto.Field(
            proto.MESSAGE,
            number=2,
            message=field_mask_pb2.FieldMask,
        )

    gcs_output_config: GcsOutputConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message=GcsOutputConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
