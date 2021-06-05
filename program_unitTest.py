import unittest
import csv_importer


class ProgramUnitTest(unittest.TestCase):
    def test_something(self):
        a_list_of_pay_records = csv_importer.import_pay_records("import/employee-payroll-data.csv")

        for payRecord in a_list_of_pay_records:
            print(str(payRecord.get_gross()) + " " + str(payRecord.get_tax()) + " " + str(
                payRecord.get_gross() - payRecord.get_tax()))


if __name__ == '__main__':
    unittest.main()




