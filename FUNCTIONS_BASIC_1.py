#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# i predict this will print '5'
# i was right!


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# there will be an error because "number of.." was not defined
# i was right!


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# will only print 5, because that was the break in the function when the return was written
# yep!


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# still just 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# will print 5 because x calls on function.. or maybe they are too close..what is the none?


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# there wil be an error because b +c have not been defined..i was wrong nothing happened


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# 7 is my guess..and i was wrong it is 25
# i need to ask why this one is 25, and the one above is added differently..or watch the video


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    # it will print a value because b has been defined
    if b < 10:
        return 5
    else:
        return 10
        # this is where the function will break
    return 7
print(number_of_oceans_or_fingers_or_continents())
# 100 and 10..i was right

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# 7 then 14 then 7 then 14..it became 21 because it added up 7 and 14


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# will get 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# 500 then 500 then 300 then 500..because 500 is global value


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# 500 then 500 then 300 then 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# 500 then 500 then 300 then 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# 1 then 3 then 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 1 then 3 then 5 then 10.