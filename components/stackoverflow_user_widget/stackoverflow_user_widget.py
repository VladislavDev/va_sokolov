from django_components import component

from django.utils import timezone

from api_registrator.models import ApiRegistrator

import json


@component.register("stackoverflow_user_widget")
class stackoverflow_user_widget(component.Component):

    template_name = "stackoverflow_user_widget/stackoverflow_user_widget.html"

    def get_context_data(self, user_id, use_user_personal=False):

        row = None
        result = None

        request_ask = 'https://api.stackexchange.com/2.3/users/' + user_id + '?site=stackoverflow'
        datetime_limit = timezone.now() - timezone.timedelta(minutes=15)

        latest_requests = ApiRegistrator.objects.filter(
            request_date__gt = datetime_limit,
            api_name = 'stackexchange'
        ).order_by('-request_date')[:1]

        
        if len(latest_requests) == 1:

            latest_request = ApiRegistrator.objects.filter(
                request_text = request_ask,
                api_name = 'stackexchange',
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
                'stackexchange',
                request_ask
            )

        if row != -1 and row.response_status_code == 200:

            user = json.loads(row.response_text)['items']
            if len(user) == 1:
                result = {
                    'status'            : 'successful',
                    'code'              : 200,
                    'data'              : user[0],
                    'use_user_personal' : use_user_personal
                }
            else:
                result = {
                    'status'            : 'error',
                    'code'              : 200,
                    'data'              : len(user),
                    'use_user_personal' : None
                }
        else: 
            result = {
                'status'            : 'error',
                'code'              : response.status_code,
                'data'              : None,
                'use_user_personal' : None
            }

        result['logo'] = "/components/stackoverflow_user_widget/media/so_icon.png"

        return {
            "so_profile": result,
        }


    class Media:
        css = "stackoverflow_user_widget/stackoverflow_user_widget.css"