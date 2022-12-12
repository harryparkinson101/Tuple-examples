# tuples

my_tuple = (1,2,3,4,5)
# this will error because a tuple is immutable so [1] cannot be changed
#my_tuple[1] = 'z'



#this will acess the second item in the tuple
print(my_tuple[2])

# this check to see if 5 is a value within my_tuple and returns a boolean value -> True
print(5 in my_tuple)

user = {
  (1,2): [1,2,3],
  'greet': 'hello',
  'age': 20
}
# this accesses the tuple key (1,2) and returns the value
print(user[(1,2)])

tuple = (1,2,3,4,5)
new_tuple = tuple[1]
# this will return (2,) as 2 is still a single tuple
print(new_tuple)

x,y,z, * other = (1,2,3,4,5)
# this will print 1
print(x)
# this will print everthing after y so [4,5]
print(other)

# .count()

tuple2 = (1,5,3,4,3,2,3,9)
# this counts the number of times input occurs in tuple 
print(tuple2.count(3))
# this returns 7 as 9 is the 7th index in the tuple
print(tuple2.index(9))
# this prints 8 because the count starts at 1
print(len(tuple2))
