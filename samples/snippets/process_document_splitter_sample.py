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

def process_document_splitter_sample(
        project_id: str,
        location: str,
        processor_id: str,
        file_path: str):
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

    # Read the splitter output from the splitter processor.
    document = result.document
    print(f'Found {len(document.entities)} subdocuments:')
    for entity in document.entities:
        conf_percent = '{:.1%}'.format(entity.confidence)
        pages_range = page_refs_to_string(entity.page_anchor.page_refs)
        # Print subdocument type information, if available
        try:
            doctype = entity.type
            print(f'{conf_percent} confident that {pages_range} a "{doctype}" subdocument.')
        except AttributeError:
            print(f'{conf_percent} confident that {pages_range} a subdocument.')


def page_refs_to_string(page_refs: dict) -> str:
    ''' Converts a page ref to a string describing the page or page range.'''
    if len(page_refs) == 1:
        num = page_refs[0].page
        if not num:
            num = "0"
        # Increase page number by one to account for 0-indexing
        # e.g. the first page should be "page 1" not "page 0"
        num = str(int(num) + 1)
        return f'page {num} is'
    else:
        start = page_refs[0].page
        if not start:
            start = "0"
        end = page_refs[1].page
        # Increase page number by one to account for 0-indexing
        # e.g. the first page should be "page 1" not "page 0"
        start = str(int(start) + 1)
        end = str(int(end) + 1)
        return f'pages {start} to {end} are'

# [END documentai_process_form_document]
