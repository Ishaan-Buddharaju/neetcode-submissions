class Solution:
    '''String encoding and decoding: 
    Use Huffman Coding or a simpler approach first'''

    # Try a delimeter first
    # def encode(self, strs):
    #     # Add a word delimeter |
    #     encodedWord = ""
    #     for word in strs: 
    #         encodedWord = encodedWord + word + "\u00B6"

    #     return encodedWord
    

    # def decode(self, encodedString):
    #     decodedWords = []
    #     currWord = ""
    #     for char in encodedString:
    #         if char == "\u00B6":
    #             decodedWords.append(currWord)
    #             currWord = ""
    #         else:
    #             currWord = currWord + char
        
    #     return decodedWords

    def encode(self, words):
        encodedString = ""
        for word in words:
            encodedString = encodedString + str(len(word)) + "#" + word
        return encodedString

    def decode(self, encodedString):
        output = []
        currWord = ""

        i = 0
        while (i < len(encodedString)):
            nextLength = ""
            while encodedString[i] != "#":
                nextLength = nextLength + encodedString[i]
                i += 1
            nextLength = int(nextLength)

            for j in range(i + 1, i + nextLength + 1):
                currWord = currWord + encodedString[j]

            output.append(currWord)
            currWord = ""
            i += nextLength + 1

        return output

 






