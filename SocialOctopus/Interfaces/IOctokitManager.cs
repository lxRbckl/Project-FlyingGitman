namespace SocialOctopus.Interfaces
{
    public interface IOctokitManager
    {

      // methods <
        void followUser(string user);

        void unfollowUser(string user);

        string[] getFollowers(string user);

        string[] getFollowing(string user);

        // >

    }
}
