input_strs = ["neetaaaaaa", "code", "love", "you"]


encoded = ''
for word in input_strs:
    size = len(word)
    encoded += str(size) + '#' + word
print(encoded)


decoded_list = []
length = len(encoded)
i = 0
while i < length:
    num_str = ''
    while encoded[i] != "#":
        num_str += encoded[i]
        i += 1
    i+=1
    end_word = i+int(num_str)
    print(i,end_word)
    word = encoded[i:end_word]
    decoded_list.append(word)
    i = end_word

print(decoded_list)