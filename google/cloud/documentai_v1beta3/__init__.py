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

from .services.document_processor_service import DocumentProcessorServiceClient
from .services.document_processor_service import DocumentProcessorServiceAsyncClient

from .types.document import Document
from .types.document_io import BatchDocumentsInputConfig
from .types.document_io import DocumentOutputConfig
from .types.document_io import GcsDocument
from .types.document_io import GcsDocuments
from .types.document_io import GcsPrefix
from .types.document_io import RawDocument
from .types.document_processor_service import BatchProcessMetadata
from .types.document_processor_service import BatchProcessRequest
from .types.document_processor_service import BatchProcessResponse
from .types.document_processor_service import CommonOperationMetadata
from .types.document_processor_service import HumanReviewStatus
from .types.document_processor_service import ProcessRequest
from .types.document_processor_service import ProcessResponse
from .types.document_processor_service import ReviewDocumentOperationMetadata
from .types.document_processor_service import ReviewDocumentRequest
from .types.document_processor_service import ReviewDocumentResponse
from .types.geometry import BoundingPoly
from .types.geometry import NormalizedVertex
from .types.geometry import Vertex

__all__ = (
    "DocumentProcessorServiceAsyncClient",
    "BatchDocumentsInputConfig",
    "BatchProcessMetadata",
    "BatchProcessRequest",
    "BatchProcessResponse",
    "BoundingPoly",
    "CommonOperationMetadata",
    "Document",
    "DocumentOutputConfig",
    "DocumentProcessorServiceClient",
    "GcsDocument",
    "GcsDocuments",
    "GcsPrefix",
    "HumanReviewStatus",
    "NormalizedVertex",
    "ProcessRequest",
    "ProcessResponse",
    "RawDocument",
    "ReviewDocumentOperationMetadata",
    "ReviewDocumentRequest",
    "ReviewDocumentResponse",
    "Vertex",
)
