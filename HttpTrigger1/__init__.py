import logging
import uuid
import azure.functions as func


def main(req: func.HttpRequest, inputDocument: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('HTTP trigger function processed a request to track visit count.')

    # Check if the inputDocument has any existing document
    if inputDocument:
        # Retrieve the current visit count
        current_document = inputDocument[0]
        visit_count = current_document.get('visit_count', 0)

        # Increment the visit count
        new_visit_count = visit_count + 1
        current_document['visit_count'] = new_visit_count

        # Update the document in Cosmos DB
        outputDocument.set(current_document)

        # Return the updated visit count
        return func.HttpResponse(f"Updated visit count: {new_visit_count}", status_code=200)

    else:
        # If no document exists, create a new one with a visit count of 1
        new_document = {
            "id": "visit_counter",  # A unique id for the document
            "visit_count": 1
        }

        # Write the new document to Cosmos DB
        outputDocument.set(func.Document.from_dict(new_document))

        # Return the initial visit count
        return func.HttpResponse(f"First visit recorded. Visit count: 1", status_code=201)