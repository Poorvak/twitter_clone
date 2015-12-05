import controllers
import webapp2
import uuid
import return_file
import CustomException
import logger
import json
import time

current_time = lambda: int(round(time.time()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Up and running')

class RestHandler(webapp2.RequestHandler):
  def dispatch(self):
    super(RestHandler, self).dispatch()

  def SendJson(self, r):
    self.response.headers['content-type'] = 'text/plain'
    self.response.write(json.dumps(r))

class Register(RestHandler):
	def post(self):
		try:
			user_form = json.loads(self.request.body)
			register_user = controllers.register_user(username=user_form['username'], 
													password=user_form['password'],
													retype_password=user_form['retype_password'])
			return return_file.USER(user=register_user)
		except CustomException.PasswordMismatchException as e:
			abort(400, message=str(e))
		except CustomException.PasswordTooShortException as e:
			abort(400, message=str(e))	
		except CustomException.UserAlreadyExistsException as e:
		    abort(409, message=str(e))
		except CustomException.BadRequestException as e:
		    abort(400, message=str(e))
		except Exception as e:
		    logger.log(e)
		    abort(500, message=config.ERROR_MESSAGE)

class Login(RestHandler):
	def get(self):
		try:
			login_form = json.loads(self.request.body)
			controllers.login(username=login_form['username'],
							password=login_form['password'])
			return return_file.SUCCESS()
		except CustomException.InvalidTokenException as e:
		    abort(400, message=str(e))
		except CustomException.BadRequestException as e:
		    abort(400, message=str(e))
		except CustomException.UserNotFoundException as e:
		    abort(409, message=str(e))
		except Exception as e:
		    logger.log(e)
		    abort(500, message=config.ERROR_MESSAGE)

class PostNewTweet(RestHandler):
	# def get(self):
	# 	try:

	# 	except

	def post(self):
		try:
			post_form = json.loads(self.request.body)
			post_tweet = controllers.post_tweet(body=post_form['body'], timestamp=current_time())
		except Exception as e:
		    logger.log(e)
		    abort(500, message=config.ERROR_MESSAGE)
class UserTweeting(RestHandler):
	def get(self, user_id):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class Timeline(RestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class Following(RestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')

class Followers(RestHandler):
	def get(self):
	    self.response.headers['Content-Type'] = 'text/plain'
	    self.response.write('Up and running')
