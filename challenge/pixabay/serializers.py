from rest_framework import serializers
import urllib.parse

class ImageSearchListSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=100, required=False)
    image_type = serializers.ChoiceField(choices=["all", "photo", "illustration", "vector"], default="photo")
    page = serializers.IntegerField(default=1, min_value=1)

    def validate(self, validated_data):
        if 'q' in validated_data:
            # q needs to be URL encoded
            validated_data['q'] = urllib.parse.quote_plus(validated_data['q'])
        return super().validate(validated_data)
