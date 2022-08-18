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

import os
from uuid import uuid4

from google.cloud import documentai
from google.cloud.exceptions import NotFound
import pytest
from samples.snippets import delete_processor_sample

location = "us"
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
processor_display_name = f"test-processor-{uuid4()}"
processor_type = "OCR_PROCESSOR"


@pytest.fixture(scope="module")
def test_processor():
    client = documentai.DocumentProcessorServiceClient()
    parent = client.common_location_path(project_id, location)
    processor = client.create_processor(
        parent=parent,
        processor=documentai.Processor(
            display_name=processor_display_name, type_=processor_type
        ),
    )
    yield processor


def test_delete_processor(capsys, test_processor):
    client = documentai.DocumentProcessorServiceClient()
    processor_id = client.parse_processor_path(test_processor.name)["processor"]

    delete_processor_sample.delete_processor_sample(
        project_id=project_id, location=location, processor_id=processor_id
    )
    out, _ = capsys.readouterr()

    assert "projects" in out
    assert "locations" in out
    assert "operations" in out
