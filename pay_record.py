from typing import List

import tax_calculator


class PayRecord:
    def __init__(self, _id: int, hours: List[float], rates: List[float]):
        self._id = id
        self._hours = hours
        self._rates = rates

    def get_id(self):
        return self._id

    def get_gross(self):
        sum_gross = 0
        for index, value in enumerate(self._hours):
            sum_gross = sum_gross + float(value) * float(self._rates[index])
        return sum_gross

    def get_tax(self):
        pass

    def get_net(self):
        pass

    def get_details(self):
        pass


class ResidentPayRecord(PayRecord):
    def __init__(self, _id: int, hours: List[float], rates: List[float]):
        self._id = id
        self._hours = hours
        self._rates = rates

    def get_tax(self):
        return tax_calculator.calc_res_tax(self.get_gross())


class WorkingHolidayPayRecord(PayRecord):
    def __init__(self, id, hours, rates, visa, year_to_date):
        self._id = id
        self._hours = hours
        self._rates = rates
        self._visa = visa
        self._year_to_date = year_to_date

    def get_tax(self):
        return tax_calculator.cal_wh_tax(self.get_gross(), self._year_to_date)

    def get_details(self):
        pass
