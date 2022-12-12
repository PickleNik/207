def powerset(s):
  s = list(s)
  if len(s) == 0:
    return [{}]

  sub_powerset = powerset(s[1:])
  modified_subsets = []
  for subset in sub_powerset:
    subset = list(subset)
    subset.append(s[0])
    subset = set(subset)
    modified_subsets.append(subset)

  return sub_powerset + modified_subsets
def primefactor(n):
  primes = []
  i = 2
  while i <= n:
    if n % i == 0:
      primes.append(i)
      n /= i
    else:
      i += 1
  return primes
def primesumoftwo(ns):
  def is_a_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime
  def is_sum_of_two_primes(n):
    for i in range(2, n):
        if is_a_prime(i) and is_a_prime(n - i):
            print(n, '=', i, '+', n - i)
            return True
    print(n, 'is not a sum of two primes')
    return False
  for x in ns:
    if not is_sum_of_two_primes(x):
      return False

  return True
def powmodularithmetic(base, exponent, modulus):
    print(base, '^', exponent,'%', modulus, '=')
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent >> 1
        base = (base * base) % modulus
    
    print(result, '\n')
    return result
def truthtable(condition):
  variables = list(set(filter(str.isalpha, condition)))
  combinations = [dict(zip(variables, values))
    for values in [
      (True, True),
      (True, False),
      (False, True),
      (False, False)
    ]
  ]
  results = [eval(condition, globals(), combination)
    for combination in combinations
  ]

  print('\t'.join(variables + ['result']))
  for combination, result in zip(combinations, results):
    print('\t'.join([str(combination[var]) 
      for var in variables
    ] + [str(result)]))
def completegraphedges(n):
  return int(n * (n - 1) / 2)

s = {}
print('\npowerset test empty set :\n', powerset(s))
s = {1, 2, 3}
print('\npowerset test { 1, 2, 3 } :\n', powerset(s))
s = {0,0,1,0,1,0}
print('\npowerset test {0,0,1,0,1,0} :\n', powerset(s))

print('\n primefactor test 2 :\n', primefactor(2))
print('\n primefactor test 10 :\n', primefactor(10))
print('\n primefactor test 13 :\n', primefactor(13))
print('\n primefactor test 22 :\n', primefactor(22))
print('\n primefactor test 69 :\n', primefactor(69))
print('\n primefactor test 100 :\n', primefactor(100))
print('\n primefactor test 1000 :\n', primefactor(1000))

print(primesumoftwo([4,5,6]))
print(primesumoftwo([69, 420, 1337]))
print(primesumoftwo([10, 12, 13, 14, 15, 16, 17, 18]))

powmodularithmetic(2, 10, 12)
powmodularithmetic(69, 420, 1337)
powmodularithmetic(123, 123, 123)
powmodularithmetic(100000, 1234567, 3)

truthtable('(A | B)')
truthtable('(A & B)')
truthtable('(A & B) | A')
truthtable('(A | B) & (A & B)')

print(completegraphedges(20))
print(completegraphedges(3000))
print(completegraphedges(100000))
