
def creatinine_clearance_calculator(age, weight, sex, serum):
    '''
    function to generate creatinine clearance rate
    parameters = age in years, weight in kg, sex, serum creatinine in micromol/L
    returns = creatinine clearance rate in mL/minute
    '''
    if sex == 'm':
        constant = 1.23
        creatinine_clearance_rate = ((140 - int(age)) * int(weight) * constant) / int(serum)
    elif sex == 'f':
        constant = 1.04
        creatinine_clearance_rate = ((140 - int(age)) * int(weight) * constant) / int(serum)
    else:
       creatinine_clearance_rate = 0
    return creatinine_clearance_rate

