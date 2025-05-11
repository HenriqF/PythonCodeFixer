import ast

def analise(code):
    def findTab(i):
        findTabs = 0
        j = i-1
        while j >= 3:
            print("look:", code[j-3:j])
            if code[j-3:j] == "   ":
                findTabs += 1
                j-=3
            else:
                break
            j -= 1
        return(findTabs)
    
    biblios = []
    with open("library.txt", "r") as libr:
        biblios = ast.literal_eval(libr.read())

    viuPrint = False
    fried = ""

    i = 0
    while i < len(code):
        if code[i:i+6] == "print(":
            if not viuPrint:
                viuPrint = True
                fried = biblios[0] + fried
                nTabs = findTab(i)
                print(nTabs)
            if nTabs != 0:
                fried = fried[:-(nTabs*4)]

            tabfix = '\n'.join('    '*nTabs + line for line in biblios[1].splitlines())

            fried += tabfix
            i += 5
        else:
            fried += code[i]  
        i += 1
            
    return(fried)

print(analise('     print("aaa")'))

