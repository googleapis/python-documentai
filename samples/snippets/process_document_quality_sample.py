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

# [START documentai_process_form_document]

# TODO(developer): Uncomment these variables before running the sample.
# project_id= 'YOUR_PROJECT_ID'
# location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID' # Create processor in Cloud Console
# file_path = '/path/to/local/pdf'

def process_document_quality_sample(
    project_id: str, location: str, processor_id: str, file_path: str
):
    from google.cloud import documentai_v1 as documentai

    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = {}
    if location == "eu":
        opts = {"api_endpoint": "eu-documentai.googleapis.com"}

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as image:
        image_content = image.read()

    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "raw_document": document}

    # Recognizes text entities in the PDF document
    result = client.process_document(request=request)

    print("Document processing complete.\n")

    # Read the quality output from the processor.
    # For a full list of Document object attributes, please reference this page: https://googleapis.dev/python/documentai/latest/_modules/google/cloud/documentai_v1beta3/types/document.html#Document
    document = result.document
    page_quality_score = []
    category_quality_scores = []
    for entity in document.entities:
        conf_percent = '{:.1%}'.format(entity.confidence)
        num = page_anchor_to_num(entity.page_anchor)
        print(f'Page {num} has a quality score of {conf_percent}:')
        for prop in entity.properties:
            conf_percent = '{:.1%}'.format(prop.confidence)
            # remove prefix string "quality/"
            category = prop.type_[len("quality/"):]
            print(f'    * {category} score of {conf_percent}')


def page_anchor_to_num(page_anchor: dict) -> str:
    try:
        return str(int(page_anchor.page_refs.page) + 1)
    except AttributeError:
        return "1"

# [END documentai_process_form_document]
