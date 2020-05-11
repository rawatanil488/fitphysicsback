from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action

from .models import Blog
from .serializers import BlogSerializer

class BlogDetails(generics.GenericAPIView):
    """
    A Generic API View that returns Blog by list
    """
    serializer_class = BlogSerializer
    def get_queryset(self):
        try:
            blog_obj = Blog.objects.filter()
        except Blog.DoesNotExist:
            blog_obj = None
        if not blog_obj:
            return {'Error': 'Blogs Do Not Exist'}
        else:
            serializer = BlogSerializer(blog_obj, many=True)
            return serializer.data

    def get(self, request, pk=None):
        return Response(self.get_queryset())


class CreateNewBlog(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A Generic API View that creates Blog
    """
    parser_class = (FileUploadParser,)
    serializer_class = BlogSerializer

    @action(detail=True, methods=['post'])
    def upload_file_blog(self, request, *args, **kwargs):
        file_serializer = BlogSerializer(data=request.data, instance=request.user)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.status, status = status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
