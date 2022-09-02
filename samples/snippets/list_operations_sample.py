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

# [START documentai_list_operations]

from google.api_core.client_options import ClientOptions
from google.longrunning.operations_pb2 import ListOperationsRequest
from google.cloud import documentai

# TODO(developer): Uncomment these variables before running the sample.
# project_id = 'YOUR_PROJECT_ID'
# location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'

# Create filter in https://google.aip.dev/160 syntax
# For full options, refer to:
# https://cloud.google.com/document-ai/docs/long-running-operations#listing_long-running_operations
# operations_filter = 'YOUR_FILTER'

# Example:
# operations_filter = "TYPE=BATCH_PROCESS_DOCUMENTS AND STATE=RUNNING"


def list_operations_sample(project_id: str, location: str, operations_filter: str):
    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # Format: projects/project_id/locations/location
    name = client.common_location_path(project=project_id, location=location)
    request = ListOperationsRequest(
        name=f"{name}/operations",
        filter=operations_filter,
    )

    # Make ListOperations request
    operations = client.list_operations(request=request)

    # Print the Operation Information
    print(operations)


# [END documentai_list_operations]
