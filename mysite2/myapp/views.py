from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
import json
from . import serializers
#from snippets.serializers import SnippetSerializer


class HelloAPIView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self , request , format =None):
        """Test GET"""

        an_api_view = [
            'Use HTTP method as function (get, post, patch, put, delete)'
        ]
        return Response({'my Django': 'Hello!', 'api_view' : an_api_view})

    def post(self, request):
        """Test POST"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Test PUT"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Test PATCH"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Test DELETE"""
        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self, request):
        """Retrun a hello message list."""
        a_viewset = [
            'Uses action (list, create retrieve, update, partial_update)',
            'Automatically maps to URLs using Routes',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!' , 'a_viewset': a_viewset})





#@api_view(['GET'])
#@renderer_classes([StaticHTMLRenderer])
def homepage_view(request):
    #data = '<html><body><h1>Hello, simple_html_view</h1></body></html>'
    x = '{ "name":"John", "age":30, "city":"New York"}'
    aaa={}
    aaa['bbb']="mordy"
    #data= json.dumps(x)
    data= json.loads(x)
    #return Response({'accepted media type': request.accepted_renderer.media_type})

    #serializer = SnippetSerializer(aaa, many=True)
    #return Response(serializer.data)

def homepage_view1(request):
    mylist = [1, 2, 3]
    return HttpResponse('Django says: Hello mordy! %s'% mylist)