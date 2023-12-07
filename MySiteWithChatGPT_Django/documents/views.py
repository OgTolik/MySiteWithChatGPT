from django.shortcuts import render
from MySiteWithChatGPT_Django.documents.models import Document


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})
