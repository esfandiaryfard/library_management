from builtins import Exception
from django.utils.translation import gettext as _
from rest_framework import status, viewsets
from rest_framework.response import Response
from library import serializers, models

"""
Create Crud for Book entity
"""


class BookViewset(viewsets.ViewSet):

    def index(self, request):
        try:
            books = models.Book.get_books()
            if not books.exists():
                return Response({"messages": _("No data to show")}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.BookSerializer(books, many=True)
            return Response({"messages": _("DataLoaded"), "data": serializer.data})
        except Exception as e:
            return Response({"message": _("status500")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
