# Whelp Homework
The code in this repo:
 - creates a simple API interface that is protected with JWT authorization. 
 - We can upload a PDF file to the /api/v1/create endpoint and when we do, the view sends this file to the Celery in the backend and returns the record id that is linked to the authorized user id and start processing asynchronously. 
 - Celery worker extracts the PDF content and saves it to the DB. 
 - From the /api/v1/check/:id endpoint you can track the status: if processing has been finalized then returns the content that was extracted from the document. 
 
 For deployment purposes docker-compose used.
