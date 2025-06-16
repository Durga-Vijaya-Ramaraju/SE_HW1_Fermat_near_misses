"""
Title: Fermat Near Miss Finder
Filename: hw1_fermat_near_miss_finer.py
External files needed: None
External files created: None
Programmers: Durga Vijaya Ramaraju Pamidi, Yamini Parvathaneni
Emails: DurgaVijayaRamaraj@lewisu.edu, Yaminiparvathaneni@lewisu.edu
Course: SU25-CPSC-60500-001
Course Name: Software Engineering
Date submitted: 06-15-2025
Description:
    This program searches for "near misses" of Fermat’s Last Theorem
    where x^n + y^n ≈ z^n for integers x, y in [10, k] and 2 < n < 12.
Resources used:
    - Fermat’s Last Theorem: https://www.youtube.com/watch?v=ReOQ300AcSU
"""

def main():
    import math

    print("Fermat Near Miss Finder")
    print("Type 'exit' at any prompt to stop the program.\n")

    while True:
        # Ask for power n
        n_input = input("Enter an integer value for n (where 2 < n < 12): ")
        if n_input.lower() == 'exit':
            break
        k_input = input("Enter a maximum value for x and y (k > 10): ")
        if k_input.lower() == 'exit':
            break

        try:
            n = int(n_input)
            k = int(k_input)
        except ValueError:
            print("Please enter valid integer values for n and k.")
            continue

        # Validate input
        if n <= 2 or n >= 12 or k <= 10:
            print("Invalid input. Please follow the constraints.")
            continue

        smallest_rel_miss = 1.0  # Start with worst case
        best_result = None  # To store x, y, z, miss, rel_miss

        for x in range(10, k + 1):
            for y in range(10, k + 1):
                lhs = x ** n + y ** n  # x^n + y^n

                # Estimate z
                z = int(lhs ** (1 / n))
                z_power = z ** n
                z1_power = (z + 1) ** n

                # Calculate the absolute miss and relative miss
                miss1 = abs(lhs - z_power)
                miss2 = abs(z1_power - lhs)
                miss = min(miss1, miss2)

                rel_miss = miss / lhs

                if rel_miss < smallest_rel_miss:
                    smallest_rel_miss = rel_miss
                    best_result = (x, y, z, miss, rel_miss)
                    print(f"\nNew smallest relative miss found:")
                    print(f"x = {x}, y = {y}, z = {z}")
                    print(f"Miss = {miss}")
                    print(f"Relative Miss = {rel_miss:.7f}")
                    print("-" * 40)

        print("\nSearch complete.")
        if best_result:
            print("Smallest relative miss:")
            print(f"x = {best_result[0]}, y = {best_result[1]}, z = {best_result[2]}")
            print(f"Miss = {best_result[3]}")
            print(f"Relative diff = {best_result[4]:.7f}")
        else:
            print("No valid results found.")
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
