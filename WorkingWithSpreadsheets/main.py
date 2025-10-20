import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

# List each company with respective product count
products_per_supplier = {}

for product_row in range(product_list.min_row + 1, product_list.max_row + 1):
    supplier_name = product_list.cell(product_row, 4).value
    if supplier_name in products_per_supplier:
        products_per_supplier[supplier_name] += 1
    else:
        products_per_supplier[supplier_name] = 1

print(products_per_supplier)