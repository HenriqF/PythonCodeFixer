import tkinter as tk
import ast
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
#funcoes tkinter
#########################################
def enviar():
    user_text = input.get("1.0", tk.END).strip()
    result = analise(user_text)
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert(tk.END, str(result))
    janela.clipboard_clear()
    janela.clipboard_append(result)
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
input.bind("<Return>", atualizar)


#necessario
#########################################
janela.mainloop()