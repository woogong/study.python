my_name = "Jones"
my_age = 34
message = "My name is \"{}\" and my age is {}".format(my_name, my_age)
print(message)

table = {'ha': '20170706', 'ye': '19940328', 'go': '20100430'}
message2 = "Birthday of {dongun}, {yeongun} and {goeun}".format(**table)
print(message2)

word1 = "|" + "정재봉".center(5) + "|"
print(word1)