#!/usr/bin/env python

import webapp2
import urllib2
import json
import jinja2
import os

from google.appengine.api import mail
from google.appengine.api import users

from  app.utils.parser import parse
from app.dao.RegisterCreditCardDAO import RegisterCreditCardDAO
from app.dao.PaymentCreditCardDAO import PaymentCreditCardDAO
from app.dao.BillGeneratorDAO import BillGeneratorDAO
from app.dao.DueDatePaymentDAO import DueDatePaymentDAO


class CreditCardMsgCtrl(webapp2.RequestHandler):

    def post(self):
        
        messageArray = json.loads(self.request.body)
        
        
        for itm in messageArray["messageJson"]:
            if "CREDIT" in str(itm['number']):
                card = parse(
                    itm['text'], itm['number'], itm['datetime'])
                if card.type == "RegisterCreditCard":
                    RegisterCreditCardDAO().post(card)
                if card.type == "PaymentCreditCard":
                    PaymentCreditCardDAO().post(card)
                if card.type == "BillGenerator":
                    BillGeneratorDAO().post(card)
                if card.type == "DueDatePayment":
                    DueDatePaymentDAO().post(card)
        
        self.response.write("Done")
