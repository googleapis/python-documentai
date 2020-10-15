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

    def _get_text(el):
        """Doc AI identifies form fields by their offsets
        in document text. This function converts offsets
        to text snippets.
        """
        response = ''
        # If a text segment spans several lines, it will
        # be stored in different text segments.
        for segment in el.text_anchor.text_segments:
            start_index = int(segment.start_index) if segment.start_index in el.text_anchor.text_segments else 0
            end_index = int(segment.end_index)
            response += document.text[start_index:end_index]
        return response

    print('Document processing complete.')

    document = result.document

    page_1 = document.pages[0]
    paragraphs = page_1.paragraphs

    for paragraph in paragraphs:
        paragraph_text = _get_text(paragraph.layout)
        print(f'Paragraph text: {paragraph_text}')

# [END documentai_process_document_sample]
