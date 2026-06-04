your_fullname = input("Please enter your  name: ").lower()
partners_fullname = input("Please enter your partner's name: ").lower()

#count the number presence of both names  in true
both_names = your_fullname + partners_fullname
t_count = both_names.count("t")
r_count = both_names.count("r")
u_count = both_names.count("u")
e_count = both_names.count("e")

true_count = t_count + r_count + u_count + e_count

#count the number presence of both names in love
l_count = both_names.count("l")
o_count = both_names.count("o")
v_count = both_names.count("v")
e_count = both_names.count("e")

love_count = l_count + o_count + v_count + e_count
score  = int(str(true_count) + str(love_count))

print("Your matching score is "+ str(score) + "%")

if score <= 40:
    print("low score")
elif score >= 50:
    print("Middle range score")
elif score >= 70:
    print("High score")

