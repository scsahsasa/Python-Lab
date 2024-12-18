#Program to swap two tuples

#create two tuples
tuple1=(1,2,3)
tuple2=("red","pink","green","yellow")

#printing tuples before swap
print("Before Swapping : ")
print("Tuple 1 : ",tuple1)
print("Tuple 2 : ",tuple2)

#swaping 1st tuple to 2nd tuple and vice-versa
tuple1,tuple2=tuple2,tuple1

#printing tuples after swap
print("\nAfter Swapping : ")
print("Tuple 1 : ",tuple1)
print("Tuple 2 : ",tuple2)
