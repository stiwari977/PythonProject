from typing import List

import pay_record



def import_pay_records(file: str) -> str:
    payRecords = []

    with open(file, "r") as data:
        # Skip the first line
        data.readline()

        # Read subsequent lines
        lines = data.readlines()

        hours_dict = {}
        rates_dict = {}
        visa_dict = {}
        year_to_date_dict = {}

        for line in lines:
            fields = line.split(",")
            id = fields[0]
            hours = fields[1]
            rates = fields[2]
            visa = fields[3]
            year_to_date = fields[4]

            if id in hours_dict.keys():
                hours_dict[id].append(hours)
            else:
                hours_dict[id] = [hours]

            if id in rates_dict.keys():
                rates_dict[id].append(rates)
            else:
                rates_dict[id] = [rates]

            if id in visa_dict.keys():
                visa_dict[id].append(visa)
            else:
                visa_dict[id] = [visa]

            if id in year_to_date_dict.keys():
                year_to_date_dict[id].append(year_to_date)
            else:
                year_to_date_dict[id] = [year_to_date]

        for id in hours_dict.keys():
            payRecord = _create_pay_record(id, hours_dict[id], rates_dict[id], visa_dict[id], year_to_date_dict[id])
            payRecords.append(payRecord)

    return payRecords


def _create_pay_record(id: int, hours: List[float], rates: List[float], visa: str, year_to_date: str):
    if visa[0] == '':
        return pay_record.ResidentPayRecord(id, hours, rates)
    else:
        return pay_record.WorkingHolidayPayRecord(id, hours, rates, visa[0], year_to_date[0])
