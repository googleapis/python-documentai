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
# Snippet for ProcessDocument
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-documentai


# [START documentai_v1_generated_DocumentProcessorService_ProcessDocument_sync]
from google.cloud import documentai_v1


def sample_process_document(name, uri):
    # Create a client
    client = documentai_v1.DocumentProcessorServiceClient()

    # Initialize request argument(s)
    inline_document = documentai_v1.Document()
    inline_document.uri = uri

    request = documentai_v1.ProcessRequest(
        inline_document=inline_document,
        name=name,
    )

    # Make the request
    response = client.process_document(request=request)

    # Handle the response
    print(response)

# [END documentai_v1_generated_DocumentProcessorService_ProcessDocument_sync]
sample_process_document("projects/182397877917/locations/us/processors/4e4c13fea46df893", "gs://akitsch-content/invoice.pdf")