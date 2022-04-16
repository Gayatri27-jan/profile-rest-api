from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from . import permissions


# Create your views here.


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return  a list of API feature"""

        an_apiview = [
            'uses a HTTP method as function(get, post, patch, delete)',
            'it is similar to tradition django view',
            'gives you most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our  name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """ patch request, only update a fields provided by request"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """ Delete and object"""
        return Response({"method": "delete"})


class HelloViewSet(viewsets.ViewSet):
    """ Test HelloViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ :return hello message"""

        a_viewset = [
            {
                "uses a action (list, create,retrieve update, partial_update,distroye)",
                "Automatically maps to URLs using routers"
                "Provides a more functionality with less code"}]

        return Response({"message": "Hello", "a_viewSet": a_viewset})

    def create(self, request):
        """Create hello message with our  name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles updating an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """ Handling  update an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """ Delete and object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """ Delete and object"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating, Creating and updating profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email",)


class LoginViewSet(viewsets.ViewSet):
    """check email and password and return auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use obtainToken APIView to validate and create a token"""
        return ObtainAuthToken().as_view()(request=request._request)
