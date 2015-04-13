#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""


def sum_orders(customers,orders):
    """custmers and orders.

    Args:
        customers (dictionary): customers
        orders (dictionary): orders

    Returns:
        dictionary: combind dictionary

    Examples:
    >>> taskd.sum_orders(CUSTOMERS,ORDERS)
        {2: {'orders': 2, 'total': 20, 'name': 'Person One',
        'email': 'email@one.com'},
         3: {'orders': 1, 'total': 15, 'name': 'Person Two',
         'email': 'email@two.com'}}
    """
    new_dict = {}
    for key in orders:
       cid = orders[key]['customer_id']
       if(orders[key]['customer_id'] in new_dict):
          new_dict[cid]['orders']=new_dict[cid]['orders']+1
          new_dict[cid]['total']=new_dict[cid]['total']+orders[key]['total']
       else:
          new_dict[cid]={}
          new_dict[cid]['name'] = customers[cid]['name']
          new_dict[cid]['email'] = customers[cid]['email']
          new_dict[cid]['orders'] = 1
          new_dict[cid]['total'] = orders[key]['total']
    return new_dict
