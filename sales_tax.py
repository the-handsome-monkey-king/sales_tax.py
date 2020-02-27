#!/usr/bin/env python
"""sales_tax.py

A sales tax calculator for Canadian sales tax by province.
Sales tax as of July 2019."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

gst = 0.05
province_tax = {
    1: {'name': 'Alberta',
        'rate': 0.00},
    2: {'name': 'British Columbia',
        'rate': 0.07},
    3: {'name': 'Manitoba',
        'rate': 0.08},
    4: {'name': 'New Brunswick',
        'rate': 0.10}, 
    5: {'name': 'Newfoundland and Labrador',
        'rate': 0.10},
    6: {'name': 'Northwest Territories',
        'rate': 0.00},
    7: {'name': 'Nova Scotia',
        'rate': 0.10},
    8: {'name':'Nunavit',
        'rate': 0.00},
    9: {'name':'Ontario',
        'rate': 0.08},
    10: {'name':'Prince Edward Island',
        'rate': 0.10},
    11: {'name':'Quebec',
        'rate': 0.09975},
    12: {'name':'Saskatchewan',
        'rate': 0.06},
    13: {'name':'Yukon',
        'rate': 0.00}
    }

def get_float(msg):
    while(True):
        try:
            arg = (float)(raw_input(msg))
            if arg < 0:
                raise ValueError
            return arg
        except(ValueError):
            print("Input is invalid. Please try again")

def get_menu():
    while(True):
        try:
            print("Select a province by number:")
            for key, province in province_tax.items():
                print("{}: {}".format(key, province['name']))
            selection = (int)(raw_input("#: "))
            return selection
        except(ValueError):
            print("Selection number was invalid. Please try again.")


def main():
    cost = get_float("Please enter the cost: ")
    selection = get_menu()
    gst_cost = round(cost * gst, 2)
    pst_cost = round(cost * province_tax[selection]['rate'], 2)
    total_tax = round(gst_cost + pst_cost, 2)
    total_cost = cost + total_tax
    print("Province: {}".format(province_tax[selection]['name']))
    print("Cost: {}".format(cost))
    print("GST: {}".format(gst_cost))
    print("Provincial Tax: {}".format(pst_cost))
    print("Total Cost: {}".format(total_cost))

if __name__ == "__main__":
    main()
