class Employee:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_job(self):
        return self.job

    def get_pay(self):
        return self.pay

    def greetings(self):
        print("hello, I am {}.".format(self.name))

