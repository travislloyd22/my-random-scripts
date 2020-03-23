# Comma Code 
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, passing the previous spam list to the function would return 
# 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'snakes']
a_string = ''

# Returns a string with all the items separated by a comman and a space with *and*
# inserted before the last item
def spam_func(my_list):
    new_string = ''
    for i in range(len(my_list)):
        if i < len(my_list) - 1:
            new_string = new_string + my_list[i] + ', '
        else:
            new_string = new_string + 'and ' + my_list[i]
    return new_string

a_string = spam_func(spam)
print(a_string)