
def is_palindrome(text: str) -> bool:
    cleaned = ""
    for ch in text:
        if not ch.isspace():
            cleaned += ch.lower()

    reversed_cleaned = cleaned[::-1]
    return cleaned == reversed_cleaned


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


def count_vowels(text: str) -> int:
    vowels = "aeiouyąęóAEIOUYĄĘÓ"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("discount must be between 0 and 1")

    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []
    stack = [nested_list]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)

    return result


def word_frequencies(text: str) -> dict:
    lower = text.lower()

    for ch in ",.!?;:\"'()-":
        lower = lower.replace(ch, " ")

    words = lower.split()

    freqs = {}
    for w in words:
        if w in freqs:
            freqs[w] += 1
        else:
            freqs[w] = 1

    return freqs


def is_prime(n: int) -> bool:

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

