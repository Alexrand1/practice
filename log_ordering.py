ls = ["j je", "b fjt", "7 zbr", "m le", "o 33"]
a = []
d = []
def log_order(lst):
    for i in range(len(lst)):
        if lst[i].split()[1].isalpha():
            a.append(lst[i])
    ans = sorted(a, key=lambda c: c.split()[1])
    for j in range(len(lst)):
        if lst[j].split()[1].isnumeric():
            ans.append(lst[j])


    return ans

print(log_order(ls))