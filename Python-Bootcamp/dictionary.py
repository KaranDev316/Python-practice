student_data = [
    {
     "name" : "Ram",
     "roll_no" : 10,
     "age" : 20,
     "course" : "Python",

    }
    ,{
     "name" : "Mohan",
     "roll_no" : 20,
     "age" : 22,
     "course" : "Java",

     }

]
new_entry_data = ("Shyam", 22 ,18 , "c++")

new_dictionary = {"name": new_entry_data[0], "roll_no": new_entry_data[1], "age": new_entry_data[2]}

student_data.append(new_dictionary)


print(student_data)
