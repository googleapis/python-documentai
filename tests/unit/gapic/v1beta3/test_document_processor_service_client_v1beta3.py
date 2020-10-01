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

"""Unit tests."""

import mock
import pytest

from google.rpc import status_pb2

from google.cloud.documentai import v1beta3
from google.cloud.documentai.v1beta3.proto import document_processor_service_pb2
from google.longrunning import operations_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestDocumentProcessorServiceClient(object):
    def test_process_document(self):
        # Setup Expected Response
        human_review_operation = "humanReviewOperation2074827282"
        expected_response = {"human_review_operation": human_review_operation}
        expected_response = document_processor_service_pb2.ProcessResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1beta3.DocumentProcessorServiceClient()

        # Setup Request
        name = client.processor_path("[PROJECT]", "[LOCATION]", "[PROCESSOR]")

        response = client.process_document(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = document_processor_service_pb2.ProcessRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_process_document_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1beta3.DocumentProcessorServiceClient()

        # Setup request
        name = client.processor_path("[PROJECT]", "[LOCATION]", "[PROCESSOR]")

        with pytest.raises(CustomException):
            client.process_document(name)

    def test_batch_process_documents(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = document_processor_service_pb2.BatchProcessResponse(
            **expected_response
        )
        operation = operations_pb2.Operation(
            name="operations/test_batch_process_documents", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1beta3.DocumentProcessorServiceClient()

        # Setup Request
        name = client.processor_path("[PROJECT]", "[LOCATION]", "[PROCESSOR]")

        response = client.batch_process_documents(name)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = document_processor_service_pb2.BatchProcessRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_process_documents_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_batch_process_documents_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1beta3.DocumentProcessorServiceClient()

        # Setup Request
        name = client.processor_path("[PROJECT]", "[LOCATION]", "[PROCESSOR]")

        response = client.batch_process_documents(name)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_review_document(self):
        # Setup Expected Response
        gcs_destination = "gcsDestination714819302"
        expected_response = {"gcs_destination": gcs_destination}
        expected_response = document_processor_service_pb2.ReviewDocumentResponse(
            **expected_response
        )
        operation = operations_pb2.Operation(
            name="operations/test_review_document", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1beta3.DocumentProcessorServiceClient()

        # Setup Request
        human_review_config = client.human_review_config_path(
            "[PROJECT]", "[LOCATION]", "[PROCESSOR]"
        )

        response = client.review_document(human_review_config)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = document_processor_service_pb2.ReviewDocumentRequest(
            human_review_config=human_review_config
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_review_document_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_review_document_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1beta3.DocumentProcessorServiceClient()

        # Setup Request
        human_review_config = client.human_review_config_path(
            "[PROJECT]", "[LOCATION]", "[PROCESSOR]"
        )

        response = client.review_document(human_review_config)
        exception = response.exception()
        assert exception.errors[0] == error
