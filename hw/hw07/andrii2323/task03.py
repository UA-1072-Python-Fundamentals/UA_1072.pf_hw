def count_characters(input_string):
    character_count = {}

    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count


input_str = "hello"
result = count_characters(input_str)
print(result)
