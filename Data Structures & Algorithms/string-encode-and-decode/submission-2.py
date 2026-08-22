class Solution:
    '''String encoding and decoding: 
    Use Huffman Coding or a simpler approach first'''

    # Try a cipher first
    def encode(self, strs):
        # Add a word delimeter |
        encodedWord = ""
        for word in strs: 
            encodedWord = encodedWord + word + "\u00B6"

        return encodedWord
    

    def decode(self, encodedString):
        decodedWords = []
        currWord = ""
        for char in encodedString:
            if char == "\u00B6":
                decodedWords.append(currWord)
                currWord = ""
            else:
                currWord = currWord + char
        
        return decodedWords




