from django_components import component

# timezone used to search for queries in the last 15 minutes
from django.utils import timezone

# ApiRegistrator used to find latest request and register new requests
from api_registrator.models import ApiRegistrator

# json used to load responses
import json


@component.register("github_user_widget")
class github_user_widget(component.Component):    
    
    template_name = "github_user_widget/github_user_widget.html"

    def get_context_data(self, user_login, use_user_personal=False):

        row     = None
        result  = None

        request_ask = 'https://api.github.com/users/' + str(user_login)
        datetime_limit = timezone.now() - timezone.timedelta(minutes=15)

        latest_requests = ApiRegistrator.objects.filter(
            request_date__gt = datetime_limit,
            request_text = request_ask
        ).order_by('-request_date')[:1]

        if len(latest_requests) == 1:

            latest_request = ApiRegistrator.objects.filter(
                request_text = request_ask,
                api_name = 'github',
                response_status_code = 200
            ).order_by('-request_date')[:1]

            if len(latest_request) == 1:
                row = latest_request[0]

            else:
                result = {
                    'status'            : 'error',
                    'code'              : 429,
                    'data'              : None,
                    'use_user_personal' : None
                }
                return result
        
        else:

            row = ApiRegistrator.register(
                'get',
                'github',
                request_ask
            )

        if row != -1 and row.response_status_code == 200:
            
            user = json.loads(row.response_text)
            
            if 'login' in user:
                result = {
                    'status'            : 'successful',
                    'code'              : 200,
                    'data'              : user,
                    'use_user_personal' : use_user_personal
                }
                
            else:
                result = {
                    'status'            : 'error',
                    'code'              : 200,
                    'data'              : 'unknown',
                    'use_user_personal' : None
                }
                
        else: 
            result = {
                'status'            : 'error',
                'code'              : response.status_code,
                'data'              : None,
                'use_user_personal' : None
            }

        result['logo'] = "/components/github_user_widget/media/gh_icon.png"

        return {
            "gh_profile": result,
        }

    class Media:
        css = "github_user_widget/github_user_widget.css"