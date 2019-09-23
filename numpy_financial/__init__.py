"""Some simple financial calculations

patterned after spreadsheet computations.

There is some complexity in each function
so that the functions behave like ufuncs with
broadcasting and being able to be called with scalars
or arrays (or other sequences).

Functions support the :class:`decimal.Decimal` type unless
otherwise stated.
"""

__all__ = ['fv', 'pmt', 'nper', 'ipmt', 'ppmt', 'pv', 'rate',
           'irr', 'npv', 'mirr']

from numpy_financial.financial import *



