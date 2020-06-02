import xlrd
import xlwt
import openpyxl


def xls_read(file_path: str = '123.xls'):
    # WORK ONLY FOR .XLS
    excel_file = xlrd.open_workbook(file_path, formatting_info=True)
    sheets = excel_file.sheets()
    return sheets


def xlsx_read(file_path: str = '123.xlsx'):
    # WORK ONLY FOR .xlsx
    excel_file = openpyxl.load_workbook(filename=file_path)
    return {name: excel_file[name] for name in excel_file.sheetnames}

