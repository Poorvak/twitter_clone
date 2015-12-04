import webapp2
import config
import urls
import resources

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Up and running')

app = webapp2.WSGIApplication(urls.URL_LIST, debug=config.DEBUG)