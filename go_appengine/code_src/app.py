import redis

redis_user = redis.Redis(config.REDIS_ENDPOINT, db=1)
redis_tweet = redis.Redis(config.REDIS_ENDPOINT, db=2)