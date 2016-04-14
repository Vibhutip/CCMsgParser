from CreditCardDAO import CreditCardDAO

class PaymentCardDAO(CreditCardDAO):

    """docstring for PaymentCardDAO"""

    def __init__(self):
        self.init()

    def post(self, card):
        self.cursor.execute("INSERT into PaymentCard(creditCardNumberLastFour, amount, spentDate, bankid, datetime) VALUES (%s,%s,%s,%s,%s)",
                            (card.creditCardNumberLastFour,
                            card.amount,
                            card.spentDate,
                            card.bankid,
                            card.datetime))
        self.commit()
