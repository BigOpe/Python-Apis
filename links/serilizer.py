from rest_framework import serializers
from .models import links
class Linkserializers(serializers.Modelserializers):
    class Meta:
       model = Link
       fields = "__all__"
