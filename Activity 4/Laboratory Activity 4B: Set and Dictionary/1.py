A = {'a', 'b', 'c', 'h', 'i', 'j', 'k'}
B = {'b', 'c', 'd', 'f', 'h'}
C = {'c', 'd', 'f', 'l', 'm', 'o'}

print(f"a. Elements in set A: {len(A)}")
print(f"   Elements in set B: {len(B)}")

b_not_in_a_and_c = B - (A | C)
print(f"b. Elements in B that are not in A and C: {len(b_not_in_a_and_c)}")

result_i = A - (B | C - {'h'})
print(f"c.i. {sorted(result_i)}") 

result_ii = B & C
print(f"c.ii. {sorted(result_ii)}")

result_iii = A & B
print(f"c.iii. {sorted(result_iii)}")

result_iv = (B & C) - A
print(f"c.iv. {sorted(result_iv)}")

result_v = A & B & C
print(f"c.v. {sorted(result_v)}")

result_vi = C - (A | B)
print(f"c.vi. {sorted(result_vi)}")