# 📌 Import libraries
import csv
from fpdf import FPDF

# 📌 Step 1: Read and analyze data from CSV
filename = "students.csv"
students = []
total_marks = 0

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["Name"]
        marks = int(row["Marks"])
        students.append((name, marks))
        total_marks += marks

average_marks = total_marks / len(students)

# 📌 Step 2: Create PDF using FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="🎓 Student Marks Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.set_fill_color(230, 230, 230)

# 📌 Table Headers
pdf.cell(100, 10, "Name", 1, 0, 'C', fill=True)
pdf.cell(40, 10, "Marks", 1, 1, 'C', fill=True)

# 📌 Table Rows
for name, marks in students:
    pdf.cell(100, 10, name, 1)
    pdf.cell(40, 10, str(marks), 1, 1)

# 📌 Summary Section
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, f"Total Marks: {total_marks}", ln=True)
pdf.cell(0, 10, f"Average Marks: {average_marks:.2f}", ln=True)

# 📌 Step 3: Save PDF File
pdf.output("student_report.pdf")
print("✅ PDF report generated as 'student_report.pdf'")
