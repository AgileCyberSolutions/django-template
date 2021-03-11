from django.shortcuts import render
from http import HTTPStatus

from django.views.decorators.csrf import csrf_exempt
from ..models.serializers.userSerializer import UserRegisterSerializer
from ..models.user import User
import io
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
import rest_framework.status as  HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.models import Group

import json 
from django.core import serializers

from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema

class OauthRegister(APIView):
    permission_classes = (AllowAny,)
    #AllowAny,  IsAuthenticated,

    renderer_classes = [JSONRenderer]

    @csrf_exempt
    @swagger_auto_schema(operation_description="Register User",responses={404: 'unauthorized',200:'success'},
    request_body=openapi.Schema(type=openapi.TYPE_OBJECT, 
    properties={
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='enter firstname'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='enter lastname'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='enter email'),
        'phone_no': openapi.Schema(type=openapi.TYPE_STRING, description='enter phone no'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING, description='enter gender (m/f)'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='enter password'),
    }))
    def post(self, request, format=None):
        if request.method == "POST":
            data = json.loads(request.body)
            streamData = io.BytesIO(request.body)
            parsedData = JSONParser().parse(streamData)
            oldserializer = UserRegisterSerializer(data=parsedData) 
            if oldserializer.is_valid():
                newuser = oldserializer.save()
                newuser.set_password(parsedData["password"])
                newuser.save()
                group = Group.objects.get(name='user_permission')
                newuser.groups.add(group)
                status_code = HTTPStatus.OK
                response = response({'success': 'true',"message":"user created"},status=status_code)
                return response
            else:
                status_code = HTTPStatus.OK
                response = response({'success': 'false',"message":"user not created"},status=status_code)
                return response
        else:
            status_code = HTTPStatus.METHOD_NOT_ALLOWED
            response = response({'success': 'false'},status=status_code)
            return response
