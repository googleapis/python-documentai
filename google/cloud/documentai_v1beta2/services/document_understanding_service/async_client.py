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

from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation
from google.api_core import operation_async
from google.cloud.documentai_v1beta2.types import document
from google.cloud.documentai_v1beta2.types import document_understanding
from google.rpc import status_pb2 as status  # type: ignore

from .transports.base import DocumentUnderstandingServiceTransport
from .transports.grpc_asyncio import DocumentUnderstandingServiceGrpcAsyncIOTransport
from .client import DocumentUnderstandingServiceClient


class DocumentUnderstandingServiceAsyncClient:
    """Service to parse structured information from unstructured or
    semi-structured documents using state-of-the-art Google AI such
    as natural language, computer vision, and translation.
    """

    _client: DocumentUnderstandingServiceClient

    DEFAULT_ENDPOINT = DocumentUnderstandingServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DocumentUnderstandingServiceClient.DEFAULT_MTLS_ENDPOINT

    from_service_account_file = (
        DocumentUnderstandingServiceClient.from_service_account_file
    )
    from_service_account_json = from_service_account_file

    get_transport_class = functools.partial(
        type(DocumentUnderstandingServiceClient).get_transport_class,
        type(DocumentUnderstandingServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, DocumentUnderstandingServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
    ) -> None:
        """Instantiate the document understanding service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DocumentUnderstandingServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint, this is the default value for
                the environment variable) and "auto" (auto switch to the default
                mTLS endpoint if client SSL credentials is present). However,
                the ``api_endpoint`` property takes precedence if provided.
                (2) The ``client_cert_source`` property is used to provide client
                SSL credentials for mutual TLS transport. If not provided, the
                default SSL credentials will be used if present.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = DocumentUnderstandingServiceClient(
            credentials=credentials, transport=transport, client_options=client_options
        )

    async def batch_process_documents(
        self,
        request: document_understanding.BatchProcessDocumentsRequest = None,
        *,
        requests: Sequence[document_understanding.ProcessDocumentRequest] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""LRO endpoint to batch process many documents. The output is
        written to Cloud Storage as JSON in the [Document] format.

        Args:
            request (:class:`~.document_understanding.BatchProcessDocumentsRequest`):
                The request object. Request to batch process documents
                as an asynchronous operation. The output is written to
                Cloud Storage as JSON in the [Document] format.
            requests (:class:`Sequence[~.document_understanding.ProcessDocumentRequest]`):
                Required. Individual requests for
                each document.
                This corresponds to the ``requests`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.document_understanding.BatchProcessDocumentsResponse``:
                Response to an batch document processing request. This
                is returned in the LRO Operation after the operation is
                complete.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([requests]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_understanding.BatchProcessDocumentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if requests is not None:
            request.requests = requests

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_process_documents,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_understanding.BatchProcessDocumentsResponse,
            metadata_type=document_understanding.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def process_document(
        self,
        request: document_understanding.ProcessDocumentRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document.Document:
        r"""Processes a single document.

        Args:
            request (:class:`~.document_understanding.ProcessDocumentRequest`):
                The request object. Request to process one document.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.document.Document:
                Document represents the canonical
                document resource in Document
                Understanding AI. It is an interchange
                format that provides insights into
                documents and allows for collaboration
                between users and Document Understanding
                AI to iterate and optimize for quality.

        """
        # Create or coerce a protobuf request object.

        request = document_understanding.ProcessDocumentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.process_document,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Done; return the response.
        return response


try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-documentai").version
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


__all__ = ("DocumentUnderstandingServiceAsyncClient",)
