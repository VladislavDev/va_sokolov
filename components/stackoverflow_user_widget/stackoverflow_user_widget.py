from django_components import component

# timezone used to search for queries in the last 15 minutes
from django.utils import timezone

# ApiRegistrator used to find latest request and register new requests
from api_registrator.models import ApiRegistrator

# json used to load responses
import json


@component.register("stackoverflow_user_widget")
class stackoverflow_user_widget(component.Component):    
    
    """This widget allows you to display information about the stackoverflow profile on the site page. 
    The component receives information about the profile using a get request to stackexchange 2.3. Since
    the service has a quota of requests (300 requests per day), when trying to get information more often
    than once every 15 minutes, the information comes from the request registry.
    """
    
    # Template for widget rendering
    template_name = "stackoverflow_user_widget/stackoverflow_user_widget.html"

    def get_context_data(self, user_id, use_user_personal=False):
        
        """Data preparation function for rendering widget template. 
        Called as a widget in html templates. 
        
        Keyword arguments:
            user_id             <str | int>             id of stackoverflow user 
            use_user_personal   <bool, default False>   if True - use display_name & avatar from stackoverflow, 
                                                            else - use stackoverflow name & logo
        Returns:
            dict: {
                status              <str>   'error' or 'successful', result of request data,
                code                <int>   status_code of response,
                data                <dict>  stackoverflow profile info,
                use_user_personal   <bool>  use_user_personal from argument
                [logo]              <str>   url of component logo
            }
        """

        # Initially we initiate variables
        row     = None  # This is one user record
        result  = None  # This is result dict of data getting

        # request string with user_id argument
        request_ask = 'https://api.stackexchange.com/2.3/users/' + str(user_id) + '?site=stackoverflow'
        # Time mark of 15-minutes-period ago
        datetime_limit = timezone.now() - timezone.timedelta(minutes=15)

        # Search of last-15-minutes requests to stackexchange (limit 1, order request_date  DESC)
        latest_requests = ApiRegistrator.objects.filter(
            request_date__gt = datetime_limit,
            api_name = 'stackexchange'
        ).order_by('-request_date')[:1]

        # If requests to stackexchange have been made in the last 15 minutes
        if len(latest_requests) == 1:

            # Trying to find the last successful request to get information on the current user
            latest_request = ApiRegistrator.objects.filter(
                request_text = request_ask,
                api_name = 'stackexchange',
                response_status_code = 200
            ).order_by('-request_date')[:1]

            # If there was such a request, we will return its result
            if len(latest_request) == 1:
                row = latest_request[0]

            # If we have not received such information, we will return the error "many requests"
            else:
                result = {
                    'status'            : 'error',
                    'code'              : 429,
                    'data'              : None,
                    'use_user_personal' : None
                }
                return result
        
        # If there have been no requests to stackexchange in the last 15 minutes
        else:

            # We register a new get request to stackexchange and get its result
            row = ApiRegistrator.register(
                'get',
                'stackexchange',
                request_ask
            )

        # If the request is made successfully
        if row != -1 and row.response_status_code == 200:

            # we get the result of the found users
            user = json.loads(row.response_text)['items']
            
            # if one user is found, we will return information about him
            if len(user) == 1:
                result = {
                    'status'            : 'successful',
                    'code'              : 200,
                    'data'              : user[0],
                    'use_user_personal' : use_user_personal
                }
                
            # otherwise, we will return the error and the number of users found
            else:
                result = {
                    'status'            : 'error',
                    'code'              : 200,
                    'data'              : len(user),
                    'use_user_personal' : None
                }
                
        # If a request error occurred, we will return information about the error
        else: 
            result = {
                'status'            : 'error',
                'code'              : response.status_code,
                'data'              : None,
                'use_user_personal' : None
            }

        # We add the url of the stackoverflow logo to the final dict
        result['logo'] = "/components/stackoverflow_user_widget/media/so_icon.png"

        return {
            "so_profile": result,
        }

    # We list the css and js modules of the component in the class to load them
    class Media:
        css = "stackoverflow_user_widget/stackoverflow_user_widget.css"