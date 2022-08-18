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
from samples.snippets import create_processor_sample

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

    try:
        client.delete_processor(processor.name)
    except NotFound as e:
        print(e.message)


def test_create_processor(capsys, test_processor):
    create_processor_sample.create_processor_sample(
        project_id=project_id,
        location=location,
        processor_display_name=test_processor.display_name,
        processor_type=test_processor.type_,
    )
    out, _ = capsys.readouterr()

    assert "Processor Name:" in out
    assert "Processor Display Name:" in out
    assert "Processor Type: OCR_PROCESSOR" in out
