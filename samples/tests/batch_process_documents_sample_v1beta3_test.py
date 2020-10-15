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
from google.cloud import storage

from samples import batch_process_documents_sample_v1beta3

project_id = 'python-docs-samples-tests'
location = 'us'
processor_id = '90484cfdedb024f6'
gcs_input_uri = 'gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri = 'gs://document-ai-python'
gcs_output_uri_prefix = uuid4()


@pytest.fixture(scope="module")
def setup():
    storage_client = storage.Client()
    storage_client.create_bucket(gcs_output_uri)


@pytest.fixture(scope="module")
def tear_down():
    storage_client = storage.Client()
    bucket = storage_client.bucket(gcs_output_uri, prefix=gcs_output_uri_prefix)
    blobs = storage_client.list_blobs(bucket)

    for blob in blobs:
        blob.delete()

    bucket.delete()


def test_batch_process_documents(capsys):
    batch_process_documents_sample_v1beta3.batch_process_documents(project_id=project_id, location=location, processor_id=processor_id, gcs_input_uri=gcs_input_uri, gcs_output_uri=gcs_output_uri, gcs_output_uri_prefix=gcs_output_uri_prefix)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert "Extracted" in out
    assert "Paragraph" in out
