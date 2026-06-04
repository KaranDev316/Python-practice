first_fullname = input("Please enter your first name: ").lower()
second_fullname = input("Please enter your last name: ").lower()

both_names = first_fullname +second_fullname
t_count = both_names.count("t")
r_count = both_names.count("r")
u_count = both_names.count("u")
e_count = both_names.count("e")

true_count = t_count + r_count + u_count + e_count
print(true_count)
print(both_names)