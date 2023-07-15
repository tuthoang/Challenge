from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import ImageDetail
from .serializers import ImageSearchListSerializer, ImageDetailSerializer
import challenge.pixabay.client as client

class ImageSearchListView(generics.GenericAPIView):
    serializer_class = ImageSearchListSerializer
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):

        params = request.GET
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=True)
        images = client.get(serializer.validated_data)
        page = serializer.validated_data.get('page', 1)
        min_visible_page = max(1, page-5)
        max_visible_page = page+5
        visible_pages = list(range(min_visible_page, max_visible_page))
        if not images:
            raise Http404

        image_serializers = [ImageDetailSerializer(data=image) for image in images]
        validated_image_details = [serializer.validated_data for serializer in image_serializers if serializer.is_valid()]
        image_details = [ImageDetail(**details) for details in validated_image_details]
        ImageDetail.objects.bulk_create(
            image_details,
            update_conflicts=True,
            unique_fields=['id'],
            update_fields=['views', 'downloads', 'likes', 'comments', 'tags', 'previewURL'],
        )

        return Response({'images': images, 'page': page, 'visible_pages': visible_pages}, 
                        template_name='templates/ImageSearchListTemplate.html')

class ImageDetailView(generics.RetrieveAPIView):
    queryset = ImageDetail
    serializer_class = ImageDetailSerializer
    permission_classes = []
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, pk):
        image_detail = self.get_object()
        serializer = self.get_serializer(image_detail)
        return Response({'image': serializer.data}, template_name='templates/ImageDetailTemplate.html')
