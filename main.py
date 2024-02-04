import pandas as pd
import glob
import fpdf
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, border=0, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, border=0, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add a header
    columns = list(df.columns)
    columns = [column.replace("_", " ").title() for column in columns]

    pdf.set_font(family='Times', style='B', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, border=1, txt=columns[0])
    pdf.cell(w=70, h=8, border=1, txt=columns[1])
    pdf.cell(w=35, h=8, border=1, txt=columns[2])
    pdf.cell(w=30, h=8, border=1, txt=columns[3])
    pdf.cell(w=30, h=8, border=1, txt=columns[4], ln=1)

    # Add roes to the table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, border=1, txt=str(row.product_id))
        pdf.cell(w=70, h=8,border=1, txt=str(row.product_name))
        pdf.cell(w=35, h=8, border=1, txt=str(row.amount_purchased))
        pdf.cell(w=30, h=8, border=1, txt=str(row.price_per_unit))
        pdf.cell(w=30, h=8, border=1, txt=str(row.total_price), ln=1)

    # Add total amount
    total_amount = df.total_price.sum()

    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, border=1, txt='')
    pdf.cell(w=70, h=8, border=1, txt='')
    pdf.cell(w=35, h=8, border=1, txt='')
    pdf.cell(w=30, h=8, border=1, txt='')
    pdf.cell(w=30, h=8, border=1, txt=str(total_amount), ln=1)

    # Add text for total amount statement
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=30, h=8, ln=1, txt=f'The total amount is {total_amount}')

    # Add python how logo
    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=25, h=8, txt='PythonHow')
    pdf.image(w=10, h=8, name="pythonhow.png")

    pdf.output(f"PDFs/{filename}.pdf")



