from InstaFollower import InstaFollower

SIMILAR_ACCOUNT = "python.learning"
USERNAME = "astridtesting282"
PASSWORD = "vs+RJE5F/8w9GFq"

# 3. Outside the class InstaFollower, initialise the object and call the three methods in order:
follower_bot = InstaFollower()

follower_bot.login(USERNAME, PASSWORD)
follower_bot.find_followers(SIMILAR_ACCOUNT)
follower_bot.follow()
