from CreditCardDAO import CreditCardDAO

class BillGeneratorDao(CreditCardDAO):

    """docstring for BillGeneratorDao"""

    def __init__(self):
        self.init()

    def post(self, card):
    	
        self.cursor.execute("INSERT into BillGenerator(bankName, creditCardNumberLastFour, billAmount, dueDate, billGenerationDate, bankid, datetime) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (card.bankName,
                            card.creditCardNumberLastFour,
                            card.billAmount,
                            card.dueDate,
                            card.billGenerationDate,
                            card.bankid,
                            card.datetime))
        self.commit()
    # Task2
    def getBiilingCycle(self):
        self.cursor.execute("SELECT * FROM BillGenerator")
        data = []
        for row in self.cursor.fetchall();
            data.append(row)
        self.close()
        return data

    def getPaymentMonthlyAverage(self):
        self.cursor.execute("SELECT bankid,billAmount,dueDate from BillGenerator")
        data = []
        for row in self.cursor.fetchall();
            data.append(row)
        self.close()
        return data