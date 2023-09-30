from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Attempt to authenticate the user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Check if the user is an admin
        if user.is_superuser:
            # Generate or get the token for the admin user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            # Non-admin users will not receive a token
            return Response({'detail': 'Authentication failed for non-admin users.'}, status=403)
