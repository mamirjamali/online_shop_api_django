# from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.core.cache import cache
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
from django.shortcuts import render
import requests
from rest_framework.views import APIView
# from .tasks import notify_customers
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(selt, request):
        try:
            logger.info('Calling httpin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except request.ConnectionErroe:
            logger.critical('httpbin is offline')

        return render(request, 'hello.html', {'name': data})
