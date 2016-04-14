
import webapp2
import jinja2
import os
from app.controller.CreditCardCtrl import CreditCardMsgCtrl

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HealthCheck(webapp2.RequestHandler):
    def get(self):
        self.response.write("Healthy")


application = webapp2.WSGIApplication([
    ('/', HealthCheck),
    ('/messages', CreditCardMsgCtrl)

    
], debug=True)

""",
('/messages', controllerhandle.MainHandler),
('/task2', TicTacToe),
('/task3', TicTacToe),
('/task4', TicTacToe)"""