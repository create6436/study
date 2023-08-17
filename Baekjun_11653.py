def factorization(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i)
    if n > 1:
        print("소수:",n)

def main():
    N = int(input("소인수분해 할 숫자:"))
    if N == 1:
        return
    factorization(N)

if __name__ == "__main__":
    main()
