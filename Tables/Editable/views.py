from django.shortcuts import render
from . import models

# Create your views here.


def index(request):

    return render(request, "index.html")


def table(request):

    data = {
        "data": [
            {
                "mirror_env": "",
                "micro_service": "",
                "ip_address": "",
                "root_passwd": "",
                "hispace_passwd": "",
                "ops": "",
                "dev": "",
                "version": "",
                "branch": "",
            }
        ]
    }
    
    return render(request, "editable_table.html")
