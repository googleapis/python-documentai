# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3",
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
            of the [content].
    """

    content = proto.Field(proto.BYTES, number=1,)
    mime_type = proto.Field(proto.STRING, number=2,)


class GcsDocument(proto.Message):
    r"""Specifies a document stored on Cloud Storage.
    Attributes:
        gcs_uri (str):
            The Cloud Storage object uri.
        mime_type (str):
            An IANA MIME type (RFC6838) of the content.
    """

    gcs_uri = proto.Field(proto.STRING, number=1,)
    mime_type = proto.Field(proto.STRING, number=2,)


class GcsDocuments(proto.Message):
    r"""Specifies a set of documents on Cloud Storage.
    Attributes:
        documents (Sequence[google.cloud.documentai_v1beta3.types.GcsDocument]):
            The list of documents.
    """

    documents = proto.RepeatedField(proto.MESSAGE, number=1, message="GcsDocument",)


class GcsPrefix(proto.Message):
    r"""Specifies all documents on Cloud Storage with a common
    prefix.

    Attributes:
        gcs_uri_prefix (str):
            The URI prefix.
    """

    gcs_uri_prefix = proto.Field(proto.STRING, number=1,)


class BatchDocumentsInputConfig(proto.Message):
    r"""The common config to specify a set of documents used as
    input.

    Attributes:
        gcs_prefix (google.cloud.documentai_v1beta3.types.GcsPrefix):
            The set of documents that match the specified Cloud Storage
            [gcs_prefix].
        gcs_documents (google.cloud.documentai_v1beta3.types.GcsDocuments):
            The set of documents individually specified
            on Cloud Storage.
    """

    gcs_prefix = proto.Field(
        proto.MESSAGE, number=1, oneof="source", message="GcsPrefix",
    )
    gcs_documents = proto.Field(
        proto.MESSAGE, number=2, oneof="source", message="GcsDocuments",
    )


class DocumentOutputConfig(proto.Message):
    r"""Config that controls the output of documents. All documents
    will be written as a JSON file.

    Attributes:
        gcs_output_config (google.cloud.documentai_v1beta3.types.DocumentOutputConfig.GcsOutputConfig):
            Output config to write the results to Cloud
            Storage.
    """

    class GcsOutputConfig(proto.Message):
        r"""The configuration used when outputting documents.
        Attributes:
            gcs_uri (str):
                The Cloud Storage uri (a directory) of the
                output.
        """

        gcs_uri = proto.Field(proto.STRING, number=1,)

    gcs_output_config = proto.Field(
        proto.MESSAGE, number=1, oneof="destination", message=GcsOutputConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
