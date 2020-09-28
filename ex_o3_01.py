sh = input("Enter Hours: ")
sr = input("Enter Rate:  ")
fh = float(sh)
#print(sh, sr)
if sh > 40:
    # print('Overtime:')
    reg = sr * sh
    otp = (sh - 40.0) * (sr * 0.5)
    # print(reg,otp)
    fh = reg + otp
    pass
else fh <= 40:
    # print('Regular')
    Pay = fh * otp
print("Pay:", xp)
