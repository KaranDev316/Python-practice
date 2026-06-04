your_fullname = input("Please enter your  name: ").lower()
partners_fullname = input("Please enter your partner's name: ").lower()
true_count = 0
love_count = 0
#count the number presence of both names  in true
both_names = your_fullname + partners_fullname
#t_count = both_names.count("t")
#r_count = both_names.count("r")
#u_count = both_names.count("u")
for i in "true":
    true_count +=both_names.count(i)
#true_count = t_count + r_count + u_count + e_count

#count the number presence of both names in love
for i in "love":
    love_count +=both_names.count(i)
#l_count = both_names.count("l")
#o_count = both_names.count("o")
#v_count = both_names.count("v")
#e_count = both_names.count("e")

#love_count = l_count + o_count + v_count + e_count
score  = int(str(true_count) + str(love_count))

print(f"Your matching score is  {score} %")
if score >= 80:
    print("Very high score")
elif score >= 70:
    print("High score")
elif score >= 50:
    print("Middle score")
else:
    print("low score")



