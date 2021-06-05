def calc_res_tax(gross: float):
    tax = 0
    if 72.0 >= gross > -1.0:
        tax = 0.19 * gross - 0.19
    elif 361.0 >= gross > 72.0:
        tax = 0.2342 * gross - 32.13
    elif 932.0 >= gross > 361.0:
        tax = 0.3477 * gross - 44.2476
    elif 1380.0 >= gross > 932.0:
        tax = 0.345 * gross - 41.7311
    elif 3111.0 >= gross > 1380.0:
        tax = 0.39 * gross - 103.8657
    elif 999999.0 >= gross > 3111.0:
        tax = 0.47 * gross - 352.7888

    return tax


def cal_wh_tax(gross: float, year_to_date: float):
    tax = 0

    year_to_date_plus_gross = 0
    try:
        year_to_date_plus_gross = float(year_to_date) + float(gross)
    except:
        pass

    if 37000.0 >= year_to_date_plus_gross > -1.0:
        tax = 0.15 * gross
    elif 90000.0 >= year_to_date_plus_gross > 37000.0:
        tax = 0.32 * gross
    elif 180000.0 >= year_to_date_plus_gross > 90000.0:
        tax = 0.37 * gross
    elif 9999999.0 >= year_to_date_plus_gross > 180000.0:
        tax = 0.45 * gross

    return tax
