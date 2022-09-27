from task import MoneyTransfer, GenerateReport


def main():

    task_1 = MoneyTransfer()
    task_1.execute()

    task_2 = GenerateReport()
    task_2.execute()



if __name__ == '__main__':
    main()