from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import CustomUser
from .serializers import SearchUserSerializer


class SearchUser(APIView):

    def post(self, request, format=None):
        searched_user = CustomUser.objects.filter(
            username__icontains=request.data["searched_user"]
        )[:10]

        serializer = SearchUserSerializer(searched_user, many=True)

        return Response(serializer.data)
