import csv, pandas, numpy

file_input = "data/application_record.csv"
file_output = "data/final_dataset.csv"
noise_percentage = 7

csv_file = pandas.read_csv(file_input)
amount = csv_file.size
noise_cell_number = int(amount * (noise_percentage / 100))
rand_rows = numpy.random.randint(low=1, high=csv_file.shape[0], size=noise_cell_number)
rand_cols = numpy.random.randint(low=1, high=csv_file.shape[1], size=noise_cell_number)
for row, col in zip(rand_rows, rand_cols):
    csv_file.iat[row, col] = numpy.nan
csv_file.to_csv(file_output, index=False)
