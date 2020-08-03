import os
import csv

filename = 'nano.csv'

lines = ( line for line in open(filename))
list_line = (s.rstrip().split(',') for s in lines)

cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)

funding = (
    int(company_dict['raisedAmt']) for company_dict in company_dicts if company_dict['round']=='a'
)

print(next(funding))
total_series_a = sum(funding)
print(total_series_a)