# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from nxtbn.users.api.v1.serializers import CustomTokenObtainPairSerializer, SignupSerializer
from allauth.account import app_settings as allauth_settings
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions  import AllowAny
from allauth.account.utils import complete_signup



from rest_framework_simplejwt.views import TokenObtainPairView


class SignupView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(request=self.request)
        token = RefreshToken.for_user(user)

        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)
    
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            response_data =  {"detail": _("Verification e-mail sent.")}
        else:
            response_data = {
                'user': serializer.data,
                'token': {
                    'refresh': str(token),
                    'access': str(token.access_token),
                }
            }

        return Response(response_data, status=status.HTTP_201_CREATED)





class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer