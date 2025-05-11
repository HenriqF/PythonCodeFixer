# if inline conditional:
# nums = [1, 2, 3, 4, 5]
# even_nums = [x for x in nums if x % 2 == 0]

# if ternario:
# result = True if 10 > 0 else False

# if normal:
# if 1 == 1:
#     pass

# if normal encontra um ":"
# if ternario encontra um "else"
# if inline encontra um "]"
# --> quero o index do fim

# pode-se encontrar um ":" ou um "]" antes do esperado:

# if a[1] == 0:
#       ^
# if {1: "skendel"}[1] == "skendel":
#      ^

# proposta: ignorar tudo dentro de porrinhas ( "(,[,{" ) completas:

#     fod     v
# if a[1] == 0:

# if {1: "skendel"}[1] == "skendel":
#    fodasefodasefodas             ^

#eu só quiero saber de : se nao for dois pontos eu nao me importo isto é porque eu sou muito incrivel e decolado
#vou assumir que aspas estao 100% fechadas e que as porrinhas 100% certas.


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
                return("Esse é um if que vai dar pra fazer o bagulho bala")

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



#CASOS QUE DERAM CERTO: --> is us chatgpt u so negakevin lov u megapoet🌹❤️‍🩹

#if (x > 10 and y < 5) or (z == 3) == True:
#if my_list[2][1] == "valor":
#if (x & 0b1010) == 0b1000:
#if 10 > 5 else (20 < 30 if True else False):
#if (lambda x: x * 2)(y) > 5 else False:
#if len("alguma_string") == 15:
#if "skendel" in my_string:
#if my_list[::2] == ["valor1", "valor3"]:
#if "skendel" in some_list else False:
#if my_dict.get("chave", 0) == 1 else False:
#if re.match(r'\d{4}', string):
#if (x > 10 and y < 5) or (z == 3 and w != 8) or (my_list[2][1] == 'valor' and len(my_string) > 15) or (some_function(x) > 50 and (x == 5 or (y % 2 == 0 and z % 3 != 0)) or (x < 10 and (my_dict.get('chave', 0) == 1 or 'skendel' in my_string))):
#if (x > 10 and y < 5) or ((z == 3 and w != 8) or (my_list[2][1] == "valor" and len(my_string) > 15)) or (some_function(x) > 50) or (x == 5 or ((y % 2 == 0) and (z % 3 != 0) and "teste" in my_dict["chave"])) or (x < 10 and (my_dict.get("chave", 0) == 1 or "skendel" in my_string)) or (my_list[0] == "inicio" and (x in [1, 2, 3])) else "Condição não satisfeita!"
#if (x > 10 and y < 5) or ((z == 3 and w != 8) or (my_list[2][1] == "valor" and len(my_string) > 15)) or (some_function(x) > 50) or (x == 5 or ((y % 2 == 0) and (z % 3 != 0) and "teste" in my_dict["chave"])) or (x < 10 and (my_dict.get("chave", 0) == 1 or "skendel" in my_string)) or (my_list[0] == "inicio" and (x in [1, 2, 3])):
#podia fazer mais, mas sinceramente fodase
##############################

print(analise(''))


