from collections import defaultdict
import numpy as np

#problem 1.1
def has_unique_chars(foo):
    chars = list(foo)
    chars.sort()
    for i ,_ in enumerate(chars):
        if i != len(chars) - 1 and chars[i] == chars[i+1]:
            return False
    return True
#problem 1.2
def is_permutation(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
#problem 1.3
def urlify(s1, tru_len):
    def rmUselessSpace(s2,i):
        end_index = i
        while s2[end_index] == " ":
            end_index += 1
        return s2[:i] + s2[end_index:]

    final = ""
    lst = ""
    for i in range(0,tru_len):
        if s1[i] == " " and lst != " ":
            final += "%20"
        elif s1[i] == " " and lst == " ":
            s1 = rmUselessSpace(s1,i)
            final += s1[i]
        else:
            final += s1[i]
        lst = s1[i]
        print(s1[i], i)
    return final
#problem 1.4
def perm_palindrone(s1):
    s1 = s1.replace(" ", "")
    print(s1)
    d = defaultdict(lambda: 0)
    for char in list(s1):
        d[char] += 1

    num_odd = 0
    for key in d.keys():
        if d[key] % 2 == 1:
            num_odd += 1

    if num_odd == 1:
        return True
    else:
        return False
#problem 1.5
def is_one_away(s1,s2):
    def get_longest(s1,s2):
        if len(s1) > len(s2):
            longest = s1
            shortest = s2
        else:
            longest = s2
            shortest = s1
        return longest, shortest

    def areSubstringsSame(long,short,i):
        if i < len(short)-1:
            sub = long[:i] + long[i+1:]
        else:
            sub = long[:i]

        return sub == short

    if s1 == s2:
        return True
    else:
        if len(s1) == len(s2):
            num_discrep = 0
            for i,val in enumerate(s1):
                if val != s2[i]:
                    num_discrep += 1
            return num_discrep == 1

        elif abs(len(s1) - len(s2)) == 1:
            longest, shortest = get_longest(s1,s2)
            for i, val in enumerate(longest):
                if i > len(shortest)-1 or val != shortest[i]:
                    return areSubstringsSame(longest,shortest,i)
        else:
            return False

#problem 1.6
def string_compression(s1):
    final_string = ""
    lst = s1[0]
    letter_counter = 1
    for char in s1[1:]:
        if char != lst:
            final_string += lst
            final_string += str(letter_counter)
            letter_counter = 1
            lst = char
        else:
            letter_counter += 1

    final_string += lst
    final_string += str(letter_counter)
    if len(final_string) >= len(s1):
        return s1
    else:
        return final_string

#problem 1.7


if __name__ == "__main__":
    print(string_compression("aacbbbbbb"))
