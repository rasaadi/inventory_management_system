import argparse

from src.inventory_processor import InventoryProcessor


# def main(argv):
def main():
    # Having issue with the argparse, hence disabling it for now
    # parser = argparse.ArgumentParser()
    # parser.add_argument("first_name",
    #                     help="Customer First Name")
    # parser.add_argument("last_name", help="Customer Last Name")
    # args = parser.parse_args()
    #
    # first_name = args.first_name
    # last_name = args.last_name
    # customer_name = [first_name, last_name]

    '''
    Customer name is hardcoded at this point since arg parser is not working at
    this moment
    '''

    customer_name = ['Indiana', 'Jones']

    iprocessor = InventoryProcessor()
    customer_id = iprocessor.read_customer_info(customer_name)
    invoice = iprocessor.read_invoice_info(customer_id)

    '''
    NO idea why the item search cannot find the items for the invoices
    found in the previous call :-(
    '''
    # items = iprocessor.read_items_info(invoice)
    # print(items)

    # Strangely item search works for the following invoices:
    # ['“IN00”', '“IN01”']
    items = iprocessor.read_items_info(['“IN00”', '“IN01”'])
    total = iprocessor.calcualte_total_amount(items)


if __name__ == "__main__":
    main()
    # main(sys.argv[1:])
