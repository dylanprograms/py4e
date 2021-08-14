
fruits = ['lime', 'grapefruit', 'banana', 'orange']
def list_maker(lst):
    for i in lst:
        print(i)

list_maker(fruits)


newf = input("What other fruits can you think of? Enter done to finish the list. ")
while newf != "done":
    fruits.append(newf)
    list_maker(fruits)
    newf = input("More fruits? ")

if newf == "done":
    print("You have " + str(len(fruits)) + " types of fruit!")
    print(fruits)