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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.documentai_v1beta3.services.document_processor_service import pagers
from google.cloud.documentai_v1beta3.types import (
    document,
    document_processor_service,
    document_schema,
    evaluation,
)
from google.cloud.documentai_v1beta3.types import processor
from google.cloud.documentai_v1beta3.types import processor as gcd_processor
from google.cloud.documentai_v1beta3.types import processor_type

from .client import DocumentProcessorServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DocumentProcessorServiceTransport
from .transports.grpc_asyncio import DocumentProcessorServiceGrpcAsyncIOTransport


class DocumentProcessorServiceAsyncClient:
    """Service to call Cloud DocumentAI to process documents
    according to the processor's definition. Processors are built
    using state-of-the-art Google AI such as natural language,
    computer vision, and translation to extract structured
    information from unstructured or semi-structured documents.
    """

    _client: DocumentProcessorServiceClient

    DEFAULT_ENDPOINT = DocumentProcessorServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DocumentProcessorServiceClient.DEFAULT_MTLS_ENDPOINT

    evaluation_path = staticmethod(DocumentProcessorServiceClient.evaluation_path)
    parse_evaluation_path = staticmethod(
        DocumentProcessorServiceClient.parse_evaluation_path
    )
    human_review_config_path = staticmethod(
        DocumentProcessorServiceClient.human_review_config_path
    )
    parse_human_review_config_path = staticmethod(
        DocumentProcessorServiceClient.parse_human_review_config_path
    )
    processor_path = staticmethod(DocumentProcessorServiceClient.processor_path)
    parse_processor_path = staticmethod(
        DocumentProcessorServiceClient.parse_processor_path
    )
    processor_type_path = staticmethod(
        DocumentProcessorServiceClient.processor_type_path
    )
    parse_processor_type_path = staticmethod(
        DocumentProcessorServiceClient.parse_processor_type_path
    )
    processor_version_path = staticmethod(
        DocumentProcessorServiceClient.processor_version_path
    )
    parse_processor_version_path = staticmethod(
        DocumentProcessorServiceClient.parse_processor_version_path
    )
    common_billing_account_path = staticmethod(
        DocumentProcessorServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DocumentProcessorServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DocumentProcessorServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DocumentProcessorServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DocumentProcessorServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DocumentProcessorServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        DocumentProcessorServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        DocumentProcessorServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        DocumentProcessorServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        DocumentProcessorServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentProcessorServiceAsyncClient: The constructed client.
        """
        return DocumentProcessorServiceClient.from_service_account_info.__func__(DocumentProcessorServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentProcessorServiceAsyncClient: The constructed client.
        """
        return DocumentProcessorServiceClient.from_service_account_file.__func__(DocumentProcessorServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DocumentProcessorServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DocumentProcessorServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DocumentProcessorServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DocumentProcessorServiceClient).get_transport_class,
        type(DocumentProcessorServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DocumentProcessorServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the document processor service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DocumentProcessorServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DocumentProcessorServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def process_document(
        self,
        request: Optional[
            Union[document_processor_service.ProcessRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document_processor_service.ProcessResponse:
        r"""Processes a single document.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_process_document():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                inline_document = documentai_v1beta3.Document()
                inline_document.uri = "uri_value"

                request = documentai_v1beta3.ProcessRequest(
                    inline_document=inline_document,
                    name="name_value",
                )

                # Make the request
                response = await client.process_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.ProcessRequest, dict]]):
                The request object. Request message for the process
                document method.
            name (:class:`str`):
                Required. The resource name of the
                [Processor][google.cloud.documentai.v1beta3.Processor]
                or
                [ProcessorVersion][google.cloud.documentai.v1beta3.ProcessorVersion]
                to use for processing. If a
                [Processor][google.cloud.documentai.v1beta3.Processor]
                is specified, the server will use its [default
                version][google.cloud.documentai.v1beta3.Processor.default_processor_version].
                Format:
                ``projects/{project}/locations/{location}/processors/{processor}``,
                or
                ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.types.ProcessResponse:
                Response message for the process
                document method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.ProcessRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.process_document,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=120.0,
            ),
            default_timeout=120.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def batch_process_documents(
        self,
        request: Optional[
            Union[document_processor_service.BatchProcessRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""LRO endpoint to batch process many documents. The output is
        written to Cloud Storage as JSON in the [Document] format.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_batch_process_documents():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.BatchProcessRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.batch_process_documents(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.BatchProcessRequest, dict]]):
                The request object. Request message for batch process
                document method.
            name (:class:`str`):
                Required. The resource name of
                [Processor][google.cloud.documentai.v1beta3.Processor]
                or
                [ProcessorVersion][google.cloud.documentai.v1beta3.ProcessorVersion].
                Format:
                ``projects/{project}/locations/{location}/processors/{processor}``,
                or
                ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.BatchProcessResponse`
                Response message for batch process document method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.BatchProcessRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_process_documents,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=120.0,
            ),
            default_timeout=120.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.BatchProcessResponse,
            metadata_type=document_processor_service.BatchProcessMetadata,
        )

        # Done; return the response.
        return response

    async def fetch_processor_types(
        self,
        request: Optional[
            Union[document_processor_service.FetchProcessorTypesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document_processor_service.FetchProcessorTypesResponse:
        r"""Fetches processor types. Note that we do not use
        ListProcessorTypes here because it is not paginated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_fetch_processor_types():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.FetchProcessorTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.fetch_processor_types(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.FetchProcessorTypesRequest, dict]]):
                The request object. Request message for fetch processor
                types.
            parent (:class:`str`):
                Required. The project of processor type to list. The
                available processor types may depend on the
                allow-listing on projects. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.types.FetchProcessorTypesResponse:
                Response message for fetch processor
                types.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.FetchProcessorTypesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.fetch_processor_types,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_processor_types(
        self,
        request: Optional[
            Union[document_processor_service.ListProcessorTypesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProcessorTypesAsyncPager:
        r"""Lists the processor types that exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_list_processor_types():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.ListProcessorTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_processor_types(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest, dict]]):
                The request object. Request message for list processor
                types.
            parent (:class:`str`):
                Required. The location of processor type to list. The
                available processor types may depend on the
                allow-listing on projects. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorTypesAsyncPager:
                Response message for list processor
                types.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.ListProcessorTypesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_processor_types,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListProcessorTypesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_processors(
        self,
        request: Optional[
            Union[document_processor_service.ListProcessorsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProcessorsAsyncPager:
        r"""Lists all processors which belong to this project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_list_processors():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.ListProcessorsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_processors(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.ListProcessorsRequest, dict]]):
                The request object. Request message for list all
                processors belongs to a project.
            parent (:class:`str`):
                Required. The parent (project and location) which owns
                this collection of Processors. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorsAsyncPager:
                Response message for list processors.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.ListProcessorsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_processors,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListProcessorsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_processor(
        self,
        request: Optional[
            Union[document_processor_service.GetProcessorRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> processor.Processor:
        r"""Gets a processor detail.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_get_processor():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.GetProcessorRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_processor(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.GetProcessorRequest, dict]]):
                The request object. Request message for get processor.
            name (:class:`str`):
                Required. The processor resource
                name.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.types.Processor:
                The first-class citizen for Document
                AI. Each processor defines how to
                extract structural information from a
                document.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.GetProcessorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_processor,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def train_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.TrainProcessorVersionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        processor_version: Optional[processor.ProcessorVersion] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Trains a new processor version. Operation metadata is returned
        as cloud_documentai_core.TrainProcessorVersionMetadata.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_train_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.TrainProcessorVersionRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.train_processor_version(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.TrainProcessorVersionRequest, dict]]):
                The request object. Request message for the create
                processor version method.
            parent (:class:`str`):
                Required. The parent (project, location and processor)
                to create the new version for. Format:
                ``projects/{project}/locations/{location}/processors/{processor}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            processor_version (:class:`google.cloud.documentai_v1beta3.types.ProcessorVersion`):
                Required. The processor version to be
                created.

                This corresponds to the ``processor_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.TrainProcessorVersionResponse`
                The response for the TrainProcessorVersion method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, processor_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.TrainProcessorVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if processor_version is not None:
            request.processor_version = processor_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.train_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.TrainProcessorVersionResponse,
            metadata_type=document_processor_service.TrainProcessorVersionMetadata,
        )

        # Done; return the response.
        return response

    async def get_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.GetProcessorVersionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> processor.ProcessorVersion:
        r"""Gets a processor version detail.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_get_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.GetProcessorVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_processor_version(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.GetProcessorVersionRequest, dict]]):
                The request object. Request message for get processor
                version.
            name (:class:`str`):
                Required. The processor resource
                name.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.types.ProcessorVersion:
                A processor version is an
                implementation of a processor. Each
                processor can have multiple versions,
                pre-trained by Google internally or
                up-trained by the customer. At a time, a
                processor can only have one default
                version version. So the processor's
                behavior (when processing documents) is
                defined by a default version

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.GetProcessorVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_processor_versions(
        self,
        request: Optional[
            Union[document_processor_service.ListProcessorVersionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProcessorVersionsAsyncPager:
        r"""Lists all versions of a processor.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_list_processor_versions():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.ListProcessorVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_processor_versions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.ListProcessorVersionsRequest, dict]]):
                The request object. Request message for list all
                processor versions belongs to a processor.
            parent (:class:`str`):
                Required. The parent (project, location and processor)
                to list all versions. Format:
                ``projects/{project}/locations/{location}/processors/{processor}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorVersionsAsyncPager:
                Response message for list processors.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.ListProcessorVersionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_processor_versions,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListProcessorVersionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.DeleteProcessorVersionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes the processor version, all artifacts under
        the processor version will be deleted.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_delete_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.DeleteProcessorVersionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_processor_version(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.DeleteProcessorVersionRequest, dict]]):
                The request object. Request message for the delete
                processor version method.
            name (:class:`str`):
                Required. The processor version
                resource name to be deleted.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.DeleteProcessorVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=document_processor_service.DeleteProcessorVersionMetadata,
        )

        # Done; return the response.
        return response

    async def deploy_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.DeployProcessorVersionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deploys the processor version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_deploy_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.DeployProcessorVersionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.deploy_processor_version(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.DeployProcessorVersionRequest, dict]]):
                The request object. Request message for the deploy
                processor version method.
            name (:class:`str`):
                Required. The processor version
                resource name to be deployed.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.DeployProcessorVersionResponse`
                Response message for the deploy processor version
                method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.DeployProcessorVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.deploy_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.DeployProcessorVersionResponse,
            metadata_type=document_processor_service.DeployProcessorVersionMetadata,
        )

        # Done; return the response.
        return response

    async def undeploy_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.UndeployProcessorVersionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Undeploys the processor version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_undeploy_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.UndeployProcessorVersionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.undeploy_processor_version(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.UndeployProcessorVersionRequest, dict]]):
                The request object. Request message for the undeploy
                processor version method.
            name (:class:`str`):
                Required. The processor version
                resource name to be undeployed.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.UndeployProcessorVersionResponse`
                Response message for the undeploy processor version
                method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.UndeployProcessorVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.undeploy_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.UndeployProcessorVersionResponse,
            metadata_type=document_processor_service.UndeployProcessorVersionMetadata,
        )

        # Done; return the response.
        return response

    async def create_processor(
        self,
        request: Optional[
            Union[document_processor_service.CreateProcessorRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        processor: Optional[gcd_processor.Processor] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_processor.Processor:
        r"""Creates a processor from the type processor that the
        user chose. The processor will be at "ENABLED" state by
        default after its creation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_create_processor():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.CreateProcessorRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_processor(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.CreateProcessorRequest, dict]]):
                The request object. Request message for create a
                processor. Notice this request is sent to a regionalized
                backend service, and if the processor type is not
                available on that region, the creation will fail.
            parent (:class:`str`):
                Required. The parent (project and location) under which
                to create the processor. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            processor (:class:`google.cloud.documentai_v1beta3.types.Processor`):
                Required. The processor to be created, requires
                [processor_type] and [display_name] to be set. Also, the
                processor is under CMEK if CMEK fields are set.

                This corresponds to the ``processor`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.types.Processor:
                The first-class citizen for Document
                AI. Each processor defines how to
                extract structural information from a
                document.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, processor])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.CreateProcessorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if processor is not None:
            request.processor = processor

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_processor,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_processor(
        self,
        request: Optional[
            Union[document_processor_service.DeleteProcessorRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes the processor, unloads all deployed model
        artifacts if it was enabled and then deletes all
        artifacts associated with this processor.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_delete_processor():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.DeleteProcessorRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_processor(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.DeleteProcessorRequest, dict]]):
                The request object. Request message for the delete
                processor method.
            name (:class:`str`):
                Required. The processor resource name
                to be deleted.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.DeleteProcessorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_processor,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=document_processor_service.DeleteProcessorMetadata,
        )

        # Done; return the response.
        return response

    async def enable_processor(
        self,
        request: Optional[
            Union[document_processor_service.EnableProcessorRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Enables a processor

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_enable_processor():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.EnableProcessorRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.enable_processor(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.EnableProcessorRequest, dict]]):
                The request object. Request message for the enable
                processor method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.documentai_v1beta3.types.EnableProcessorResponse` Response message for the enable processor method.
                   Intentionally empty proto for adding fields in
                   future.

        """
        # Create or coerce a protobuf request object.
        request = document_processor_service.EnableProcessorRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.enable_processor,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.EnableProcessorResponse,
            metadata_type=document_processor_service.EnableProcessorMetadata,
        )

        # Done; return the response.
        return response

    async def disable_processor(
        self,
        request: Optional[
            Union[document_processor_service.DisableProcessorRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Disables a processor

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_disable_processor():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.DisableProcessorRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.disable_processor(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.DisableProcessorRequest, dict]]):
                The request object. Request message for the disable
                processor method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.documentai_v1beta3.types.DisableProcessorResponse` Response message for the disable processor method.
                   Intentionally empty proto for adding fields in
                   future.

        """
        # Create or coerce a protobuf request object.
        request = document_processor_service.DisableProcessorRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.disable_processor,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.DisableProcessorResponse,
            metadata_type=document_processor_service.DisableProcessorMetadata,
        )

        # Done; return the response.
        return response

    async def set_default_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.SetDefaultProcessorVersionRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Set the default (active) version of a
        [Processor][google.cloud.documentai.v1beta3.Processor] that will
        be used in
        [ProcessDocument][google.cloud.documentai.v1beta3.DocumentProcessorService.ProcessDocument]
        and
        [BatchProcessDocuments][google.cloud.documentai.v1beta3.DocumentProcessorService.BatchProcessDocuments].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_set_default_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.SetDefaultProcessorVersionRequest(
                    processor="processor_value",
                    default_processor_version="default_processor_version_value",
                )

                # Make the request
                operation = client.set_default_processor_version(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.SetDefaultProcessorVersionRequest, dict]]):
                The request object. Request message for the set default
                processor version method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.SetDefaultProcessorVersionResponse`
                Response message for set default processor version
                method.

        """
        # Create or coerce a protobuf request object.
        request = document_processor_service.SetDefaultProcessorVersionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_default_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("processor", request.processor),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.SetDefaultProcessorVersionResponse,
            metadata_type=document_processor_service.SetDefaultProcessorVersionMetadata,
        )

        # Done; return the response.
        return response

    async def review_document(
        self,
        request: Optional[
            Union[document_processor_service.ReviewDocumentRequest, dict]
        ] = None,
        *,
        human_review_config: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Send a document for Human Review. The input document
        should be processed by the specified processor.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_review_document():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                inline_document = documentai_v1beta3.Document()
                inline_document.uri = "uri_value"

                request = documentai_v1beta3.ReviewDocumentRequest(
                    inline_document=inline_document,
                    human_review_config="human_review_config_value",
                )

                # Make the request
                operation = client.review_document(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.ReviewDocumentRequest, dict]]):
                The request object. Request message for review document
                method.
            human_review_config (:class:`str`):
                Required. The resource name of the
                HumanReviewConfig that the document will
                be reviewed with.

                This corresponds to the ``human_review_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.ReviewDocumentResponse`
                Response message for review document method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([human_review_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.ReviewDocumentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if human_review_config is not None:
            request.human_review_config = human_review_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.review_document,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=120.0,
            ),
            default_timeout=120.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("human_review_config", request.human_review_config),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.ReviewDocumentResponse,
            metadata_type=document_processor_service.ReviewDocumentOperationMetadata,
        )

        # Done; return the response.
        return response

    async def evaluate_processor_version(
        self,
        request: Optional[
            Union[document_processor_service.EvaluateProcessorVersionRequest, dict]
        ] = None,
        *,
        processor_version: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Evaluates a ProcessorVersion against annotated
        documents, producing an Evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_evaluate_processor_version():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.EvaluateProcessorVersionRequest(
                    processor_version="processor_version_value",
                )

                # Make the request
                operation = client.evaluate_processor_version(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.EvaluateProcessorVersionRequest, dict]]):
                The request object. Evaluates the given ProcessorVersion
                against the supplied documents.
            processor_version (:class:`str`):
                Required. The resource name of the
                [ProcessorVersion][google.cloud.documentai.v1beta3.ProcessorVersion]
                to evaluate.
                ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``

                This corresponds to the ``processor_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.documentai_v1beta3.types.EvaluateProcessorVersionResponse`
                Metadata of the EvaluateProcessorVersion method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([processor_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.EvaluateProcessorVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if processor_version is not None:
            request.processor_version = processor_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.evaluate_processor_version,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("processor_version", request.processor_version),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            document_processor_service.EvaluateProcessorVersionResponse,
            metadata_type=document_processor_service.EvaluateProcessorVersionMetadata,
        )

        # Done; return the response.
        return response

    async def get_evaluation(
        self,
        request: Optional[
            Union[document_processor_service.GetEvaluationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> evaluation.Evaluation:
        r"""Retrieves a specific evaluation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_get_evaluation():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.GetEvaluationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.GetEvaluationRequest, dict]]):
                The request object. Retrieves a specific Evaluation.
            name (:class:`str`):
                Required. The resource name of the
                [Evaluation][google.cloud.documentai.v1beta3.Evaluation]
                to get.
                ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}/evaluations/{evaluation}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.types.Evaluation:
                An evaluation of a ProcessorVersion's
                performance.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.GetEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_evaluation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_evaluations(
        self,
        request: Optional[
            Union[document_processor_service.ListEvaluationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEvaluationsAsyncPager:
        r"""Retrieves a set of evaluations for a given processor
        version.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import documentai_v1beta3

            async def sample_list_evaluations():
                # Create a client
                client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

                # Initialize request argument(s)
                request = documentai_v1beta3.ListEvaluationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.documentai_v1beta3.types.ListEvaluationsRequest, dict]]):
                The request object. Retrieves a list of evaluations for
                a given ProcessorVersion.
            parent (:class:`str`):
                Required. The resource name of the
                [ProcessorVersion][google.cloud.documentai.v1beta3.ProcessorVersion]
                to list evaluations for.
                ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListEvaluationsAsyncPager:
                The response from ListEvaluations.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_processor_service.ListEvaluationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_evaluations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEvaluationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[operations_pb2.ListOperationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[operations_pb2.GetOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def cancel_operation(
        self,
        request: Optional[operations_pb2.CancelOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.CancelOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.cancel_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_location(
        self,
        request: Optional[locations_pb2.GetLocationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = locations_pb2.GetLocationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.get_location,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_locations(
        self,
        request: Optional[locations_pb2.ListLocationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Optional[float] = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = locations_pb2.ListLocationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.list_locations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-documentai",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DocumentProcessorServiceAsyncClient",)
