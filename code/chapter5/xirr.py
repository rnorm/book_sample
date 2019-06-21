from datetime import datetime
from scipy.optimize import root

def NPV(cashflow_dates, cashflow_amounts, discount_rate):
  assert len(cashflow_dates)==len(cashflow_amounts), "inconsistent lengths of cashflows dates and amounts"
  days_in_year=365.0
  times = [(e-cashflow_dates[0]).days/days_in_year for e in cashflow_dates]
  return sum(cashflow_amounts[i]/(1.0+discount_rate)**e for i,e in enumerate(times))

def xirr(cashflow_dates, cashflow_amounts):
  # we use the scipy.optimize.root function to find the root
  return root(fun=lambda x:NPV(cashflow_dates,cashflow_amounts,x),x0=[0.0]).x
