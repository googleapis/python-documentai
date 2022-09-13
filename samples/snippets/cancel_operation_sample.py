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

# [START documentai_cancel_operation]

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import FailedPrecondition, NotFound
from google.cloud import documentai
from google.longrunning.operations_pb2 import CancelOperationRequest

# TODO(developer): Uncomment these variables before running the sample.
# location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
# operation_name = 'YOUR_OPERATION_NAME' # Format is 'projects/project_id/locations/location/operations/operation_id'


def cancel_operation_sample(location: str, operation_name: str):
    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    request = CancelOperationRequest(name=operation_name)

    # Make CancelOperation request
    try:
        client.cancel_operation(request=request)
        print(f"Operation {operation_name} cancelled")
    except (FailedPrecondition, NotFound) as e:
        print(e.message)


# [END documentai_cancel_operation]
