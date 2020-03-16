import time

def swapper(src):
    data = src.split()
    # print(data)
    omits = []
    limit = len(data)
    i = 0
    while i < limit:

        if data[i] in symbols:
            omits.append([data[i], i])
            # print("\n\n"+data[i]+"\n\n")
            del data[i]
            limit -=1
        # print(f"data[i] = {data[i]}")
        if i%2!=0:
            firlet = data[i - 1][0]
            seclet = data[i][0]

            if data[i][0].isupper():
                firlet = firlet.upper()
            elif data[i][0].islower():
                firlet = firlet.lower()
            if data[i - 1][0].isupper():
                seclet = seclet.upper()
            elif data[i - 1][0].islower():
                seclet = seclet.lower()
            newfir = data[i-1][1:]
            newsec = data[i][1:]

            data[i-1] = "".join([seclet, newfir])
            data[i] = "".join([firlet, newsec])
        i += 1
    # print(omits)

    for k in range(len(omits)):
        data.insert(omits[k][1], omits[k][0])

    ans = " ".join(data)
    return ans

def fileswap(srcfile):
    file = open(srcfile, "r")
    fdata_global = file.readlines()
    file.close
    for i in range(len(fdata_global)):
        fdata_global[i] = swapper(fdata_global[i])
        # print(fdata_global[i])
    answer = "\n".join(fdata_global)
    # print(answer)
    res = open("swap_result.txt", "a+")

    res.write(str("\n\n"+time.ctime())+"\nfilename = "+srcfile+"\n\n")
    res.write(answer)
    res.close

def ui():
    global flag
    source = input('Введите текст, полный путь к файлу, либо "exit" для выхода\n')
    if source == "exit":
        flag = False
        return
    if source[1:3] == ":/" and source.count("/")>1:
        print('Файл с именем "swap_result" сохранён в папку с исходным файлом.')
        fileswap(source)
    else:
        print("Результат:")
        print(swapper(source))

def main():
    while flag:
        ui()
    else:
        print("\nСпасибо за использование!")
        time.sleep(1)

flag = True
symbols = "-_+=\|/?<>.,!@#$%^&*()~`:;{}[]"
main()
