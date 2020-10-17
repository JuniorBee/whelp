from celery.task import Task

from core.models import File, PDFContent
from core.utils import get_pdf_content


class ExtractPDFContent(Task):
    def run(self, file_id, *args, **kwargs):
        file_obj = File.objects.get(id=file_id)
        file_path = file_obj.file.path
        content = get_pdf_content(file_path)
        if PDFContent.objects.create(file=file_obj, content=content):
            return True
        return False
