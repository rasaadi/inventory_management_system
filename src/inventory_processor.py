import pandas as pd
from src import resource_config


class InventoryProcessor:
    def __init__(self):
        self.customer_file = resource_config.CUSTOMER_FILE_PATH
        self.invoice_file = resource_config.INVOICE_FILE_PATH
        self.item_file = resource_config.ITEM_FILE_PATH

    def read_customer_info(self, customer_name):
        # Assuming no duplicate customer exist
        print("Reading customer info")
        if customer_name is not None:
            c_fname = '”{}”'.format(customer_name[0])
            c_laname = '”{}”'.format(customer_name[1])

            df = pd.read_csv(self.customer_file, sep=',')

            print("Customer search: {0} {1}".format(c_fname, c_laname))
            customer = df.loc[(df['”FIRST_NAME”'] == '{}'.format(c_fname)) &
                              (df['”LAST_NAME”'] == '{}'.format(c_laname))]

            print("Customer: \n{}".format(customer))
            return customer['“ID”'].to_list()

    def read_invoice_info(self, customer_id_lst):
        print("Reading invoice info")
        # Assume only one item in the customer_id_lst list
        if customer_id_lst is not None:
            df = pd.read_csv(self.invoice_file, sep=',')

            print("Invoice search: {}".format(customer_id_lst[0]))
            invoices = df.loc[
                (df['“CUSTOMER_ID”'] == '{}'.format(customer_id_lst[0]))]
            print("Invoices: \n{}".format(invoices))
            return invoices['”INVOICE_ID”'].to_list()

    def read_items_info(self, invoice_lst):
        print("Reading item info")
        items_dict = {}

        if invoice_lst is not None:
            df = pd.read_csv(self.item_file, sep=',')
            print(df.head())
            print("Items search: {}".format(invoice_lst))
            for invoice in invoice_lst:
                items = df.loc[(df['“INVOICE_ID”'] == '{}'.format(invoice))]
                items_dict[invoice] = items

        # for k, v in items_dict.items():
        #     print(k, v)
        return items_dict

    def calcualte_total_amount(self, item_dict):
        print("Calculating total mount/spent")
        total = []
        for k, v in item_dict.items():
            print("Customer Purchase History: \n{}".format((k, v)))
            amounts = v['”AMOUNT”'].to_list()

            # Cleaning up the amount
            clean_amount = []
            for item in amounts:
                clean_amount.append(item.replace('”', ''))

            # Converting amount to num/float
            for i in range(0, len(clean_amount)):
                # Expecting float decimal points issue
                clean_amount[i] = float(clean_amount[i])

            total.append(sum(clean_amount))
        print("total: {}".format(total))
        return total
