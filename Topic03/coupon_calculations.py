"""
Program: coupon_calculations.py
Author: Lily Ellison
Last date modified: 01/29/2023

The purpose of this program is to prompt the user for the amount of the purchase, the cash coupon, and the percent
coupon. Then calculate and return the order total, including tax and shipping.

"""

#Constants used in calculations:
TAX_RATE_FACTOR = 1.06 #multiply by subtotal to include tax rate of 6%

SHIP_10 = 10 #compare to subtotals to calculate shipping
SHIP_30 = 30
SHIP_50 = 50

SHIP_UNDER_10 = 5.95 #shipping fees
SHIP_UNDER_30 = 7.95
SHIP_UNDER_50 = 11.95
SHIP_OVER_50 = 0

CASH_5 = 5 #amounts for cash coupons
CASH_10 = 10

PERCENT_10 = 10 #compare to input of percentage amount on percentage discount
PERCENT_15 = 15
PERCENT_20 = 20

PERCENT_10_OFF = 0.9 #multiply by working subtotal to get amount after percentage discount applied
PERCENT_15_OFF = 0.85
PERCENT_20_OFF = 0.8

cashDiscount = 0 #initiation of cashDiscount, default value 0
percentDiscount = 1 #initiation of percentDiscount, default value 1 (1 - 0, since it's 0% off)
shippingRate = 100
"""Initiation of shippingRate, default set to 100 since this will always be changed, setting a high default helps alert 
me if there is a problem where this is not changed."""

purchaseAmount = input("Purchase total: ") #Input purchase amount, input is string
if purchaseAmount.isdigit(): #checks to see if input is a digit
    purchaseAmount = float(purchaseAmount) #casts input to float for calculations
    cashSubtotal = purchaseAmount #initiates cashSubtotal as purchaseAmount in case there is no cash coupon
    percentSubtotal = cashSubtotal #initiates percentSubtotal as cashSubtotal in case there is no percent coupon

    cashCouponCk = input("Cash Coupon?(Y/N): ") #checks to see if there is a cash coupon
    cashCouponCk = cashCouponCk.upper() #casts entry to uppercase for comparison

    if cashCouponCk != 'Y' and cashCouponCk != 'N': #checks for invalid options
        print("Invalid entry. No cash coupon discounted.")
    elif cashCouponCk == 'N': #selects for a valid negative entry
        print("No cash coupon discounted.")
    elif cashCouponCk == 'Y': #selects for a valid positive entry
        cashCoupAmt = input("Enter cash coupon amount (5 or 10): ") #prompts for cash coupon amount
        if cashCoupAmt.isdigit(): #checks if entry is a digit; removes invalid ones
            cashCoupAmt = float(cashCoupAmt) #casts input to float for calculations
            if cashCoupAmt != CASH_5 and cashCoupAmt != CASH_10: #removes invalid numbers
                print("Invalid entry. No cash coupon discounted.")
            else:
                cashDiscount = cashCoupAmt #sets cashDiscount to valid entry
            cashSubtotal = purchaseAmount - cashDiscount #calculates price after cash coupon discount
        else:
            print("Invalid entry. No cash coupon discounted.") #alerts user that entry was not valid
    print("Price after cash coupon: $" + '%.2f' % cashSubtotal) #updates user to the price after cash coupon

    percentCouponCk = input("Percent Coupon?(Y/N): ") #similar prompts to above
    percentCouponCk = percentCouponCk.upper()

    if percentCouponCk != 'Y' and percentCouponCk != 'N':
        print("Invalid entry. No percentage coupon discounted.")
    elif percentCouponCk == 'N':
        print("No percentage coupon discounted.")
    elif percentCouponCk == 'Y':
        percentCoupAmt = input("Enter percentage off (10, 15, or 20): ")
        if percentCoupAmt.isdigit():
            percentCoupAmt = float(percentCoupAmt)
            if percentCoupAmt != PERCENT_10 and percentCoupAmt != PERCENT_15 and percentCoupAmt != PERCENT_20:
                print("Invalid entry. No percentage coupon discounted.")
            elif percentCoupAmt == PERCENT_10 or percentCoupAmt == PERCENT_15 or percentCoupAmt == PERCENT_20:
                if percentCoupAmt == PERCENT_10:
                    percentDiscount = PERCENT_10_OFF
                elif percentCoupAmt == PERCENT_15:
                    percentDiscount = PERCENT_15_OFF
                elif percentCoupAmt == PERCENT_20:
                    percentDiscount = PERCENT_20_OFF
                percentSubtotal = percentDiscount * cashSubtotal
        else:
            print("Invalid entry. No percentage coupon discounted.")
    print("Price after percentage coupon: $" + '%.2f' % percentSubtotal)

    taxSubtotal = percentSubtotal * TAX_RATE_FACTOR #adds tax

    print("Price with 6% tax included: $" + '%.2f' % taxSubtotal)

    if taxSubtotal < SHIP_10: #selects for shipping cost
        shippingRate = SHIP_UNDER_10
    elif taxSubtotal < SHIP_30:
        shippingRate = SHIP_UNDER_30
    elif taxSubtotal < SHIP_50:
        shippingRate = SHIP_UNDER_50
    else:
        shippingRate = SHIP_OVER_50

    print("Shipping rate: $" '%.2f' % shippingRate) #informs user of shipping rate
    finalTotal = taxSubtotal + shippingRate #calculates total by adding shipping
    print("Final total: $" + '%.2f' % finalTotal) #prints final total

