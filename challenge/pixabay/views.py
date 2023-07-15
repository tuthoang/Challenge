from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import ImageSearchListSerializer
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
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({'images': images, 'page': page, 'visible_pages': visible_pages}, 
                        template_name='templates/ImageSearchListTemplate.html')
