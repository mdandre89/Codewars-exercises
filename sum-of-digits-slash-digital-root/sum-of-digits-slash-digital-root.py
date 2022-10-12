def digital_root(n):
    return (n - 1) % 9 + 1 if n>0 and n!=9 else 0