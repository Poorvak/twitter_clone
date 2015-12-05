import config
import urls
import resources
import webapp2

app = webapp2.WSGIApplication(urls.URL_LIST, debug=config.DEBUG)