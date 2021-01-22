import sys
import csv

file = sys.argv[1]
columns = sys.argv[2:]
stdout_write = csv.writer(sys.stdout)

def sort_by_column(file, columns):
  def sort_by_column(row):
    sorted_columns = []
    for column in columns:
      column_num = int(column)
      sorted_columns.append(row[column_num])
    return sorted_columns

  rows = []
  with open(file, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
      rows.append(row)

  sorted_rows = sorted(rows, key=sort_by_column)
  with open(file, 'r') as f:
    for row in sorted_rows:
      stdout_write.writerow(row)

sort_by_column(file, columns)
