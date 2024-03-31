def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def print_prime(n):
    for i in range(2,n):
        if is_prime(i):
            print(i)
            print()
n=int(input("Enter the limit:"))
print_prime(n)