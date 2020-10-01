# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.documentai.v1beta3 DocumentProcessorService API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.path_template
import grpc

from google.cloud.documentai.v1beta3.gapic import (
    document_processor_service_client_config,
)
from google.cloud.documentai.v1beta3.gapic import enums
from google.cloud.documentai.v1beta3.gapic.transports import (
    document_processor_service_grpc_transport,
)
from google.cloud.documentai.v1beta3.proto import document_pb2
from google.cloud.documentai.v1beta3.proto import document_processor_service_pb2
from google.cloud.documentai.v1beta3.proto import document_processor_service_pb2_grpc
from google.longrunning import operations_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-documentai",
).version


class DocumentProcessorServiceClient(object):
    """
    Service to call Cloud DocumentAI to process documents according to the
    processor's definition. Processors are built using state-of-the-art Google
    AI such as natural language, computer vision, and translation to extract
    structured information from unstructured or semi-structured documents.
    """

    SERVICE_ADDRESS = "us-documentai.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.documentai.v1beta3.DocumentProcessorService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentProcessorServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def human_review_config_path(cls, project, location, processor):
        """Return a fully-qualified human_review_config string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/processors/{processor}/humanReviewConfig",
            project=project,
            location=location,
            processor=processor,
        )

    @classmethod
    def processor_path(cls, project, location, processor):
        """Return a fully-qualified processor string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/processors/{processor}",
            project=project,
            location=location,
            processor=processor,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.DocumentProcessorServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.DocumentProcessorServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = document_processor_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=document_processor_service_grpc_transport.DocumentProcessorServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = document_processor_service_grpc_transport.DocumentProcessorServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def process_document(
        self,
        name,
        document=None,
        skip_human_review=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Processes a single document.

        Example:
            >>> from google.cloud.documentai import v1beta3
            >>>
            >>> client = v1beta3.DocumentProcessorServiceClient()
            >>>
            >>> name = client.processor_path('[PROJECT]', '[LOCATION]', '[PROCESSOR]')
            >>>
            >>> response = client.process_document(name)

        Args:
            name (str): Required. The processor resource name.
            document (Union[dict, ~google.cloud.documentai.v1beta3.types.Document]): The document payload, the [content] and [mime_type] fields must be
                set.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.documentai.v1beta3.types.Document`
            skip_human_review (bool): Whether Human Review feature should be skipped for this request. Default to
                false.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.documentai.v1beta3.types.ProcessResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "process_document" not in self._inner_api_calls:
            self._inner_api_calls[
                "process_document"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.process_document,
                default_retry=self._method_configs["ProcessDocument"].retry,
                default_timeout=self._method_configs["ProcessDocument"].timeout,
                client_info=self._client_info,
            )

        request = document_processor_service_pb2.ProcessRequest(
            name=name, document=document, skip_human_review=skip_human_review,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["process_document"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_process_documents(
        self,
        name,
        input_configs=None,
        output_config=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        LRO endpoint to batch process many documents. The output is written
        to Cloud Storage as JSON in the [Document] format.

        Example:
            >>> from google.cloud.documentai import v1beta3
            >>>
            >>> client = v1beta3.DocumentProcessorServiceClient()
            >>>
            >>> name = client.processor_path('[PROJECT]', '[LOCATION]', '[PROCESSOR]')
            >>>
            >>> response = client.batch_process_documents(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. The processor resource name.
            input_configs (list[Union[dict, ~google.cloud.documentai.v1beta3.types.BatchInputConfig]]): The input config for each single document in the batch process.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.documentai.v1beta3.types.BatchInputConfig`
            output_config (Union[dict, ~google.cloud.documentai.v1beta3.types.BatchOutputConfig]): The overall output config for batch process.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.documentai.v1beta3.types.BatchOutputConfig`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.documentai.v1beta3.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_process_documents" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_process_documents"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_process_documents,
                default_retry=self._method_configs["BatchProcessDocuments"].retry,
                default_timeout=self._method_configs["BatchProcessDocuments"].timeout,
                client_info=self._client_info,
            )

        request = document_processor_service_pb2.BatchProcessRequest(
            name=name, input_configs=input_configs, output_config=output_config,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["batch_process_documents"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            document_processor_service_pb2.BatchProcessResponse,
            metadata_type=document_processor_service_pb2.BatchProcessMetadata,
        )

    def review_document(
        self,
        human_review_config,
        document=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Send a document for Human Review. The input document should be processed by
        the specified processor.

        Example:
            >>> from google.cloud.documentai import v1beta3
            >>>
            >>> client = v1beta3.DocumentProcessorServiceClient()
            >>>
            >>> human_review_config = client.human_review_config_path('[PROJECT]', '[LOCATION]', '[PROCESSOR]')
            >>>
            >>> response = client.review_document(human_review_config)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            human_review_config (str): Required. The resource name of the HumanReviewConfig that the document will be
                reviewed with.
            document (Union[dict, ~google.cloud.documentai.v1beta3.types.Document]): The document that needs human review.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.documentai.v1beta3.types.Document`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.documentai.v1beta3.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "review_document" not in self._inner_api_calls:
            self._inner_api_calls[
                "review_document"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.review_document,
                default_retry=self._method_configs["ReviewDocument"].retry,
                default_timeout=self._method_configs["ReviewDocument"].timeout,
                client_info=self._client_info,
            )

        request = document_processor_service_pb2.ReviewDocumentRequest(
            human_review_config=human_review_config, document=document,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("human_review_config", human_review_config)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        operation = self._inner_api_calls["review_document"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            document_processor_service_pb2.ReviewDocumentResponse,
            metadata_type=document_processor_service_pb2.ReviewDocumentOperationMetadata,
        )
