
def coin_change(coins, amount):

    # Create DP array
    dp = [float('inf')] * (amount + 1)

    # Base condition
    dp[0] = 0

    # Calculate minimum coins
    for i in range(1, amount + 1):
        for coin in coins:

            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    # Check if change is possible
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# Main Program
coins = [1, 2, 5]

amount = int(input("Enter amount: "))

result = coin_change(coins, amount)

if result == -1:
    print("Change cannot be made")
else:
    print("Minimum coins required:", result)
