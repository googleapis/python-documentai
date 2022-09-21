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

from samples.snippets import delete_processor_version_sample

location = "us"
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
processor_id = "91e072f8626a76b7"
processor_version_id = "pretrained-ocr-v1.0-2020-09-23"


def test_delete_processor_version(capsys):
    delete_processor_version_sample.delete_processor_version_sample(
        project_id=project_id,
        location=location,
        processor_id=processor_id,
        processor_version_id=processor_version_id,
    )
    out, _ = capsys.readouterr()

    assert "DELETE" in out or "pretrained" in out or "operation" in out
