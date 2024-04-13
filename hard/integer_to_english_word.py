# https://leetcode.com/problems/integer-to-english-words/description/

digits = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
others = ["Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        # split number into chunks of 3 digits
        chunks = []
        while num > 0:
            chunk = 0
            for i in range(3):
                digit = num % 10
                chunk += digit * 10**i
                num //= 10
            chunks.append(chunk)
        print(chunks)
    
        # converts chunks of < 1000 into words
        result = []
        for idx in range(len(chunks)):
            chunk = chunks[idx]
            if chunk == 0:
                if chunks[idx+1] != 0:
                    result.append(others[idx])
            else:
                if idx - 1 >= 0 and chunks[idx-1] != 0:
                    result.append(others[idx-1])

                if 10 < chunk % 100 < 20:
                    if chunk // 100 != 0:
                        # 3 digit
                        result.append(teens[(chunk % 100) - 11])
                        result.append("Hundred")
                        result.append(digits[(chunk // 100) - 1])
                    else:
                        # 2 digit
                        result.append(teens[(chunk % 100) - 11])
                else:      
                    i = 0
                    while chunk > 0:
                        digit = chunk % 10
                        if digit != 0:
                            if i == 0:
                                result.append(digits[digit - 1])
                            elif i == 1:
                                result.append(tens[digit - 1])
                            elif i == 2:
                                result.append("Hundred")
                                result.append(digits[digit - 1])
                        chunk //= 10
                        i += 1
        return " ".join(reversed(result))

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberToWords(1000000))