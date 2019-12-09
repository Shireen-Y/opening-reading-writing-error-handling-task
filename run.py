from new_users import *
from read_write_names import *

New_users.new_file('users.txt')

person1 = New_users('1- James')
person2 = New_users('2- Jimmy')
person3 = New_users('3- Jimbob')
person4 = New_users('4- Ali')
person5 = New_users('5- Stacey')
person6 = New_users('6- Akon')
person7 = New_users('7- Drake')
person8 = New_users('8- Omarion')
person9 = New_users('9- Jack')
person10 = New_users('10- Mo')

writing_names('users.txt', person1.name)
writing_names('users.txt', person2.name)
writing_names('users.txt', person3.name)
writing_names('users.txt', person4.name)
writing_names('users.txt', person5.name)
writing_names('users.txt', person6.name)
writing_names('users.txt', person7.name)
writing_names('users.txt', person8.name)
writing_names('users.txt', person9.name)
writing_names('users.txt', person10.name)

reading_names('name.txt')
