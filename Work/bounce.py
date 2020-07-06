# bounce.py
#
# Exercise 1.5

height = 100
total_bounces = 10
bounce = 0

while bounce < total_bounces:
    height = height * (3/5)
    bounce = bounce + 1
    print(bounce, round(height, 4))

