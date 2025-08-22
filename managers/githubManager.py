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


   def userGetFollowing(self, user):
      """ GET /user/following/{username} """

      return get(url = self._url(f"/user/following/{user}"), headers = self._headers).json()


   def followUser(self, user):
      """ PUT /user/following/{username} """

      return put(url = self._url(f"/user/following/{user}"), headers = self._headers).json()


   def unfollowUser(self, user):
      """ DELETE /user/following/{username} """

      return delete(url = self._url(f"/user/following/{user}"), headers = self._headers).json()