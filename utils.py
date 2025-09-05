
def add(a, b):
    return a + b

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def normalize_text(s):
    return ' '.join(s.strip().split())

def parse_int_safe(s, default=None):
    try:
        return int(s)
    except Exception:
        return default

def unique_sorted(lst):
    return sorted(set(lst))

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def merge_dicts(a, b):
    res = a.copy()
    res.update(b)
    return res

def max_subarray_sum(arr):
    # Kadane's algorithm
    if not arr:
        return 0
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far
