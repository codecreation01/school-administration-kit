print ("basic school administration kit")
import csv

def write_into_csv (info_list):
    with open('student_info.csv'.'w+'.'newline')as csv file:
    writer=csv.writer(csv_file)
    writer.writerow (info_list)
if_name_=='_main_':
    condition=True
    student name=1
condition= True
while (condition):
      student_info=input("enter student information in format(Name.age.contact_number.Email_I'd)")
      print ("entered information:"+student_info)
      student_info_list=student_info.split(" ")
      print ("entered split up is:"+str(student_info_list))
      choice_check=input("is entered information correct?(yes/no):")
      if choice_check=="yes":
      write_into_csv (student_info_list)
      condition_check=input("enter(yes/no) if you want to enter information:")
      if condition_check=="yes":
          condition=True
      elif condition_check=="no"
          condition=False
