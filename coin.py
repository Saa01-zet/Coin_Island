from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        INF = amount + 1

        dp = [INF] * (amount + 1)
        dp[0] = 0

        for current_sum in range(1, amount + 1):
            for coin in coins:
                if coin <= current_sum:
                    coins_for_rest = dp[current_sum - coin]

                    if coins_for_rest != INF:
                        candidate = 1 + coins_for_rest

                        if candidate < dp[current_sum]:
                            dp[current_sum] = candidate

        if dp[amount] == INF:
            return -1
        else:
            return dp[amount]

def test_coin_change():
    print("ПРОВЕРКА: Размен монет")

    sol = Solution()

    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = sol.coinChange(coins1, amount1)
    print(f"\nТест 1:")
    print(f"  Монеты: {coins1}")
    print(f"  Сумма: {amount1}")
    print(f"  Результат: {result1}")
    print(f"  Ожидалось: 3 (5 + 5 + 1)")
    print("Пройден!" if result1 == 3 else "Не пройден!")

    coins2 = [2]
    amount2 = 3
    result2 = sol.coinChange(coins2, amount2)
    print(f"\nТест 2:")
    print(f"  Монеты: {coins2}")
    print(f"  Сумма: {amount2}")
    print(f"  Результат: {result2}")
    print(f"  Ожидалось: -1 (нельзя набрать)")
    print("Пройден!" if result2 == -1 else "Не пройден!")

    coins3 = [1]
    amount3 = 0
    result3 = sol.coinChange(coins3, amount3)
    print(f"\nТест 3:")
    print(f"  Монеты: {coins3}")
    print(f"  Сумма: {amount3}")
    print(f"  Результат: {result3}")
    print(f"  Ожидалось: 0 (нет монет)")
    print("Пройден!" if result3 == 0 else "Не пройден!")

    coins4 = [1, 6, 7]
    amount4 = 13
    result4 = sol.coinChange(coins4, amount4)
    print(f"\nТест 4 (почему НЕ используем жадный алгоритм):")
    print(f"  Монеты: {coins4}")
    print(f"  Сумма: {amount4}")
    print(f"  Жадный алгоритм дал бы: 7 + 1*6 = 7 монет")
    print(f"  Оптимальное решение: 6 + 7 = 2 монеты")
    print(f"  Результат DP: {result4}")
    print("Пройден!" if result4 == 2 else "Не пройден!")

if __name__ == "__main__":
    test_coin_change()