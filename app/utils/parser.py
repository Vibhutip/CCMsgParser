#!/usr/bin python
import json
import re
from app.model.creditCardMsgModels import *


def parse(message, bank, datetime):

	if 'successfully activated' in message:
		a=re.findall(r'Your (.*?)- (.*?) number (.*?) has been successfully activated. Your card is valid upto (.*)',message)
		return RegisterCreditCard(a[0][0], a[0][1], a[0][2], a[0][3], bank, datetime)

	if 'Thank you' in message:
		a=re.findall(r'Thank you for using your credit card ending with(.*?)for payment of INR(.*?)on(.*)',message)
		return PaymentCreditCard(a[0][0], a[0][1], a[0][2], bank, datetime)

	if 'bill amount' in message:
		a=re.findall(r'Your (.*?) card number ending in (.*?) has a bill amount of INR (.*?) for month (.*?) ,your due date is (.*)',message)
		return BillGenerator(a[0][0], a[0][1], a[0][2], a[0][3], a[0][4], bank, datetime)

	if 'We confirm' in message:
		a=re.findall(r'We confirm your bill payment for card number ending with(.*?)of Rs.(.*?)for (.*?). Your due date was (.*?) . Your payment has been made on(.*?). Late payment charges Rs. (.*).',message)
		return DueDatePayment(a[0][0], a[0][1], a[0][2], a[0][3], a[0][4], a[0][5], bank, datetime)

