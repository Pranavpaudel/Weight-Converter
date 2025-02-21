
weight = float(input("Your weight: "))

weight_type= input("(k)gs or (l)bs: ")
weight_type.lower()
while weight_type != "k" and weight_type!="l":
    print("Invalid input. Type k for kg and l for lbs")
    weight_type = input("(k)gs or (l)bs: ")

if weight_type == "k":
    weight = weight * 2.2
    print("your weight in lbs is " + str(weight)+ "lbs")

elif weight_type == "l":
    weight = weight / 2.2
    print("Your weight in kgs is "+ str(weight) +  "kgs")


