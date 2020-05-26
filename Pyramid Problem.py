def pyramid():
 rows = 0
 rows = int(input('Please enter number of rows: '))
 for count in range(rows):
  print(' '*(rows - count - 1) + '*'*(2*count +1))