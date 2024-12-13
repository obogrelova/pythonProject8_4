import csv


def clean_price(price):
    return int(price.replace('руб.', '').replace(' ', ''))

input_file = 'price.csv'
output_file = 'cleaned_price.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)
print(f'Обработанные файлы сохранены в файл {output_file}')


