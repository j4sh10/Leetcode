class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        newarray = []
        count = 0
        for word in words:
            if x in word:
                newarray.append(count)
            count += 1
        return newarray

        #################################
        # for word in range(len(words)):
        #     print(word)
        #################################
            # for char in word:
            #     if char == x:
            #         print(x)