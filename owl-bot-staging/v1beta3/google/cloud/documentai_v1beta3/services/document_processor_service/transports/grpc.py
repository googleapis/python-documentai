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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.documentai_v1beta3.types import document_processor_service
from google.cloud.documentai_v1beta3.types import processor as gcd_processor
from google.longrunning import operations_pb2  # type: ignore
from .base import DocumentProcessorServiceTransport, DEFAULT_CLIENT_INFO


class DocumentProcessorServiceGrpcTransport(DocumentProcessorServiceTransport):
    """gRPC backend transport for DocumentProcessorService.

    Service to call Cloud DocumentAI to process documents
    according to the processor's definition. Processors are built
    using state-of-the-art Google AI such as natural language,
    computer vision, and translation to extract structured
    information from unstructured or semi-structured documents.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'documentai.googleapis.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(cls,
                       host: str = 'documentai.googleapis.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def process_document(self) -> Callable[
            [document_processor_service.ProcessRequest],
            document_processor_service.ProcessResponse]:
        r"""Return a callable for the process document method over gRPC.

        Processes a single document.

        Returns:
            Callable[[~.ProcessRequest],
                    ~.ProcessResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'process_document' not in self._stubs:
            self._stubs['process_document'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/ProcessDocument',
                request_serializer=document_processor_service.ProcessRequest.serialize,
                response_deserializer=document_processor_service.ProcessResponse.deserialize,
            )
        return self._stubs['process_document']

    @property
    def batch_process_documents(self) -> Callable[
            [document_processor_service.BatchProcessRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the batch process documents method over gRPC.

        LRO endpoint to batch process many documents. The output is
        written to Cloud Storage as JSON in the [Document] format.

        Returns:
            Callable[[~.BatchProcessRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'batch_process_documents' not in self._stubs:
            self._stubs['batch_process_documents'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/BatchProcessDocuments',
                request_serializer=document_processor_service.BatchProcessRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['batch_process_documents']

    @property
    def fetch_processor_types(self) -> Callable[
            [document_processor_service.FetchProcessorTypesRequest],
            document_processor_service.FetchProcessorTypesResponse]:
        r"""Return a callable for the fetch processor types method over gRPC.

        Fetches processor types.

        Returns:
            Callable[[~.FetchProcessorTypesRequest],
                    ~.FetchProcessorTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'fetch_processor_types' not in self._stubs:
            self._stubs['fetch_processor_types'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/FetchProcessorTypes',
                request_serializer=document_processor_service.FetchProcessorTypesRequest.serialize,
                response_deserializer=document_processor_service.FetchProcessorTypesResponse.deserialize,
            )
        return self._stubs['fetch_processor_types']

    @property
    def list_processors(self) -> Callable[
            [document_processor_service.ListProcessorsRequest],
            document_processor_service.ListProcessorsResponse]:
        r"""Return a callable for the list processors method over gRPC.

        Lists all processors which belong to this project.

        Returns:
            Callable[[~.ListProcessorsRequest],
                    ~.ListProcessorsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_processors' not in self._stubs:
            self._stubs['list_processors'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/ListProcessors',
                request_serializer=document_processor_service.ListProcessorsRequest.serialize,
                response_deserializer=document_processor_service.ListProcessorsResponse.deserialize,
            )
        return self._stubs['list_processors']

    @property
    def create_processor(self) -> Callable[
            [document_processor_service.CreateProcessorRequest],
            gcd_processor.Processor]:
        r"""Return a callable for the create processor method over gRPC.

        Creates a processor from the type processor that the
        user chose. The processor will be at "ENABLED" state by
        default after its creation.

        Returns:
            Callable[[~.CreateProcessorRequest],
                    ~.Processor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_processor' not in self._stubs:
            self._stubs['create_processor'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/CreateProcessor',
                request_serializer=document_processor_service.CreateProcessorRequest.serialize,
                response_deserializer=gcd_processor.Processor.deserialize,
            )
        return self._stubs['create_processor']

    @property
    def delete_processor(self) -> Callable[
            [document_processor_service.DeleteProcessorRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the delete processor method over gRPC.

        Deletes the processor, unloads all deployed model
        artifacts if it was enabled and then deletes all
        artifacts associated with this processor.

        Returns:
            Callable[[~.DeleteProcessorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_processor' not in self._stubs:
            self._stubs['delete_processor'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/DeleteProcessor',
                request_serializer=document_processor_service.DeleteProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['delete_processor']

    @property
    def enable_processor(self) -> Callable[
            [document_processor_service.EnableProcessorRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the enable processor method over gRPC.

        Enables a processor

        Returns:
            Callable[[~.EnableProcessorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'enable_processor' not in self._stubs:
            self._stubs['enable_processor'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/EnableProcessor',
                request_serializer=document_processor_service.EnableProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['enable_processor']

    @property
    def disable_processor(self) -> Callable[
            [document_processor_service.DisableProcessorRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the disable processor method over gRPC.

        Disables a processor

        Returns:
            Callable[[~.DisableProcessorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'disable_processor' not in self._stubs:
            self._stubs['disable_processor'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/DisableProcessor',
                request_serializer=document_processor_service.DisableProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['disable_processor']

    @property
    def review_document(self) -> Callable[
            [document_processor_service.ReviewDocumentRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the review document method over gRPC.

        Send a document for Human Review. The input document
        should be processed by the specified processor.

        Returns:
            Callable[[~.ReviewDocumentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'review_document' not in self._stubs:
            self._stubs['review_document'] = self.grpc_channel.unary_unary(
                '/google.cloud.documentai.v1beta3.DocumentProcessorService/ReviewDocument',
                request_serializer=document_processor_service.ReviewDocumentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['review_document']

    def close(self):
        self.grpc_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = (
    'DocumentProcessorServiceGrpcTransport',
)