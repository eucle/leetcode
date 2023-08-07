def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
    if purchaseAmount in {5, 25, 45, 65, 85}:
        return round(100 - purchaseAmount, -1) - 10
    else:
        return round(100 - purchaseAmount, -1)


print(accountBalanceAfterPurchase(9))
print(accountBalanceAfterPurchase(15))
