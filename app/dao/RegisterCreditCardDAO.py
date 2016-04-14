from CreditCardDAO import CreditCardDAO

class RegisterCreditCardDAO(CreditCardDAO):

    """docstring for RegisterCreditCardDAO"""

    def __init__(self):
        self.init()

    def post(self, card):        
        self.cursor.execute("INSERT into RegisterCreditCard(bankName, creditCardType, creditCardNumber, validityDate, bankid, datetime) VALUES (%s,%s,%s,%s,%s,%s)",
                            (card.bankName,
                            card.creditCardType,
                            card.creditCardNumber,
                            card.validityDate,
                            card.bankid,
                            card.datetime))
        
        self.commit()
