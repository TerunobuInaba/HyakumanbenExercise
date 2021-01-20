import csv

with open('./data.csv', 'w') as f:
  for i in range(114):
    x = i+1
    straight_NS = x
    left_NS = 59-straight_NS
    right_NS = 55-straight_NS
    straight_WE = straight_NS-2
    left_WE = 59-straight_NS
    right_WE = 55-straight_NS
    if (
      straight_NS <= 0
      or left_NS <= 0
      or right_NS <= 0
      or straight_WE <= 0
      or left_WE <= 0
      or right_WE <= 0
      ):
      continue
    w = csv.writer(f)
    # w.writerow([x, 4, 34])
    w.writerow([
      left_NS,
      straight_NS,
      right_NS,
      right_WE,
      left_WE,
      straight_WE,
      right_NS,
      straight_NS,
      left_NS,
      straight_WE,
      left_WE,
      right_WE
    ])   