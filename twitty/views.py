from urllib.parse import quote
from django.http import JsonResponse
from allauth.socialaccount.admin import SocialApp
from requests_oauthlib import OAuth1 
import requests

# Create your views here.
def tweet_search(request):
    search_term = "china"
    query = quote(search_term)
    #url = "https://api.twitter.com/1.1/search/tweets.json?q=%s"%(query)

    person = request.user
    # 7ag el user ena e9eer 3inda akthar min account with one user 
    social_account = person.socialaccount_set.get(user=person.id)
    social_token = social_account.socialtoken_set.get(account=social_account.id)
     #7ag tarteeb el API 
    token = social_token.token
    token_secret = social_token.token_secret

    social_app = SocialApp.objects.get(provider= social_account.provider)
    client_id =social_app.client_id
    client_secret = social_app.secret
    auth_value = OAuth1(client_id, client_secret, token, token_secret)
    resp = requests.get(url, auth=auth_value)

    return JsonResponse(resp.json(), safe=False)