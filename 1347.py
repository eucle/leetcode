def minSteps(s, t):
    s_dict, t_dict, steps = {}, {}, 0
    for a, b in zip(s, t):
        s_dict[a] = s_dict.get(a, 0) + 1
        t_dict[b] = t_dict.get(b, 0) + 1
    for letter in s_dict:
        if letter not in t_dict:
            steps += s_dict[letter]
        elif letter in t_dict and s_dict[letter] > t_dict[letter]:
            steps += s_dict[letter] - t_dict[letter]
    return steps


print(minSteps('bab', 'aba'))
print(minSteps('leetcode', 'practice'))
print(minSteps('anagram', 'mangaar'))
