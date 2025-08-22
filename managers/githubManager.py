from functools import wraps
from requests import (get, put, delete, RequestException)


def errorHandler(func):
    
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        
        try: return func(self, *args, **kwargs)
        except Exception as e:
            
            print(f"{func.__name__}: {e}")
            return False
        
    return wrapper


class GithubManager:


   def __init__(self, token):
      """  """

      self._base = "https://api.github.com/"
      self._url = lambda endpoint : self._base + endpoint
      self._headers = {"Authorization" : f"token {token}"}


   @errorHandler
   def _userGetDetails(self, user):
      """ GET /users/{username} """

      return get(url = self._url(f"/users/{user}"), headers = self._headers).json()


   @errorHandler
   def _userGetFollowers(self, user):
      """ GET all followers of a given user """

      page = 1
      followers = []
      while (response := get(
         
         headers = self._headers,
         url = self._url(f"/users/{user}/followers?per_page=100&page={page}")
         
      ).json()):
         
         followers.extend([u["login"] for u in response])
         page += 1

      return followers
   

   @errorHandler
   def _followUser(self, user):
      """ PUT /user/following/{username} """

      return put(url = self._url(f"/user/following/{user}"), headers = self._headers)


   @errorHandler
   def _unfollowUser(self, user):
      """ DELETE /user/following/{username} """

      return delete(url = self._url(f"/user/following/{user}"), headers = self._headers)