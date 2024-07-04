text1 = "Abdaurhman"
text2 = "namhruadbA"

matches = []

def compare2Text():
    
    wordLen = len(text1)
    
    if text1 == text2:
        
        return print("Matched")
    
    else:
        i = 0
        
        for g in range(wordLen * wordLen):
          for l in range(wordLen):
            
            if text1[i] == text2[l]:
                
                matches.append(text2[l])
                print(text2[l])
                
            else:
                pass
            
          if i < wordLen:
           i += 1
         
        if len(matches) == len(text1):
            
            return (print("Matched"))
        else:
            return (print("Not Matched"))
                

compare2Text()