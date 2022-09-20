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

# [START documentai_set_default_processor_version]

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import NotFound
from google.cloud import documentai

# TODO(developer): Uncomment these variables before running the sample.
# project_id = 'YOUR_PROJECT_ID'
# location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID'
# processor_version_id = 'YOUR_PROCESSOR_VERSION_ID'


def set_default_processor_version_sample(
    project_id: str, location: str, processor_id: str, processor_version_id: str
):
    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor
    # e.g.: projects/project_id/locations/location/processors/processor_id
    processor = client.processor_path(project_id, location, processor_id)

    # The full resource name of the processor version
    # e.g.: projects/project_id/locations/location/processors/processor_id/processorVersions/processor_version_id
    processor_version = client.processor_version_path(
        project_id, location, processor_id, processor_version_id
    )

    request = documentai.SetDefaultProcessorVersionRequest(
        processor=processor, default_processor_version=processor_version
    )

    # Make SetDefaultProcessorVersion request
    try:
        operation = client.set_default_processor_version(request)
        # Print operation details
        print(operation.operation.name)
        # Wait for operation to complete
        operation.result()
    except NotFound as e:
        print(e.message)


# [END documentai_set_default_processor_version]
