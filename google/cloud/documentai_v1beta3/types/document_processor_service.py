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

from google.cloud.documentai_v1beta3.types import document as gcd_document
from google.cloud.documentai_v1beta3.types import document_io
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3",
    manifest={
        "ProcessRequest",
        "HumanReviewStatus",
        "ProcessResponse",
        "BatchProcessRequest",
        "BatchProcessResponse",
        "BatchProcessMetadata",
        "ReviewDocumentRequest",
        "ReviewDocumentResponse",
        "ReviewDocumentOperationMetadata",
        "CommonOperationMetadata",
    },
)


class ProcessRequest(proto.Message):
    r"""Request message for the process document method.
    Attributes:
        inline_document (google.cloud.documentai_v1beta3.types.Document):
            An inline document proto.
        raw_document (google.cloud.documentai_v1beta3.types.RawDocument):
            A raw document content (bytes).
        name (str):
            Required. The processor resource name.
        document (google.cloud.documentai_v1beta3.types.Document):
            The document payload, the [content] and [mime_type] fields
            must be set.
        skip_human_review (bool):
            Whether Human Review feature should be
            skipped for this request. Default to false.
    """

    inline_document = proto.Field(
        proto.MESSAGE, number=4, oneof="source", message=gcd_document.Document,
    )
    raw_document = proto.Field(
        proto.MESSAGE, number=5, oneof="source", message=document_io.RawDocument,
    )
    name = proto.Field(proto.STRING, number=1,)
    document = proto.Field(proto.MESSAGE, number=2, message=gcd_document.Document,)
    skip_human_review = proto.Field(proto.BOOL, number=3,)


class HumanReviewStatus(proto.Message):
    r"""The status of human review on a processed document.
    Attributes:
        state (google.cloud.documentai_v1beta3.types.HumanReviewStatus.State):
            The state of human review on the processing
            request.
        state_message (str):
            A message providing more details about the
            human review state.
        human_review_operation (str):
            The name of the operation triggered by the processed
            document. This field is populated only when the [state] is
            [HUMAN_REVIEW_IN_PROGRESS]. It has the same response type
            and metadata as the long running operation returned by
            [ReviewDocument] method.
    """

    class State(proto.Enum):
        r"""The final state of human review on a processed document."""
        STATE_UNSPECIFIED = 0
        SKIPPED = 1
        VALIDATION_PASSED = 2
        IN_PROGRESS = 3
        ERROR = 4

    state = proto.Field(proto.ENUM, number=1, enum=State,)
    state_message = proto.Field(proto.STRING, number=2,)
    human_review_operation = proto.Field(proto.STRING, number=3,)


class ProcessResponse(proto.Message):
    r"""Response message for the process document method.
    Attributes:
        document (google.cloud.documentai_v1beta3.types.Document):
            The document payload, will populate fields
            based on the processor's behavior.
        human_review_operation (str):
            The name of the operation triggered by the
            processed document. If the human review process
            is not triggered, this field will be empty. It
            has the same response type and metadata as the
            long running operation returned by
            ReviewDocument method.
        human_review_status (google.cloud.documentai_v1beta3.types.HumanReviewStatus):
            The status of human review on the processed
            document.
    """

    document = proto.Field(proto.MESSAGE, number=1, message=gcd_document.Document,)
    human_review_operation = proto.Field(proto.STRING, number=2,)
    human_review_status = proto.Field(
        proto.MESSAGE, number=3, message="HumanReviewStatus",
    )


class BatchProcessRequest(proto.Message):
    r"""Request message for batch process document method.
    Attributes:
        name (str):
            Required. The processor resource name.
        input_configs (Sequence[google.cloud.documentai_v1beta3.types.BatchProcessRequest.BatchInputConfig]):
            The input config for each single document in
            the batch process.
        output_config (google.cloud.documentai_v1beta3.types.BatchProcessRequest.BatchOutputConfig):
            The overall output config for batch process.
        input_documents (google.cloud.documentai_v1beta3.types.BatchDocumentsInputConfig):
            The input documents for batch process.
        document_output_config (google.cloud.documentai_v1beta3.types.DocumentOutputConfig):
            The overall output config for batch process.
        skip_human_review (bool):
            Whether Human Review feature should be
            skipped for this request. Default to false.
    """

    class BatchInputConfig(proto.Message):
        r"""The message for input config in batch process.
        Attributes:
            gcs_source (str):
                The Cloud Storage location as the source of
                the document.
            mime_type (str):
                Mimetype of the input. If the input is a raw document, the
                supported mimetypes are application/pdf, image/tiff, and
                image/gif. If the input is a [Document] proto, the type
                should be application/json.
        """

        gcs_source = proto.Field(proto.STRING, number=1,)
        mime_type = proto.Field(proto.STRING, number=2,)

    class BatchOutputConfig(proto.Message):
        r"""The message for output config in batch process.
        Attributes:
            gcs_destination (str):
                The output Cloud Storage directory to put the
                processed documents.
        """

        gcs_destination = proto.Field(proto.STRING, number=1,)

    name = proto.Field(proto.STRING, number=1,)
    input_configs = proto.RepeatedField(
        proto.MESSAGE, number=2, message=BatchInputConfig,
    )
    output_config = proto.Field(proto.MESSAGE, number=3, message=BatchOutputConfig,)
    input_documents = proto.Field(
        proto.MESSAGE, number=5, message=document_io.BatchDocumentsInputConfig,
    )
    document_output_config = proto.Field(
        proto.MESSAGE, number=6, message=document_io.DocumentOutputConfig,
    )
    skip_human_review = proto.Field(proto.BOOL, number=4,)


