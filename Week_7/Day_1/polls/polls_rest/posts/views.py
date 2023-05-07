from django.shortcuts import render
from .models import Post
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST , HTTP_202_ACCEPTED)

# Create your views here.



class PostView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                queryset = Post.objects.get(id = pk)
                serializer = PostSerializer(queryset)
            except Post.DoesNotExist:
                return Response({'details': 'post not found'}, status=HTTP_400_BAD_REQUEST)
        else:
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset,many=True)
        
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = HTTP_200_OK)
        return Response(serializer.errors , status = HTTP_400_BAD_REQUEST)
    def delete(self ,request, pk , *args,**kwargs):
        try:
            post = Post.objects.get(id = pk)
            post.delete()
            return Restponse({'details': 'post deleted'}, status =HTTP_202_ACCEPTED)
        except:
            return Response({'details': 'post not found'}, status=HTTP_400_BAD_REQUEST)
    def put(self ,request, *args,**kwargs):
        pk = kwargs.get('pk')

        if pk:
            try:
                post = Post.objects.get(id=pk)
                serializer = PostSerializer(post , data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data , status=HTTP_202_ACCEPTED)
            except Post.DoesNotExist:
                return Response({"detail":"Post Not Found"} , status=HTTP_400_BAD_REQUEST)

        else:
            return Response({"detail":"PK Not Found"} , status=HTTP_400_BAD_REQUEST)