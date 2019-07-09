from library import models
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class BookSerializer(DynamicFieldsModelSerializer):

    class Meta:
            model = models.Book
            fields = '__all__'
            read_only_fields = ('updated_by', 'created_by')





