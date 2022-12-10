import PyPDF2
roll = input('Enter Your Roll: ')
# with open('1st_Sem_2022_Regulation.pdf','rb') as file:
#     data = PyPDF2.PdfFileReader(file)
#     with open('data.txt','w') as data_file:
#         for i in range(data.numPages):
#             data_file.write((data.getPage(i).extract_text()))
with open('data.txt','r') as data_file:
        result = data_file.read()
        find_roll = result.find(roll)
        k = find_roll
        res = ''
        flag = False
        for i in range(find_roll, len(result)):
            if result[i] == '{':
                res += result[k]
                k+=1
                flag = True
                if result[k] =='}':
                    res+='}'
                    break
            elif result[i] =='(' and flag == False:
                res+=result[k]
                k+=1
                if result[k] == ')':
                    res += ')'
                    break
        print(res)