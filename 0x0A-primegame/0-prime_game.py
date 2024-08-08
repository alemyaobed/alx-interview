#!/usr/bin/python3
""" Prime Game """

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_counts_up_to(n):
    """Calculate number of primes up to each number from 1 to n."""
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
        prime_count[i] = count
    return prime_count

def isWinner(x, nums):
    """Determine the winner of the most rounds."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    prime_count = get_prime_counts_up_to(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Maria wins if the number of primes up to n is odd, otherwise Ben wins
        if prime_count[n] % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        # Return None if the winner cannot be determined
        return None
