from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import JSONCLP, JSONSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class JSONView(ModelViewSet):
    queryset = JSONCLP.objects.all() 
    serializer_class = JSONSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if "Valor Contagem" in data:
            data["Valor_Contagem"] = data.pop("Valor Contagem")
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
def myView(request):
    queryset = JSONCLP.objects.all() 
    context = {
        'objects': queryset, 
    }
    return render(request, 'template.html', context)