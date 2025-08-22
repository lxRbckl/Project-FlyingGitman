from requests import (get, put, delete)


class GithubManager:


   def __init__(self, token):
      """  """

      self._base = "https://api.github.com/"
      self._url = lambda endpoint : self._base + endpoint
      self._headers = {"Authorization" : f"token {token}"}


   def userGetDetails(self, user):
      """ GET /users/{username} """

      return get(url = self._url(f"/users/{user}"), headers = self._headers).json()


   def userGetFollowers(self, user, per = 100):
      """ GET all followers of a given user """

      page = 1
      followers = []
      while (response := get(
         
         headers = self._headers,
         url = self._url(f"/users/{user}/followers?per_page={per}&page={page}")
         
      ).json()):
         
         followers.extend([u["login"] for u in response])
         page += 1

      return followers
   

   def followUser(self, user):
      """ PUT /user/following/{username} """

      return put(url = self._url(f"/user/following/{user}"), headers = self._headers).json()


   def unfollowUser(self, user):
      """ DELETE /user/following/{username} """

      return delete(url = self._url(f"/user/following/{user}"), headers = self._headers).json()