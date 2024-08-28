from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token
    
class MyTokenOtbainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #     token_data = response.data

    #     user = self.request.user

    #     token_data.update({
    #         'username': user.username,
    #         'email': user.email,
    #     })

    #     return Response(token_data)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)