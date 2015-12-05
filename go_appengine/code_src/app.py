import redis

redis_user = redis.StrictRedis.from_url(config.REDIS_ENDPOINT, db=1)
redis_post = redis.StrictRedis.from_url(config.REDIS_ENDPOINT, db=2)
redis_timeline = redis.StrictRedis.from_url(config.REDIS_ENDPOINT, db=3)