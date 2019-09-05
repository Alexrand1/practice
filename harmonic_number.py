def harmonic_number(n, i=1):
    val = 1/i
    if i == n:
        return val + (1/i)
    else:
        return val + (harmonic_number(n, i+1))


print(harmonic_number(3))
