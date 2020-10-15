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

from google.cloud import documentai_v1beta3 as documentai

project_id = 'YOUR_PROJECT_ID'
location = 'us'
processor_id = '90484cfdedb024f6'
gcs_input_uri = 'gs://cloud-samples-data/documentai/invoice.pdf'
gcs_output_uri = 'output-bucket'

# [START documentai_process_document_sample]

# TODO(developer): Uncomment these variables before running the sample.
# project_id= 'YOUR_PROJECT_ID';
# location = 'YOUR_PROJECT_LOCATION'; // Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID'; // Create processor in Cloud Console
# file_path = '/path/to/local/pdf';


def process_document_sample(project_id: str, location: str, processor_id: str, file_path: str):
    client_options = dict(api_endpoint="us-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=client_options)

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    name = f'projects/{project_id}/locations/{location}/processors/{processor_id}'

    with open(file_path, 'rb') as image:
        image_content = image.read()

    # Read the file into memory
    document = {
        'content': image_content,
        'mime_type': 'application/pdf'
    }

    # Configure the process request
    request = {
        'name': name,
        'document': document
    }

    result = client.process_document(request=request)

    print('Document processing complete.')

    document = result.document
    text = document.text

    page_1 = document.pages[0]
    paragraphs = page_1.paragraphs

    for paragraph in paragraphs:
        paragraph_text = get_text(paragraph.layout.text_anchor, text)
        print(f'Paragraph text: {paragraph_text}')


def get_text(text_anchor: dict, text: str):
    # First shard in document doesn't have startIndex property
    start_index = text_anchor.text_segments[0].start_index if text_anchor.text_segments[0].start_index is not None else 0
    end_index = text_anchor.text_segments[0].end_index

    return text[start_index:end_index]

# [END documentai_process_document_sample]
