# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment_amount = 1000
month = 0

while principal > 0:
    month += 1
    current_payment = payment
    if month >= extra_payment_start_month and month < extra_payment_end_month:
        current_payment += extra_payment_amount

    principal = principal * (1+rate/12) - current_payment
    if principal < 0:
        current_payment += principal
        principal = 0

    total_paid += current_payment
    print(f'{month:10d} {total_paid:10.2f} {principal:10.2f}')

print(f'Total paid ${total_paid:0.2f}')
print('Months', month)
