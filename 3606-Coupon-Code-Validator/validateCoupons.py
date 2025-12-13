# leetcode 3606 Coupon Code Validator
'''
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

    - code[i]: a string representing the coupon identifier.
    - businessLine[i]: a string denoting the business category of the coupon.
    - isActive[i]: a boolean indicating whether the coupon is currently active.

A coupon is considered valid if all of the following conditions hold:

    1. code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
    2. businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
    3.isActive[i] is true.

Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

Constraints:

n == code.length == businessLine.length == isActive.length
1 <= n <= 100
0 <= code[i].length, businessLine[i].length <= 100
code[i] and businessLine[i] consist of printable ASCII characters.
isActive[i] is either true or false.
'''

# Solution
# Runtime: 7 ms, Memory: 18.21 MB
def validateCoupons(code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
    valid_items = []
    category_rank = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

    for c, b, a in zip(code, businessLine, isActive):
        if a and (c == "_" or c.replace("_", "").isalnum()) and b in category_rank:
            valid_items.append({"code": c, "line": b})

    valid_items.sort(key=lambda x: (category_rank[x["line"]], x["code"]))

    return [item["code"] for item in valid_items]

# Better Solution
# Runtime: 3 ms, Memory: 18.18 MB
def validateCoupons(code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
    def isValid(record):
        return (record[0] in valid_business and record[2] and record[1].replace('_', 'a').isalnum())

    valid_business = {"electronics", "grocery", "restaurant", "pharmacy"}

    ans = sorted(filter(isValid, zip(businessLine, code, isActive)))
    return [coupId for _, coupId, _ in ans]

# Test Case
code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]

output = ["PHARMA5","SAVE20"]
assert validateCoupons(code, businessLine, isActive) == output

code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
businessLine = ["grocery","electronics","invalid"]
isActive = [False,True,True]

output = ["ELECTRONICS_50"]
assert validateCoupons(code, businessLine, isActive) == output

code = ["2","E","Q","w","m","V","j","s","c","_","V","T"]
businessLine = ["pharmacy","electronics","pharmacy","invalid","invalid","pharmacy","pharmacy","electronics","restaurant","grocery","grocery","invalid"]
isActive = [False,False,True,True,True,True,True,False,False,True,False,False]

output = ["_","Q","V","j"]
assert validateCoupons(code, businessLine, isActive) == output

print("All test cases passed")
