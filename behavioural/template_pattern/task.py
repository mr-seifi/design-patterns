class Task:

    def execute(self):
        print('Logged!')


class MoneyTransfer(Task):

    def execute(self):
        super().execute()
        print('Money transfer!')


class GenerateReport(Task):
    
    def execute(self):
        super().execute()
        print('Generate report!')