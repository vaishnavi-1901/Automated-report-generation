import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Load the dataset
df = pd.read_csv("sales.csv")

# Step 2: Calculate totals
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

# Step 3: Find top/low product by sales
product_sales = df.groupby("Product")["Sales"].sum()
top_product = product_sales.idxmax()
low_product = product_sales.idxmin()

# Step 4: Find top/low month by sales
month_sales = df.groupby("Month")["Sales"].sum()
top_month = month_sales.idxmax()
low_month = month_sales.idxmin()

# Step 5: Create PDF
pdf_file = "Sales_Report.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFont("Helvetica-Bold", 18)
c.drawString(200, 750, "Sales Performance Report")

c.setFont("Helvetica", 12)
y = 700

c.drawString(50, y, f"Total Sales: {total_sales}")
y -= 20
c.drawString(50, y, f"Total Profit: {total_profit}")
y -= 40

c.drawString(50, y, f"Top Product by Sales: {top_product} ({product_sales[top_product]})")
y -= 20
c.drawString(50, y, f"Lowest Product by Sales: {low_product} ({product_sales[low_product]})")
y -= 40

c.drawString(50, y, f"Top Month by Sales: {top_month} ({month_sales[top_month]})")
y -= 20
c.drawString(50, y, f"Lowest Month by Sales: {low_month} ({month_sales[low_month]})")
y -= 40

# Step 6: Save PDF
c.save()
print("✅ Sales_Report.pdf generated successfully!")