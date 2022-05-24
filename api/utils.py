from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer.data