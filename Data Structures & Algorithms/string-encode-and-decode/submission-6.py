class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for char in s:
                encoded += chr((ord(char)+30)%256)
            encoded+=" "
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        for char in s:
            if char == " ":
                decoded.append(word)
                word = ""
            else:
                word += chr((ord(char)-30)%256)
        return decoded
