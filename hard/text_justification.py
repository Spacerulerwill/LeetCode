# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # split the words into groups of words that can be justified in one line together
        word_groups = []
        current_len_total = 0
        current_group = []
        for word in words:
            if len(current_group) == 0:
                current_group.append(word)
                current_len_total += len(word)
            else:
                if current_len_total + len(word) + 1 > maxWidth:
                    word_groups.append(current_group)
                    current_len_total = len(word)
                    current_group = [word]
                else:
                    current_group.append(word)
                    current_len_total += len(word) + 1
        word_groups.append(current_group)

        lines = []
        # proess all but last
        for i in range(len(word_groups)-1):
            group = word_groups[i]
            total = sum(len(string) for string in group)
            spaces = maxWidth - total

            if len(group) == 1:
                lines.append(group[0].ljust(maxWidth))
            else:
                # we have an amount of spaces to distribute evenly between an amount of words
                quotient = spaces // (len(group)-1)
                remainder = spaces % (len(group)-1)
                pieces = [quotient] * (len(group)-1)
                for i in range(remainder):
                    pieces[i] += 1
                
                # construct the line - it is now center justified
                line = ""
                for i in range(len(group)-1):
                    line += group[i]
                    line += (" " * pieces[i])
                line += group[-1]
                lines.append(line)
                
        # process last
        last_line = (" ".join(word_groups[-1])).ljust(maxWidth)
        lines.append(last_line)
        return lines



if __name__ == "__main__":
    solution = Solution()
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))