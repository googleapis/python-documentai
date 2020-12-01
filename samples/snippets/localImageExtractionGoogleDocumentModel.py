from google.cloud import vision
import io
import os
import re
from google.cloud import documentai_v1beta3 as documentai
from google.cloud import storage

def process_document_sample(project_id: str, location: str, processor_id: str, file_path: str):
    # Instantiates a client
    client = documentai.DocumentProcessorServiceClient()
    #client = DocumentProcessorServiceClientUs()
    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first

    #name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    #name =  "https://us-documentai.googleapis.com/v1beta3/projects/poc-lab-280103/locations/us/processors/be6f7b359ec71fc9:process"
    #name = "v1beta3/projects/poc-lab-280103/locations/us/processors/be6f7b359ec71fc9:process"
    #name = "projects/poc-lab-280103/locations/us"
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "document": document}
    
    # Recognizes text entities in the PDF document
    result = client.process_document(request=request)
    print("Llegue perros")
    document = result.document

    print("Document processing complete.")

    # For a full list of Document object attributes, please reference this page: https://googleapis.dev/python/documentai/latest/_modules/google/cloud/documentai_v1beta3/types/document.html#Document

    document_pages = document.pages

    # Read the text recognition output from the processor
    print("The document contains the following paragraphs:")
    for page in document_pages:
        paragraphs = page.paragraphs
        for paragraph in paragraphs:
            paragraph_text = get_text(paragraph.layout, document)
            print(f"Paragraph text: {paragraph_text}")


# Extract shards from the text field
def get_text(doc_element: dict, document: dict):
    """
    Document AI identifies form fields by their offsets
    in document text. This function converts offsets
    to text snippets.
    """
    response = ""
    # If a text segment spans several lines, it will
    # be stored in different text segments.
    for segment in doc_element.text_anchor.text_segments:
        start_index = (
            int(segment.start_index)
            if segment in doc_element.text_anchor.text_segments
            else 0
        )
        end_index = int(segment.end_index)
        response += document.text[start_index:end_index]
    return response

def parse_invoice(project_id='poc-lab-280103',
         input_uri='gs://documentos-prueba-ocr/5.pdf'):

    client = documentai.DocumentUnderstandingServiceClient()

    gcs_source = documentai.types.GcsSource(uri=input_uri)
    print(type(gcs_source))
    # mime_type can be application/pdf, image/tiff,
    # and image/gif, or application/json
    input_config = documentai.types.InputConfig(
        gcs_source=gcs_source, mime_type='application/pdf')

    # Location can be 'us' or 'eu'
    parent = 'projects/{}/locations/us'.format(project_id)
    print(parent)
    request = documentai.types.ProcessDocumentRequest(
        parent=parent,
        input_config=input_config)

    document = client.process_document(request=request)

    # All text extracted from the document
    print('Document Text: {}'.format(document.text))

#parse_invoice()
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
region = 'us'
proccesor_id = '90484cfdedb024f6'
document = 'resources/invoice.pdf'
process_document_sample(project_id, region ,proccesor_id ,document)

