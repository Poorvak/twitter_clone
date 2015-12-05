import resources
import re

URL_LIST = [ ('/', resources.MainPage), ('/status', resources.PostNewTweet),
		('/status/(.*)', resources.UserTweeting), ('/timeline', resources.Timeline),
		('/following', resources.Following), ('/followers', resources.Followers),
		('/register', resources.Register), ('/login', resources.Login)]
