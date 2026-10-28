# A program to calculate marks & grade of a student
import streamlit as st

st.title("Student Marks & Grade Calculator")

marks = []

for i in range(1, 6):
    mark = st.number_input(f"Enter marks for Subject {i}", 0, 100)
    marks.append(mark)

if st.button("Calculate Result"):

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    if all(mark >= 33 for mark in marks):
        status = "PASS"
    else:
        status = "FAIL"

    st.write("Total Marks:", total,)
    st.write("Percentage:",total,'/500','=',percentage, "%")
    st.write("Grade:", grade)
    st.write("Result:", status)