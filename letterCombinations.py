class Solution:
    def letterCombinations(self, digits: str):
        if digits=="":
            return []

        num_map = {}
        num_map['2'] = ['a','b','c']
        num_map['3'] = ['d','e','f']
        num_map['4'] = ['g','h','i']
        num_map['5'] = ['j','k','l']
        num_map['6'] = ['m','n','o']
        num_map['7'] = ['p','q','r','s']
        num_map['8'] = ['t','u','v']
        num_map['9'] = ['w','x','y','z']
        product = ['']
        for k in digits:
            product = [s+i for s in product for i in num_map[k]]
        return product
di = "23"
so=Solution()
print(so.letterCombinations(di))