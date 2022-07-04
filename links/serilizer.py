from rest_framework import serilizers
from .models import links
class Linkserilizers(serializers.Modelserializers):
    class Meta:
       model = Link
       fields = "__all__"
