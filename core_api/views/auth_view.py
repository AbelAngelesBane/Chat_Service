from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import AuthTokenError

from rest_framework.views import APIView
from rest_framework.response import Response
from ..constants import *
from ..general_functions import *
from ..models.consumer_model import *
from ..serializers.auth_serializer import *

from ..constants import *
import smtplib, ssl
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                str(user.is_active) + str(user.pk) + str(timestamp)
        )

email_verification_token = EmailVerificationTokenGenerator()


class apiRegisterAccount(APIView):
    def post(self,request):

        errors = {}
        request_data = request.data.copy()

        if request.content_type != 'application/x-www-form-urlencoded':
            # fix the return message later
            return Response(data={'status': wrong_input, 'message':wrong_header_key_msg, 'errors':{'Content-Type': ["Unacceptable value"]}})
        
        required_fields = ['email','username','password']

        for field in required_fields:
            if field not in request_data:
                return Response(data={'status':wrong_input, 'message':wrong_body_vals_msg, 'errors':wrong_body_vals_msg})
            else:
                if request_data[field] == '':
                    errors[field] = null_field_error

        if validate_emailAdd(request_data['email']) != True:  
            errors['email'] = 'Invalid email format'
            return Response(data={'status':wrong_input, 'message':wrong_body_vals_msg, 'errors':errors})
         
        if User.objects.filter(email=request_data['email']).count() != 0:
            errors['email'] = 'Email already exist'

        if len(errors) != 0: 
            return Response(data={'status':wrong_input, 'message':wrong_body_vals_msg, 'errors':errors})
        

        #check if req fields are present
        #check if fields are not null
        #check if email is valid
        #Check if email is taken
        #check if register_as works
        #check serializer


        serializer = ConsumerRegisterProfileSerializer(data=request_data)
        if serializer.is_valid():
            message = "A verification email has been sent to: " + serializer.data['email'] 
            user, _ = User.objects.get_or_create(
                username = serializer.data['username'],
                email = serializer.data['email'],
                is_active = False,
                password = make_password(serializer.data['password']),               
            )
            domain = '127.0.0.1:8000'

            
            email_body = 'Open the link to verify your account: \t' + ""


        #      path('activate/<uidb64>/<token>', 
        #  ActivateView.as_view(), 
        #  name='activate'),

            # "http://{{ domain }}{% url 'activate' uidb64=uid token=token %}"

            email = EmailMessage(
                subject = 'Chat Verification Code',
                body = email_body,
                from_email = 'mydjangoapp22@gmail.com',
                to = ['abelebane10@gmail.com'],
                bcc = ['abelbane@yahoo.com'],
            )

            email.send()


            ConsumerModel.objects.create(     
                    uid = generate_uuid(),
                    name = user.username,
                )
            return Response(data={"status": ok, 'message': message}, status=ok) 
        return Response(data={'status':wrong_input, 'message':wrong_body_vals_msg, 'errors':serializer.errors})      
     
        
                       





