from builtins import Exception
from django.utils.translation import gettext as _
from rest_framework import status, viewsets
from rest_framework.response import Response
from library import serializers, models
from django.utils import timezone
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

    def store(self, request):
        try:
            serializer = serializers.BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user)
                return Response({"message": _("Added Successfully")}, status=status.HTTP_201_CREATED)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": _("status500")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        try:
            book = models.Book.get_book(pk)
            serializer = serializers.BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save(updated_by=request.user, updated_at=timezone.now())
                return Response({"message": _("Added Successfully")}, status=status.HTTP_205_RESET_CONTENT)
            return Response({'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except models.Book.DoesNotExist:
            return Response({"message": _("No data to show")}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except models.Book.MultipleObjectsReturned:
            return Response({"message": _("you can add just one pk")}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response({"message": _("status500")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk, format=None):
        try:
            book = models.Book.get_book(pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": _("status500")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)