class BatchProcessResponse(proto.Message):
    r"""Response message for batch process document method.    """


class BatchProcessMetadata(proto.Message):
    r"""The long running operation metadata for batch process method.
    Attributes:
        state (google.cloud.documentai_v1beta3.types.BatchProcessMetadata.State):
            The state of the current batch processing.
        state_message (str):
            A message providing more details about the
            current state of processing. For example, the
            error message if the operation is failed.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update time of the operation.
        individual_process_statuses (Sequence[google.cloud.documentai_v1beta3.types.BatchProcessMetadata.IndividualProcessStatus]):
            The list of response details of each
            document.
    """

    class State(proto.Enum):
        r"""Possible states of the batch processing operation."""
        STATE_UNSPECIFIED = 0
        WAITING = 1
        RUNNING = 2
        SUCCEEDED = 3
        CANCELLING = 4
        CANCELLED = 5
        FAILED = 6

    class IndividualProcessStatus(proto.Message):
        r"""The status of a each individual document in the batch
        process.

        Attributes:
            input_gcs_source (str):
                The source of the document, same as the [input_gcs_source]
                field in the request when the batch process started. The
                batch process is started by take snapshot of that document,
                since a user can move or change that document during the
                process.
            status (google.rpc.status_pb2.Status):
                The status of the processing of the document.
            output_gcs_destination (str):
                The output_gcs_destination (in the request as
                'output_gcs_destination') of the processed document if it
                was successful, otherwise empty.
            human_review_operation (str):
                The name of the operation triggered by the
                processed document. If the human review process
                is not triggered, this field will be empty. It
                has the same response type and metadata as the
                long running operation returned by
                ReviewDocument method.
            human_review_status (google.cloud.documentai_v1beta3.types.HumanReviewStatus):
                The status of human review on the processed
                document.
        """

        input_gcs_source = proto.Field(proto.STRING, number=1,)
        status = proto.Field(proto.MESSAGE, number=2, message=status_pb2.Status,)
        output_gcs_destination = proto.Field(proto.STRING, number=3,)
        human_review_operation = proto.Field(proto.STRING, number=4,)
        human_review_status = proto.Field(
            proto.MESSAGE, number=5, message="HumanReviewStatus",
        )

    state = proto.Field(proto.ENUM, number=1, enum=State,)
    state_message = proto.Field(proto.STRING, number=2,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)
    individual_process_statuses = proto.RepeatedField(
        proto.MESSAGE, number=5, message=IndividualProcessStatus,
    )


class ReviewDocumentRequest(proto.Message):
    r"""Request message for review document method.
    Attributes:
        inline_document (google.cloud.documentai_v1beta3.types.Document):
            An inline document proto.
        human_review_config (str):
            Required. The resource name of the
            HumanReviewConfig that the document will be
            reviewed with.
        document (google.cloud.documentai_v1beta3.types.Document):
            The document that needs human review.
    """

    inline_document = proto.Field(
        proto.MESSAGE, number=4, oneof="source", message=gcd_document.Document,
    )
    human_review_config = proto.Field(proto.STRING, number=1,)
    document = proto.Field(proto.MESSAGE, number=2, message=gcd_document.Document,)


class ReviewDocumentResponse(proto.Message):
    r"""Response message for review document method.
    Attributes:
        gcs_destination (str):
            The Cloud Storage uri for the human reviewed
            document.
    """

    gcs_destination = proto.Field(proto.STRING, number=1,)


class ReviewDocumentOperationMetadata(proto.Message):
    r"""The long running operation metadata for review document
    method.

    Attributes:
        state (google.cloud.documentai_v1beta3.types.ReviewDocumentOperationMetadata.State):
            Used only when Operation.done is false.
        state_message (str):
            A message providing more details about the
            current state of processing. For example, the
            error message if the operation is failed.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update time of the operation.
        common_metadata (google.cloud.documentai_v1beta3.types.CommonOperationMetadata):
            The basic metadata of the long running
            operation.
    """

    class State(proto.Enum):
        r"""State of the longrunning operation."""
        STATE_UNSPECIFIED = 0
        RUNNING = 1
        CANCELLING = 2
        SUCCEEDED = 3
        FAILED = 4
        CANCELLED = 5

    state = proto.Field(proto.ENUM, number=1, enum=State,)
    state_message = proto.Field(proto.STRING, number=2,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)
    common_metadata = proto.Field(
        proto.MESSAGE, number=5, message="CommonOperationMetadata",
    )


class CommonOperationMetadata(proto.Message):
    r"""The common metadata for long running operations.
    Attributes:
        state (google.cloud.documentai_v1beta3.types.CommonOperationMetadata.State):
            The state of the operation.
        state_message (str):
            A message providing more details about the
            current state of processing.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update time of the operation.
    """

    class State(proto.Enum):
        r"""State of the longrunning operation."""
        STATE_UNSPECIFIED = 0
        RUNNING = 1
        CANCELLING = 2
        SUCCEEDED = 3
        FAILED = 4
        CANCELLED = 5

    state = proto.Field(proto.ENUM, number=1, enum=State,)
    state_message = proto.Field(proto.STRING, number=2,)
    create_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)


__all__ = tuple(sorted(__protobuf__.manifest))
