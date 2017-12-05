from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

def member_list(request):
	mannaie = request.user
	# 7ag el user ena e9eer 3inda akthar min account with one user 
	social_account = mannaie.socialaccount_set.get(user=mannaie.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)
	token = social_token.token

# to call all members of that organization
	#url = "https://api.github.com/orgs/joincoded/members"
# to call List user repositories 
	url = "https://api.github.com/users/mana3ii/repos"	
	res =requests.get(url, headers={"Authorization": "token "+token})
	# headers to pass the autharisation key it takes the value of the key
	return JsonResponse(res.json(), safe=False)