from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


# Create your views here.


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request):
        """Return  a list of API feature"""

        an_apiview = [
            'uses a HTTP method as function(get, post, patch, delete)',
            'it is similar to tradition django view',
            'gives you most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})