else:
    print("Invalid entry. Please try again.") #selects out invalid entries from first prompt

"""
Testing:

Input: h
Expected Output: "Invalid entry. Please try again."
Actual Output: "Invalid entry. Please try again."

Input: 100, n, n
Expected output: "No cash coupon discounted.; Price after cash coupon: $100.00; No percentage coupon discounted.; Price 
after percentage coupon: $100.00; Price with 6% tax included: $106.00; Shipping rate: $0.00; Final total: $106.00"
Actual Output: "No cash coupon discounted.; Price after cash coupon: $100.00; No percentage coupon discounted.; Price 
after percentage coupon: $100.00; Price with 6% tax included: $106.00; Shipping rate: $0.00; Final total: $106.00"

Input: 50, y, 10, n
Expected output: "Price after cash coupon: $40.00; No percentage coupon discounted.; Price after percentage coupon: 
$40.00; Price with 6% tax included: $42.40; Shipping rate: $11.95; Final total: $54.35"
Actual Output: "Price after cash coupon: $40.00; No percentage coupon discounted.; Price after percentage coupon: 
$40.00; Price with 6% tax included: $42.40; Shipping rate: $11.95; Final total: $54.35"

Input: 30, n, y, 10
Expected output: "No cash coupon discounted.; Price after cash coupon: $30.00; Price after percentage coupon: $27.00; 
Price with 6% tax included: $28.62; Shipping rate: $7.95; Final total: $36.57"
Actual Output:"No cash coupon discounted.; Price after cash coupon: $30.00; Price after percentage coupon: $27.00; 
Price with 6% tax included: $28.62; Shipping rate: $7.95; Final total: $36.57"

Input: 20, y, 10, y, 20
Expected output: "Price after cash coupon: $10.00; Price after percentage coupon: $8.00; 
Price with 6% tax included: $8.48; Shipping rate: $5.95; Final total: $14.43"
Actual Output: "Price after cash coupon: $10.00; Price after percentage coupon: $8.00; 
Price with 6% tax included: $8.48; Shipping rate: $5.95; Final total: $14.43"

Input: 100, x, x
Expected output: "Invalid entry. No cash coupon discounted.; Price after cash coupon: $100.00; Invalid entry. No 
percentage coupon discounted; Price after percentage coupon: $100.00; 
Price with 6% tax included: $106.00; Shipping rate: $0.00; Final total: $106.00"
Actual Output:"Invalid entry. No cash coupon discounted.; Price after cash coupon: $100.00; Invalid entry. No 
percentage coupon discounted; Price after percentage coupon: $100.00; 
Price with 6% tax included: $106.00; Shipping rate: $0.00; Final total: $106.00"

Input: 100, 5, 5
Expected output: "Invalid entry. No cash coupon discounted.; Price after cash coupon: $100.00; Invalid entry. No 
percentage coupon discounted; Price after percentage coupon: $100.00; 
Price with 6% tax included: $106.00; Shipping rate: $0.00; Final total: $106.00"
Actual Output:"Invalid entry. No cash coupon discounted.; Price after cash coupon: $100.00; Invalid entry. No 
percentage coupon discounted; Price after percentage coupon: $100.00; 
Price with 6% tax included: $106.00; Shipping rate: $0.00; Final total: $106.00"
"""