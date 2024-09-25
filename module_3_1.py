calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):   
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result
    

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if item.lower() == string.lower():
            return True
    return False    


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)