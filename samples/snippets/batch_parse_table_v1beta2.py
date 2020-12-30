# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START documentai_batch_parse_table]
import re

from google.cloud import documentai_v1beta2 as documentai
from google.cloud import storage

# TODO(developer): Uncomment these variables before running the sample.
# project_id= 'YOUR_PROJECT_ID'
# location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID' # Create processor in Cloud Console
# gcs_input_uri = "YOUR_INPUT_URI"
# gcs_output_uri = "YOUR_OUTPUT_BUCKET_URI"
# gcs_output_uri_prefix = "YOUR_OUTPUT_URI_PREFIX"


def batch_parse_table(
    project_id,
    location,
    gcs_input_uri,
    gcs_output_uri,
    gcs_output_uri_prefix,
    timeout: int = 300,
):

    client = documentai.DocumentUnderstandingServiceClient()

    destination_uri = f"{gcs_output_uri}/{gcs_output_uri_prefix}/"

    gcs_source = documentai.types.document_understanding.GcsSource(uri=gcs_input_uri)

    # 'mime_type' can be 'application/pdf', 'image/tiff',
    # and 'image/gif', or 'application/json'
    input_config = documentai.types.document_understanding.InputConfig(
        gcs_source=gcs_source, mime_type="application/pdf"
    )

    gcs_destination = documentai.types.document_understanding.GcsDestination(
        uri=gcs_input_uri
    )

    # Where to write results
    output_config = documentai.types.document_understanding.OutputConfig(
        gcs_destination=gcs_destination, pages_per_shard=1
    )

    bounding_box = documentai.types.geometry.BoundingPoly(
        normalized_vertices=[
            {"x": 0, "y": 0},
            {"x": 1, "y": 0},
            {"x": 1, "y": 1},
            {"x": 0, "y": 1},
        ]
    )

    table_bound_hints = documentai.types.document_understanding.TableBoundHint(
        bounding_box=bounding_box
    )

    table_extraction_params = (
        documentai.types.document_understanding.TableExtractionParams(
            enabled=True, table_bound_hints=[table_bound_hints]
        )
    )

    # Location can be 'us' or 'eu'
    parent = f"projects/{project_id}/locations/{location}"

    request = documentai.types.document_understanding.ProcessDocumentRequest(
        input_config=input_config,
        output_config=output_config,
        table_extraction_params=table_extraction_params,
    )

    requests = documentai.types.document_understanding.BatchProcessDocumentsRequest(
        parent=parent, requests=[request]
    )

    operation = client.batch_process_documents(requests)

    # Wait for the operation to finish
    operation.result(timeout=timeout)


# [END documentai_batch_parse_table]
