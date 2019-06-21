NPV = function(cashflow_dates, cashflow_amounts, discount_rate){
  stopifnot(length(cashflow_dates)==length(cashflow_amounts))
  days_in_year = 365 # we assume there are 365 days in each year
  times= as.numeric(difftime(cashflow_dates, cashflow_dates[1], units="days"))/days_in_year
  sum(cashflow_amounts/(1+discount_rate)^times)
}

xirr = function(cashflow_dates, cashflow_amounts){
  stopifnot(length(cashflow_dates)==length(cashflow_amounts))
  # we use uniroot function in R for root-finding
  uniroot(f=function(x) NPV(cashflow_dates,cashflow_amounts,x), interval= c(-1,100))$root
}

