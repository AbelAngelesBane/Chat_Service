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

# from ..serializers.auth_serializer import *

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
                return Response(data={'status':wrong_input, 'message':wrong_body_vals_msg, 'errors':inc_body_parameter_msg})
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
            message = "Registration Successful"
            user, _ = User.objects.get_or_create(
                username = serializer.data['username'],
                email = serializer.data['email'],
                password = make_password(serializer.data['password'])
            )

            ConsumerModel.objects.create(     
                    uid = generate_uuid(),
                    name = user.username,
                )
            return Response(data={"status": ok, 'message': message}, status=ok) 
        return Response(data={'status':wrong_input, 'message':wrong_body_vals_msg, 'errors':serializer.errors})      
     
        
                       





