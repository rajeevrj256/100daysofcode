class Solution(object):
    def backspaceCompare(self, s, t):
        def process_string(input_str):
            result = []
            for char in input_str:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return "".join(result)

        processed_s = process_string(s)
        processed_t = process_string(t)

        return processed_s == processed_t
