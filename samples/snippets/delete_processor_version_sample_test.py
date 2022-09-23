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

import mock
from samples.snippets import delete_processor_version_sample

location = "us"
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
processor_id = "aaaaaaaaa"
processor_version_id = "xxxxxxxxxx"


@mock.patch(
    "google.cloud.documentai.DocumentProcessorServiceClient.delete_processor_version"
)
@mock.patch("google.api_core.operation.Operation")
def test_delete_processor_version(
    operation_mock, delete_processor_version_mock, capsys
):
    delete_processor_version_mock.return_value = operation_mock

    delete_processor_version_sample.delete_processor_version_sample(
        project_id=project_id,
        location=location,
        processor_id=processor_id,
        processor_version_id=processor_version_id,
    )

    delete_processor_version_mock.assert_called_once()

    out, _ = capsys.readouterr()

    assert "operation" in out
