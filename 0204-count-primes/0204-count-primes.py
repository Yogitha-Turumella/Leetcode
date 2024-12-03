class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0  # No primes less than 2
        
        # Create a boolean array to mark numbers as prime or not
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        # Use Sieve of Eratosthenes
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Count primes
        return sum(is_prime)