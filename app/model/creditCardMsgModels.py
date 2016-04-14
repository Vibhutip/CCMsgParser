

class RegisterCreditCard:
    bankName = ""
    creditCardType = ""
    creditCardNumber = ""
    validityDate = ""
    bankid = ""
    datetime = ""
    type = "RegisterCreditCard"

    def __init__(self, *args):
        self.bankName = args[0]
        self.creditCardType = args[1]
        self.creditCardNumber = args[2]
        self.validityDate = args[3]
        self.bankid = args[4]
        self.datetime = args[5]
        self.type = "RegisterCreditCard"


class PaymentCreditCard:
    creditCardNumberLastFour = ""
    amount = ""
    spentDate = ""
    bankid = ""
    datetime = ""
    type = "PaymentCreditCard"

    def __init__(self, *args):
        self.creditCardNumberLastFour = args[0]
        self.amount = args[1]
        self.spentDate = args[2]
        self.bankid = args[3]
        self.datetime = args[4]
        self.type = "PaymentCreditCard"


class BillGenerator:
    bankName = ""
    creditCardNumberLastFour = ""
    billAmount = ""
    dueDate = ""
    billGenerationDate = ""
    bankid = ""
    datetime = ""
    type = "BillGenerator"

    def __init__(self, *args):
        self.bankName = args[0]
        self.creditCardNumberLastFour = args[1]
        self.billAmount = args[2]
        self.dueDate = args[3]
        self.billGenerationDate = args[4]
        self.bankid = args[5]
        self.datetime = args[6]
        self.type = "BillGenerator"


class DueDatePayment:
    creditCardNumberLastFour = ""
    billAmout = ""
    billingMonth = ""
    dueDate = ""
    paymentDate = ""
    latePaymentCharges = ""
    bankid = ""
    datetime = ""
    type = "DueDatePayment"

    def __init__(self, *args):
        self.creditCardNumberLastFour = args[0]
        self.billAmout = args[1]
        self.billingMonth = args[2]
        self.dueDate = args[3]
        self.paymentDate = args[4]
        self.latePaymentCharges = args[5]
        self.bankid = args[6]
        self.datetime = args[7]
        self.type = "DueDatePayment"
