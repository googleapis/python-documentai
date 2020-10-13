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

# [START documentai_batch_process_documents_sample]
# from google.cloud import documentai.v1beta3 as documentai

from google.cloud.documentai_v1beta3.services.document_processor_service import (
    DocumentProcessorServiceClient
)
import tempfile

from google.cloud import storage
from uuid import uuid4
import json

project_id = 'YOUR_PROJECT_ID'
location = 'us'
processor_id = '90484cfdedb024f6'
gcs_input_uri = 'gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri = 'output-bucket'
gcs_output_uri_prefix = uuid4()

# [START document_ai_batch_process_document_sample]

# TODO(developer): Uncomment these variables before running the sample.
# project_id = 'YOUR_PROJECT_ID';
# location = 'YOUR_PROJECT_LOCATION'; // Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID';
# gcs_input_uri = 'YOUR_SOURCE_PDF';
# gcs_output_uri = 'YOUR_STORAGE_BUCKET';
# gcs_output_uri_prefix = 'YOUR_STORAGE_PREFIX';


def batch_process_documents_sample(project_id: str, location: str, processor_id: str, gcs_input_uri: str, gcs_output_uri: str, gcs_output_uri_prefix: str):

    client_options = dict(api_endpoint="us-documentai.googleapis.com")
    client = DocumentProcessorServiceClient(client_options=client_options)
    storage_client = storage.Client(project=project_id)
    name = "projects/{project}/locations/{location}/processors/{processor_id}".format(
        project=project_id, location=location, processor_id=processor_id
    )
    input_config = {
        "gcs_source": gcs_input_uri,
        "mime_type": 'application/pdf'
    }
    input_configs = [input_config]
    output_config = {
        "gcs_destination": "{gcs_output_uri}/{gcs_output_uri_prefix}"
    }
    # output_configs = [output_config]

    # Configure the batch process request.
    request = {
        'name': name,
        'input_configs': input_configs,
        'output_config': output_config
    }

    try:
        batch_process(request=request, client=client)
        # results_generator = 
        # for results in results_generator:
        #     result_list.extend(results)
    except TimeoutError as e:
        print("Uh-oh! - %s", e)

    print('Document processing complete.')

    # List all of the files in the Storage bucket
    bucket = storage_client.get_bucket(gcs_output_uri)
    print('Fetching results ...')
    blobs = bucket.list_blobs(prefix=gcs_output_uri_prefix)
    for blob in blobs:
        if (blob.exists):
            print("Fetched file")

        # Download and store json data in a temp file.
        temporary_file = tempfile.TemporaryFile()
        with open(tempfile, "wb"):
            blob.download_to_file(temporary_file)
        # Parse json file into Document
        document = json.loads(temporary_file)

        text = dict(document)

        # Get all of the document text as one big string

        # Read the text recognition output from the processor
        print('The document contains the following paragraphs:')

        [page1] = document.pages
        paragraphs = dict(page1)

        for paragraph in paragraphs:
            paragraph_text = get_text(paragraph.layout.text_anchor, text)
            print('Paragraph Text: \n{paragraph_text}', paragraph_text)

        # Form parsing provides additional output about
        # form-formatted PDFs. You  must create a form
        # processor in the Cloud Console to see full field details.
        print('\nThe following form key/value pairs were detected:')

        form_fields = dict(page1)
        for field in form_fields:
            field_name = get_text(field.field_name.text_anchor, text)
            field_value = get_text(field.field_value.text_anchor, text)

            print('Extracted key value pair:')
            print('\t{field_name},{field_value}', field_name, field_value)

        temporary_file.close()


def batch_process(request: dict, client: DocumentProcessorServiceClient):
    while True:
        yield client.batch_process_documents(request=request)


def get_text(text_anchor: dict, text: str):
    if (len(text_anchor.text_segments) > 0 or text_anchor.text_segments is not None):
        start_index = text_anchor.text_segments[0].start_index if text_anchor.text_segments[0].start_index is not None else 0
        end_index = text_anchor.text_segments[0].end_index

        return text.substring(start_index, end_index)
    else:
        return "[NO TEXT]"

# [END documentai_batch_process_documents_sample]