using System;

using SocialOctopus.Managers;
using SocialOctopus.Interfaces;


namespace SocialOctopus
{

   class SocialOctopus {

      static void Main(string[] args)
      {

         IOctokit octokitHandler = new OctokitManager();
         IDatabase databaseHandler = new DatabaseManager();
         

      }

   }

}  