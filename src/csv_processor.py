import os
import sys
import csv

sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from src import resource_config


class CsvProcessor:
    def __init__(self):
        self.customer_file = resource_config.CUSTOMER_FILE_PATH
        self.invoice_file = resource_config.INVOICE_FILE_PATH
        self.item_file = resource_config.ITEM_FILE_PATH

    def customer_generator(self):
        print("Generating Customer Information...")
        with open(self.customer_file, 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', )
            next(csv_reader)
            for line in csv_reader:
                yield line
                # print(row)

    def customer_processor(self, customer_file_gen, customer_name):
        print("Processing Customer Information...")
        for line in customer_file_gen:
            if line[1] == customer_name[0] and line[2] == customer_name[1]:
                print("Matched customer details: {}".format(line))
                return line[0]  # Customer ID

    def invoice_generator(self):
        print("Generating Invoice Information...")
        with open(self.invoice_file, 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', )
            next(csv_reader)
            for line in csv_reader:
                yield line
                # print(row)

    def invoice_processor(self, invoice_generator, customer_id):
        print("Processing Invoice Information...")
        invoice_list = []
        for line in invoice_generator:
            # print(line)
            if line[0] == customer_id:
                print("Matched invoice details: {}".format(line))
                invoice_list.append(line[1])

        if len(invoice_list) == 0:
            print("No matched INVOICE record found")
        else:
            return invoice_list

    def item_generator(self):
        print("Generating Item Information...")
        with open(self.item_file, 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', )
            next(csv_reader)
            for line in csv_reader:
                yield line
                # print(row)

    def item_processor(self, invoice_generator, invoice_id_lst):
        print("Processing Item Information...")
        # print("Invoice id: {}".format(invoice_id_lst))
        item_dict = {}
        for line in invoice_generator:
            # print(line)
            for invoice in invoice_id_lst:
                if line[0] == invoice:
                    print("Matched item details: {}".format(line))
                    item_dict[line[1]] = line

        if len(item_dict) == 0:
            print("No matched ITEM record found")
        else:
            # for k, v in item_dict.items():
            #     print(k, v)
            return item_dict
        # #
        # # for k, v in item_dict.items():
        # #     print("Printing item dictionary")
        # #     print(k, v)
        # return item_dict

    def total_calculator(self, item_dictionary):
        print("Calculating total amount...")
        amounts = []
        clean_amount = []
        if item_dictionary is not None:
            for k, v in item_dictionary.items():
                # print(type(v))
                # print(v[2])
                amounts.append(v[2])

        # Cleaning up the amount
        for item in amounts:
            clean_amount.append(item.replace('”', ''))

        # Converting amount to num/float
        for i in range(0, len(clean_amount)):
            # Expecting float decimal points issue
            clean_amount[i] = float(clean_amount[i])
        total = sum(clean_amount)
        print("total: {}".format(total))
        return total


reader = CsvProcessor()

# customer_id = reader.customer_processor(reader.customer_generator(),
#                                         ['”Olivia”','”Johnson”'])
customer_id = reader.customer_processor(reader.customer_generator(),
                                        ['”Indiana”', '”Jones”'])
# customer_id = reader.customer_processor(reader.customer_generator(),
#                                         ['”Harper”','”Moore”'])
print(customer_id)

invoice_id = reader.invoice_processor(reader.invoice_generator(), customer_id)
print(invoice_id)

items = reader.item_processor(reader.item_generator(),
                              ['“IN0999987”', '“IN0999999”'])

# items = reader.item_processor(reader.item_generator(), invoice_id)

total = reader.total_calculator(items)
