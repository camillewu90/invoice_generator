import pandas as pd
import glob
import fpdf


filepaths = glob.glob("invoices/*.xlsx")
for file in filepaths:
    df = pd.read_excel(file, sheet_name="Sheet 1")
    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.output(f"{file.replace('xlsx','pdf')}")



