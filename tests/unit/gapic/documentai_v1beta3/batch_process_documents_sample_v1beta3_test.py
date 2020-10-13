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

from uuid import uuid4
import pytest
import sys
import os
from google.cloud import storage
import google.api_core as api_core

from samples import batch_process_documents_sample_v1beta3

from google.cloud.documentai_v1beta3.services.document_processor_service import (
    DocumentProcessorServiceClient,
)
from google.cloud.documentai_v1beta3.services.document_processor_service import (
    transports,
)
from google.cloud.documentai_v1beta3.types import document
from google.cloud.documentai_v1beta3.types import document_processor_service
from google.cloud.documentai_v1beta3.types import geometry
from google.cloud.documentai_v1beta3.types import BatchProcessRequest


location = "us"
project_id = '1012616486416'
processor_id = '90484cfdedb024f6'
bucket_name = 'python_docs_samples_test_%s' %uuid4()
gcs_input_uri ='gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri = 'output_bucket'
gcs_output_uri_prefix = uuid4()

test_process_document = {
'project_id': project_id,
'location': location,
'processor_id': '90484cfdedb024f6',
'gcs_input_uri': 'gs://cloud-samples-data/documentai/invoice.pdf',
'gcs_output_uri_prefix': uuid4(),
}

name = "projects/1012616486416/locations/us/processors/90484cfdedb024f6"

client_options = dict(api_endpoint="us-documentai.googleapis.com")
client = DocumentProcessorServiceClient(client_options=client_options)
# input_config = BatchProcessRequest.BatchInputConfig()
# input_config.gcs_source = 'gs://cloud-samples-data/documentai/invoice.pdf'
# input_config.mime_type = 'application/pdf'

# output_config = {
# 	"gcs_destination": "{gcs_output_uri}/{gcs_output_uri_prefix}"
# }
# output_config = BatchProcessRequest.BatchOutputConfig(output_config)


# request = BatchProcessRequest(name=name, input_configs=[input_configs], output_config=output_config)

@pytest.fixture(scope="module")
def setup():
	storage_client = storage.Client()
	storage_client.bucket(bucket_name)
	# bout = io.BytesIO
	# original_print_stream = sys.stdout
	# sys.stdout = test_stdout = bout

@pytest.fixture(scope="module")
def tear_down():
	storage_client = storage.Client()
	bucket = storage_client.bucket(bucket_name)
	blobs = bucket.list_blobs(prefix=test_process_document.get('gcs_output_uri_prefix'))

	for blob in blobs:
		blob.delete()

	bucket.delete()

def test_batch_process_documents():
	response = batch_process_documents_sample_v1beta3.batch_process_documents_sample(project_id=project_id, location=location, processor_id=processor_id, gcs_input_uri=gcs_input_uri, gcs_output_uri=gcs_output_uri, gcs_output_uri_prefix=gcs_output_uri_prefix)
	# response = client.batch_process_documents(request=request)
	# got = str(bout)
	# assert "Paragraph text:" in got
	# assert "Extracted:" in got
	assert isinstance(response, api_core.operation.Operation)

	# sys.stdout = original_print_stream

# TODO - since I'm doing this synchronously, I need to figure out a way to get/assert against the BatchProcessResponse 