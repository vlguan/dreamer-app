import boto3
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .form import DreamForm
from .utils import *
# from .serializer import *

def add_dream(request):
    if request.method == 'POST':
        form = DreamForm(request.POST)
        if form.is_valid():
            dream = form.save(commit=False)
            dream.user = request.user
            dream.save()
            nouns, verbs= dream_parser(request.POST)
            for noun in nouns:

            for verb in verbs:
                
            if request.interpret():
                
