import controllers
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Up and running')

class PostNewTweet(webapp2.RequestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class UserTweeting(webapp2.RequestHandler):
	def get(self, user_id):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class Timeline(webapp2.RequestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class Following(webapp2.RequestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class Followers(webapp2.RequestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')
