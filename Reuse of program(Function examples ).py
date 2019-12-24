def my_function(fname):
    print(fname + "danial")


my_function("john ")
my_function("Mike ")


# If we call the function without parameter, it uses the default value:
def countryname(country="Norway"):
    print("i am from " + country)


countryname("Pakistan")
countryname("")
countryname("china")


# You can send any data types of parameter to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def eat(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "orange"]
fruits.append("mango")
eat(fruits)


# return value
def cal(x):
    return 5 * x


print(cal(3))
print(cal(5))
print(cal(7))


# If the number of arguments are unknown, add a * before the parameter name:
def child(*kids):
    print("the youngest child is " + kids[2])


child("amy", "mandy", "sam")


def changeme(mylist):
    mylist.append([1, 2, 3, 4]);
    print("Values inside the function", mylist)
    return


mylists = [10, 20, 30, 40];
changeme(mylists);
print("Values outside the functioon:", mylists)


def changemy(mylist):
    mylist = [1, 2, 3, 4];
    print("Values inside the function", mylist);
    return


mylist = [10, 20, 30, 40];
changemy(mylist);
print("Values outside the function", mylist);


def printinfo(name, age):
    print("Name:", name)
    print("age:", age)
    return


printinfo('max', 35);
