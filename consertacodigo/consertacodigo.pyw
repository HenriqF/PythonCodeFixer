import tkinter as tk
import ast
import random

#criar a porra toda
#########################################
janela = tk.Tk()
janela.geometry('1250x950')
janela.title("Fix ts rn is so kevin🥀")

#Código que roda quando eu quero
#########################################



def analise(code):
    def findTab(i):
        findTabs = 0
        j = i-1
        while j >= 3:
            if code[j-3:j] == "   ":
                findTabs += 1
                j-=3
            else:
                break
            j -= 1
        return(findTabs)
    
    def analise(s):
        out = ""
        c = {'(':')','[':']','{':'}','"':'ma',"'":"ma"}
        c2 = {')':"(","]":"[","}":"{"}

        i = 0
        stack = []
        while i < len(s):
            char = s[i]
            if char in c.keys():
                if c[char] == "ma":
                    i += 1
                    while i < len(s) and s[i] != char:
                        i += 1
                else:
                    stack.append(char)
            elif char in c2.keys():
                if stack and stack[-1] == c2[char]:
                    stack.pop()
                else:
                    return("if inline")

            elif char == ":":
                if not stack:
                    return(True, i)

            elif char == "e":
                try:
                    if s[i+1:i+4] == "lse":
                        if not stack:
                            return("if ternario")
                except:
                    pass

            elif stack == []:
                out += char
            i += 1
        return("saporran ao conmpensa")


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
            if nTabs != 0:
                fried = fried[:-(nTabs*4)]

            tabfix = '\n'.join('    '*nTabs + line for line in biblios[1].splitlines())

            fried += tabfix
            i += 5


        if code[i:i+2] == "if" or code[i:i+4] == "elif":
            ans = analise(code[i:])
            if ans[0] == True:
                idxdoisponto = i+ans[1]
                arg = code[i+2:idxdoisponto] if code[i:i+2] == "if" else code[i+4:idxdoisponto]

                bvalue = random.randint(4, 20)
                pos = random.randint(0,99)
                final = " or" + arg
                for j in range(bvalue):
                    pos = random.randint(0,99)
                    final = f" or {biblios[2][pos]}" + final
                bvalue = random.randint(4, 20)
                for j in range(bvalue):
                    pos = random.randint(0,99)
                    final += f" or {biblios[2][pos]}"

                final += ":"
                final = final[4:]

                fried += "if " if code[i:i+2] == "if" else "elif "
                fried += final
                i = idxdoisponto
            else:
                fried += "if " if code[i:i+2] == "if" else "elif "
                i += 2 if code[i:i+2] == "if" else 4


        else:
            fried += code[i]  
        i += 1
            
    return(fried)
#funcoes tkinter
#########################################
def enviar():
    user_text = input.get("1.0", tk.END).strip()
    result = analise(user_text)
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert(tk.END, str(result))
    # janela.clipboard_clear()
    # janela.clipboard_append(result)
    janela.update()

def atualizar(*args):
    enviar()

#Detalhes, textos
#########################################
textoinput = tk.Label(janela, text="Coloque a porra nojenta aqui ❌")
textoinput.grid(row=0, column=1, padx=10, pady=10)
textoinput2 = tk.Label(janela, text="Resultado fix 100% ✅:")
textoinput2.grid(row=0, column=2, padx=10, pady=10)

#Botoes
#########################################
botao = tk.Button(janela, text="Go go go", command=atualizar, width=80, height=2)
botao.grid(row=2, column=1, padx=10, pady=10)

#Caixas de input, output
#########################################
output = tk.Text(janela, height=50, width=75, state=tk.DISABLED)
output.grid(row=1, column=2, padx=10, pady=10)

input = tk.Text(janela, height=50, width=75)
input.grid(row=1, column=1, padx=10, pady=10)
input.bind("<KeyRelease>", atualizar)

#necessario
#########################################
janela.mainloop()