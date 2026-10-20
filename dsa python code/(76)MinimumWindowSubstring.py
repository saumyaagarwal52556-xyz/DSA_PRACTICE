#isme hamne ek need name ka counter banaya jo t string ke character ki frequency store karega, fir hum s string me loop chalaenge agar s string ka character need me nhi h to usk0 need me dalke uski frequence negative me track karenge, or agar h to msising ko reduce karenge fir uski frequence kam karenge, 
#jab sabre character t ke mil jaenge matlb missing zero hoga tab ham shrink karna start karenge , string ham left, right ki help se karenge ,agar need[s[left]] ki frequence negative h to usko increase karo or left ko bhi increase karo,
#iske baad start or end ka modify karo right or keft ke basis pe, kyuki vo hi actual answer store karenga
# ham left ko increase karenge, ye dekhne ke liye kahi uske aage koi choti substring h ya nhi

from collections import Counter

def Minimumsubstring(s, t):
        if not s or not t or len(s) < len(t):
            return ""
        
        # 'need' stores the deficit count of characters we still need to find
        need = Counter(t)
        missing = len(t)
        
        start, end = 0, 0
        left = 0
        
        for right, char in enumerate(s):
            # If this character is needed (deficit > 0), decrement the missing count
            if need[char] > 0:
                missing -= 1
            
            # Reduce its deficit (can become negative if we have extra characters)
            need[char] -= 1
            
            # Once we have a valid window (no characters missing)
            if missing == 0:
                # Shrink from the left to discard unneeded or duplicate characters
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # Update our minimum window boundaries
                if end == 0 or (right - left) < (end - start):
                    start, end = left, right + 1
                    
                # Evict the character at 'left' to continue the search
                need[s[left]] += 1
                missing += 1
                left += 1
                
        return s[start:end]




str="ddaaabbca"
t="abc"
print(Minimumsubstring(str , t ))