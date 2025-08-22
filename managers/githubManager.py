from requests import (get, put, delete)


class GithubManager:


   def __init__(self, token):
      """  """

      self._base = "https://api.github.com/"
      self._url = lambda endpoint : self._base + endpoint
      self._headers = {"Authorization" : f"token {token}"}


   def userGetDetails(user):
      """ GET /users/{username} """

      pass


   def userGetFollowing(user):
      """ GET /user/following/{username} """

      pass


   def followUser(user):
      """ PUT /user/following/{username} """

      pass


   def unfollowUser(user):
      """ DELETE /user/following/{username} """

      pass