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
# Generated code. DO NOT EDIT!
#
# Snippet for FetchProcessorTypes
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-documentai


# [START documentai_v1_generated_DocumentProcessorService_FetchProcessorTypes_sync]
from google.cloud import documentai_v1


def sample_fetch_processor_types():
    # Create a client
    client = documentai_v1.DocumentProcessorServiceClient()

    # Initialize request argument(s)
    request = documentai_v1.FetchProcessorTypesRequest(
        parent="parent_value",
    )

    # Make the request
    response = client.fetch_processor_types(request=request)

    # Handle the response
    print(response)

# [END documentai_v1_generated_DocumentProcessorService_FetchProcessorTypes_sync]
