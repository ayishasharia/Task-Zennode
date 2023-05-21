# Product catalog
productNames = ["Product A", "Product B", "Product C"]
productPrices = [20, 40, 50]

# purchase
quantities = []
giftWraps = []
for i in range(len(productNames)):
    quantity = int(input("Enter quantity for {}: ".format(productNames[i])))
    quantities.append(quantity)
    giftWrap = input("Is {} wrapped as a gift? (yes/no): ".format(productNames[i]))
    giftWraps.append(giftWrap.lower() == "yes")

# Calculate product totals
productTotals = []
for i in range(len(productNames)):
    productTotal = quantities[i] * productPrices[i]
    if giftWraps[i]:
        productTotal += quantities[i] * 1  # including gift wrap fee
    productTotals.append(productTotal)

# Calculate subtotal
subtotal = sum(productTotals)

# Apply discount
discounts = []

if subtotal > 200:
    discounts.append(10)  # Flat $10 discount

if max(quantities) > 10:
    discounts.append(subtotal * 5 / 100)  # 5% discount

if sum(quantities) > 20:
    discounts.append(subtotal * 10 / 100)  # 10% discount

if sum(quantities) > 30 and max(quantities) > 15:
    tieredDiscount = max(subtotal - (15 * min(productPrices)), 0) * 50 / 100  # 50% discount on quantities above 15
    discounts.append(tieredDiscount)

if discounts:
    maxDiscount = max(discounts)
    if maxDiscount == 10:
        appliedDiscount = "flat10Discount"
    elif maxDiscount == subtotal * 5 / 100:
        appliedDiscount = "bulk5Discount"
    elif maxDiscount == subtotal * 10 / 100:
        appliedDiscount = "bulk10Discount"
    else:
        appliedDiscount = "tiered50Discount"
else:
    maxDiscount = 0
    appliedDiscount = "No discount applied"


# Calculate discount amount
discountAmount = maxDiscount

# Calculate shipping fee
shippingFee = (sum(quantities) // 10) * 5  # $5 shipping fee per package (10 products per package)

# Calculate total cost
total = subtotal - discountAmount + shippingFee

# Output results
print("Product Details:")
for i in range(len(productNames)):
    print("{} - Quantity: {}, Total: {}".format(productNames[i], quantities[i], productTotals[i]))
print("Subtotal:", subtotal)
print("Discount Applied:", appliedDiscount)
print("Discount Amount:", discountAmount)
print("Shipping Fee:", shippingFee)
print("Total:", total)