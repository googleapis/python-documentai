# # Copyright 2020 Google LLC
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

from samples import quickstart_sample_v1beta3


location = "us"
project_id = '1012616486416'
processor_id = '90484cfdedb024f6'
bucket_name = 'python_docs_samples_test_%s' % uuid4()
gcs_input_uri = 'gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri = 'output-bucket'
gcs_output_uri_prefix = uuid4()
file_name = 'samples/resources/invoice.pdf'
file_path = os.path.join(os.getcwd(), file_name)

name = "projects/1012616486416/locations/us/processors/90484cfdedb024f6"


@pytest.fixture(scope="module")
def setup():
    storage_client = storage.Client()
    storage_client.bucket(bucket_name)


@pytest.fixture(scope="module")
def tear_down():
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=gcs_output_uri_prefix)

    for blob in blobs:
        blob.delete()

        bucket.delete()


def test_quickstart(capsys):
    quickstart_sample_v1beta3.quickstart(project_id=project_id, location=location, processor_id=processor_id, file_path=file_path)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    assert "Paragraph" in out
