def long_unique_substring(s):
    char_index = {}
    start = 0
    max_lenght = 0
    longest_sub = ""
    
    for i in range(len(s)):
        if i[s] in char_index and char_index[s[i]] >= start:
            start = char_index[s[i]] + 1
            
            char_index[s[i]] = i
            
            current_length = i - start + 1
            
            if current_length > max_length:
                max_length = current_length
                longest_sub = s[start:i+1]
                
            return longest_sub, max_length
        
s = "kjahdiqhigyguyewyu"
substring, length = long_unique_substring(s)
print("Longest str", substring)
print("Lenght", length)