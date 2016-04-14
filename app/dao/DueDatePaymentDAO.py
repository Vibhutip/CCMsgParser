from CreditCardDAO import CreditCardDAO

class DueDatePaymentDAO(CreditCardDAO):

    """docstring for DueDatePaymentDAO"""

    def __init__(self):
        self.init()

    def post(self, card):
        self.cursor.execute("INSERT into DueDatePayment(creditCardNumberLastFour, billAmout, billingMonth, dueDate, paymentDate, latePaymentCharges, bankid, datetime) VALUES (%s,%s,%s,%s,%s,%s, %s,%s)",
                            (card.creditCardNumberLastFour,
                            card.billAmout,
                            card.billingMonth,
                            card.dueDate,
                            card.paymentDate,
                            card.latePaymentCharges,
                            card.bankid,
                            card.datetime))
        self.commit()
    #Task3
    def getDelayAndPenalty(self):
        self.cursor.execute("SELECT bankid, latePaymentCharges, paymentDate, dueDate, billingMonth from DueDatePayment");
        data = []
        for row in self.cursor.fetchall();
            data.append(row)
        self.close()
        return data
