from django.db import models
from django.utils import timezone

import requests

class ApiRegistrator(models.Model):

    request_type = models.CharField(max_length=10)
    request_date = models.DateTimeField('DateTime')
    request_text = models.CharField(max_length=250)

    api_name = models.CharField(max_length=100, default="unknown")

    response_status_code = models.IntegerField(default=0)
    response_text = models.TextField()

    def __str__(self):
        return str(self.response_status_code) + ": " + self.request_text


    def register(req_type, api_base, text):

        response = None
        if req_type == 'get':
            response = requests.get(text)
        else:
            return -1

        return ApiRegistrator.objects.create(
            request_type = req_type,
            request_date = timezone.now(),
            request_text = text,
            api_name = api_base,
            response_status_code = response.status_code,
            response_text = response.text
        )
