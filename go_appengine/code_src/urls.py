import resources

URL_LIST = [ ('/', MainPage), ('/status', resources.PostNewTweet),
		('/status/(*)', resources.UserTweeting), ('/timeline', resources.Timeline),
		('/following', resources.Following), ('/followers', resources.Followers)]
