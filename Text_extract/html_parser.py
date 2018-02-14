from bs4 import BeautifulSoup
from pathlib import Path
import re
import pandas as pd
#list3 gets the entire text with the tables
#text 5 gets the headers
# The len of both list3 and text5 are same if not same we have a problem with the code
def parse_html():
    pathlist = Path(specify the path in the directory the html files exist).glob('**/*.htm')
    text4 = []
    text5 = []
    text6 = []
    text7 = []
    text71 = []
    text72 = []
    text8 = []
    list1 = []
    text3 = []
    table1 = []
    header1 = []
    x1 = q2 = d = c = e = g = sf = sf1 = sf2 = sf3 = sc2 = sc5 = sc1 = t = line1 = line2 = line3 = line4 = line5 = line6 = ' '
    text2 = d1 = sc9 = sc8 = a1 = a2 = a3 = a4 =a5 =a6 = a7 = a8 = b1 = b2 =b3 =b4 = l1 = l2 = l3= l4 =l5 = l6 = l7 = c1 = ' '
    flag = flag1 = flag5 = flag4 = flag2 = flag3 = False
    first = second = table_flag = False
    text9 = []
    text91 = []
    text92 = []
    text94 = []
    text1 = []
    list2 = []
    text21 = []
    list3 =[]
    list4 = []
    list5= []
    list6 = []
    list7 = []
    datasets = []
    dataset11 = []
    text93 = []
    list73 = []
    list74 = []
    list71 = []
    list72 = []
    list73 = []
    j7 = j = k = p1 = j1 = k = k3  = k2 = q4 = q5  = j2 = counter1 = counter2 = min1 = 0
    str1 = ' '
    x12 = 0
    depth3 = [] 
    depth2 = []
    k7 = k8 = 0
    index_d = {} #to index the pictures if present
    x2 = ' '
    flag7 = flag8 = flag9 = flag10 =  False
    pd.set_option('display.max_colwidth', -1)
    for path in pathlist: #searching in each html file
        k = k +1
        path_in_str = str(path)
        f = open(path_in_str, 'r',encoding = "ISO-8859-1")
        soup = BeautifulSoup(f.read(),"html.parser")
        [title.decompose() for title in soup.find_all("title")]
        [script1.decompose() for script1 in soup.find_all("script")]
        for h in soup.find_all("h1"):
            d = h.get_text()
            text4.append(d)
            flag1 = True
        for img in soup.find_all("img"):
            # text62.append(k)
            text92.append(img['src'])
        if soup.find_all("table"):
            flag4 = True
        i6 = i7 = i8 = i9 = 0
        z12 = ' '
        if flag4: #to get the tables in proper format
            with open(path_in_str,'r',encoding = "utf-8",errors='ignore') as q:
                i3 = 0
                soup1 = BeautifulSoup(q,"html.parser")
                tables1 = pd.read_html(path_in_str)
                tables = soup1.find_all("table")
                for table in tables:
                    if table.findParent("table"):
                        i3 = i3 + 1
                for tr in soup.find_all('tr'):
                    soup14 = BeautifulSoup(str(tr), "html.parser")
                    i6 = i6 + 1
                    for table2 in soup14.find_all("table"):
                        list71.append(i6)
                        i8 = i6
                        for tr1 in table2.find_all('tr'):
                            i7 = i7 + 1
                        list72.append(i7)
                if len(list71) > 1:
                    for i in range(len(list71)):
                        x22 = list71[i] + list72[i]
                        list73 = list73 + (list(range(list71[i], x22)))
                if i3 == 0:
                    y1 = ' '
                    for i in range(len(tables1)):
                        if len(tables1[i].columns) == 2:
                            for j in range(len(tables1[i])):
                                text3.append(str(tables1[i][0][j]) + '\t' + str(tables1[i][1][j]))
                        if len(tables1[i].columns) == 3:
                            for j in range(len(tables1[i])):
                                text3.append(str(tables1[i][0][j]) + '\t' + str(tables1[i][1][j]) + '\t' + str(tables1[i][2][j]))
                        if len(tables1[i].columns) == 4:
                            for j in range(len(tables1[i])):
                                text3.append(str(tables1[i][0][j]) + '\t' + str(tables1[i][1][j]) + '\t' + str(tables1[i][2][j]) + '\t' + str(tables1[i][2][j]))
                        for i1 in range(len(text3)):
                            y1 = y1 + text3[i1] + '\n'
                        if "<!-- kadovFilePopupInit" in str(y1):
                            y1 = re.sub("<!-- kadovFilePopupInit\(\'[a-zA-Z][0-9]+\'\); //-->", "", str(y1))
                        y1 = re.sub("\s\s+", " ", y1)
                        y1 =y1.strip()
                        list7.append(y1)
                        text2 = text2+ y1
                        text21.append(path_in_str)
                        text1.append(len(tables1) - i3)
                        y1 = ' '
                        del text3[:]
                if i3 != 0:
                    y1 = ' '
                    k1 = i3 - 1
                    for i in range(len(tables1)):
                        if i == k1:
                            for i1 in range(len(tables1[k1][1])):
                                if len(list71) == 1 and len(list72) == 1:
                                    if i1 not in range(list71[0], list71[0] + list72[0]):
                                        text3.append(str(tables1[k1][0][i1]) + '\t' + str(tables1[k1][1][i1]))
                            for i1 in range(len(text3)):
                                y1 = y1 + str(text3[i1]) + '\n'
                            if "<!-- kadovFilePopupInit" in str(y1):
                                y1 = re.sub("<!-- kadovFilePopupInit\(\'[a-zA-Z][0-9]+\'\); //-->", "", str(y1))
                            y1 = re.sub("\s\s+", " ", y1)
                            y1 = y1.strip()
                            list7.append(y1)
                            text2 = text2 + y1
                            text21.append(path_in_str)
                            text1.append(len(tables1) - i3)
                            y1 = ' '
                            del text3[:]
                        else:
                            if i != i3:
                                for i1 in range(len(tables1[k1-1][1])):
                                    if i1 not in list73:
                                        text3.append(str(tables1[k1-1][0][i1]) + '\t' + str(tables1[k1-1][1][i1]))
                                for i1 in range(len(text3)):
                                    y1 = y1 + str(text3[i1]) + '\n'
                                if "<!-- kadovFilePopupInit" in str(y1):
                                    y1 = re.sub("<!-- kadovFilePopupInit\(\'[a-zA-Z][0-9]+\'\); //-->", "", str(y1))
                                y1 = re.sub("\s\s+", " ", y1)
                                y1 = y1.strip()
                                list7.append(y1)
                                text2 = text2 + y1
                                text21.append(path_in_str)
                                text1.append(len(tables1) - i3)
                                y1 = ' '
                                del text3[:]
        i6 = i7 = i8 = i9 = 0
        flag4 = False
        if flag1: #mapping the text at the appropriate headers and appending text at the appropriate places
            with open(path_in_str,'r+',encoding = "ISO-8859-1") as q1:
                l1 = (q1.readlines())
                k8  = k8+1
                for m in range(0,len(l1)):
                    l2 = l1[m]
                    if "h3" in l2 :
                        l7 = BeautifulSoup(l1[m],"html.parser")
                        text8.append(m)
                    if "h4" in l2:
                        l7 = BeautifulSoup(l1[m], "html.parser")
                        text8.append(m)
            sorted(text8)
            with open(path_in_str,'r+',encoding="ISO-8859-1") as q2:
                l3 = q2.readlines()
                k5 = len(text8)+len(text9)
                x14 = ' '
                if path_in_str in text21:
                    q5 = text1[text21.index(path_in_str)]
                if q5 == 1:
                    table_flag =True
                if q5 > 1:
                    j7 = text21.index(path_in_str)
                for m2 in range(0,len(l3)):
                    l2 = l3[m2]
                    if "h1" in l2:
                        l7 = BeautifulSoup(l3[m2],"html.parser")
                        x14 = l7.get_text().replace('\n','')
                if len(text8) == 0:
                    flag7 = True
                    counter2 = counter2 + 1
                    text72.append(counter2)
                    list3.append(x14 + '\n')
                    text5.append(x14)
                    soup11 = BeautifulSoup(q2, "html.parser")
                    [td.decompose() for td in soup11.find_all('tr')]
                    for p in soup11.find_all("p"):
                        x17 = ''
                        x17 = str(p.get_text()).replace('\n','')
                        x17 = re.sub("\s\s+" , " ", x1)
                        x17 = x17.strip()
                        if x17 not in text2:
                            a = len(list3)
                            list3[a - 1] = list3[a - 1] + x17
                            l5 = l5 + str(p.get_text()).replace('\n ', ' ')
                    for h2 in soup11.find_all("table"):
                        if path_in_str in text21:
                            table1.append(path_in_str)
                            x12 = x12 + 1
                            list74.append(x12)
                            k9 = len(list3)
                            if table_flag:
                                list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[text21.index(path_in_str)])
                            else:
                                list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[j7])
                                j7 = j7+1
                            table_flag = False
                        break
                    for img in soup11.find_all("img"):
                        text93.append(img['src'])
                    index_d[len(list3)-1] = str(text93)
                    x2 = x1 = ''
                    del text93[:]
                line5 = l5
                l5 = l4 = ' '
                if len(text8) > 0:
                    flag8 = True
                    for i1 in range(len(text8)):
                        if i1 == len(text8)-1 and len(text8) == 1:
                            initial = text8[i1] - 1
                            next1 = len(l3)
                            for m2 in range(0, initial):
                                l2 = str(l3[m2])
                                if '<p>&nbsp;</p>' in l2:
                                    l2 = str(l3[m2]).replace('<p>&nbsp;</p>', '<p>@11111</p>')
                                x2 = str(x2) + l2
                            if '<li class=kadov-p><p>' in x2:
                                x2 = x2.replace('<li class=kadov-p><p>', '<li class=kadov-p><p>@123444')
                            x2 = x2.encode('utf-8')
                            soup112 = BeautifulSoup(x2, "html.parser")
                            if soup112.find_all('table') or soup112.find_all('p'):
                                list3.append(x14)
                                text5.append(x14)
                            [td.decompose() for td in soup112.find_all('tr')]
                            for img in soup112.find_all('img'):
                                text6.append(k)
                                text93.append(img['src'])
                            index_d[len(list3) - 1] = str(text93)
                            del text93[:]
                            for p in soup112.find_all("p"):
                                x17 = ''
                                x17 = str(p.get_text()).replace('\n', '').replace('Â', '')
                                x17 = re.sub("\s\s+", " ", x17)
                                x17 = x17.strip()
                                if x17 not in text2:
                                    a = len(list3)
                                    list3[a - 1] = list3[a - 1] + x17
                                    l5 = l5 + str(p.get_text()).replace('\n ', ' ')
                            for h2 in soup112.find_all("table"):
                                if path_in_str in text21:
                                    table1.append(path_in_str)
                                    x12 = x12 + 1
                                    list74.append(x12)
                                    k9 = len(list3)
                                    if table_flag:
                                        list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[text21.index(path_in_str)])
                                    else:
                                        list3[k9 - 1] = list3[k9 - 1] + str(list7[j7])
                                        j7 = j7 + 1
                                    table_flag = False
                                break
                            x2 =l2 = ' '
                            for m2 in range(initial, next1):
                                l2 = str(l3[m2])
                                if '<p>&nbsp;</p>' in l2:
                                    l2 = str(l3[m2]).replace('<p>&nbsp;</p>', '<p>@11111</p>')
                                x2 = str(x2) + l2
                            if '<li class=kadov-p><p>' in x2:
                                x2 = x2.replace('<li class=kadov-p><p>', '<li class=kadov-p><p>@123444')
                            x2 = x2.encode('utf-8')
                            soup114 = BeautifulSoup(x2, "html.parser")
                            [td.decompose() for td in soup114.find_all('tr')]
                            l5 = l4 + '\n'
                            for h3 in soup114.find_all("h3"):
                                l4 = l4 + str(h3.get_text()).replace('\n ', '')
                                list3.append(str(h3.get_text()).replace('\n', '') + '\n')
                                text5.append(x14 + ' - ' + (str(h3.get_text()).replace('\n', '') + '\n'))
                            for h4 in soup114.find_all("h4"):
                                list3.append(str(h4.get_text()).replace('\n', '') + '\n')
                                text5.append(x14 + ' - ' + str(h4.get_text()).replace('\n', '') + '\n')
                            for p in soup114.find_all("p"):
                                x17 = ''
                                x17 = str(p.get_text()).replace('\n', '').replace('Â', '')
                                x17 = re.sub("\s\s+", " ", x17)
                                x17 = x17.strip()
                                if x17 not in text2:
                                    a = len(list3)
                                    list3[a - 1] = list3[a - 1] + x17
                                    l5 = l5 + str(p.get_text()).replace('\n ', ' ')
                            for h2 in soup114.find_all("table"):
                                if path_in_str in text21:
                                    table1.append(path_in_str)
                                    x12 = x12 + 1
                                    list74.append(x12)
                                    k9 = len(list3)
                                    if table_flag:
                                        list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[text21.index(path_in_str)])
                                    else:
                                        list3[k9 - 1] = list3[k9 - 1] +'\n' + str(list7[j7])
                                        j7 = j7 + 1
                                    table_flag = False
                                break
                            for img in soup114.find_all('img'):
                                text6.append(k)
                                text93.append(img['src'])
                            index_d[len(list3) - 1] = str(text93)
                            del text93[:]
                        x2 = x1 = ''
                        line6 = line6 + l5
                        l5 = l4 = ' '

                        if i1 == len(text8)-1 and len(text8) > 1:
                            j1 = k
                            initial = text8[i1]-1
                            next1 = len(l3)
                            text91.append(str(text8[i1]-1))
                            for m2 in range(initial, next1):
                                l2 = str(l3[m2])
                                if '<p>&nbsp;</p>' in l2:
                                    l2 = str(l3[m2]).replace('<p>&nbsp;</p>','<p>@11111</p>')
                                x2 = str(x2) + l2
                            if '<li class=kadov-p><p>' in x2:
                                x2 = x2.replace('<li class=kadov-p><p>', '<li class=kadov-p><p>@123444')
                            x2 = x2.encode('utf-8')
                            soup11 = BeautifulSoup(x2, "html.parser")
                            l5 = l4 + '\n'
                            [td.decompose() for td in soup11.find_all('tr')]
                            for h3 in soup11.find_all("h3"):
                                l4 = l4 + str(h3.get_text()).replace('\n ', '')
                                list3.append(str(h3.get_text()).replace('\n', '') + '\n')
                                text5.append(x14 + ' - ' + (str(h3.get_text()).replace('\n', '') + '\n'))
                            for h4 in soup11.find_all("h4"):
                                list3.append(str(h4.get_text()).replace('\n', '') + '\n')
                                text5.append(x14 + ' - ' + str(h4.get_text()).replace('\n', '') + '\n')
                            for p in soup11.find_all("p"):
                                x17 = ''
                                x17 = str(p.get_text()).replace('\n','').replace('Â','')
                                x17 = re.sub("\s\s+" , " ", x17)
                                x17 = x17.strip()
                                if x17 not in text2:
                                    a = len(list3)
                                    list3[a-1] = list3[a-1] + x17
                                    l5 = l5 + str(p.get_text()).replace('\n ',' ')
                            for h2 in soup11.find_all("table"):
                                if path_in_str in text21:
                                    table1.append(path_in_str)
                                    x12 = x12 + 1
                                    list74.append(x12)
                                    k9 = len(list3)
                                    if table_flag:
                                        list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[text21.index(path_in_str)])
                                    else:
                                        list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[j7])
                                        j7 = j7 + 1
                                    table_flag = False
                                break
                            for img in soup11.find_all('img'):
                                text6.append(k)
                                text93.append(img['src'])
                            index_d[len(list3)-1] = str(text93)
                            del text93[:]
                        x2 = x1 = ''
                        line6 = line6 + l5
                        l5 = l4 = ' '
                        if i1 < len(text8) - 1:
                            flag9 =True
                            counter2 = counter2 + 1
                            text72.append(counter2)
                            initial = text8[i1] - 1
                            next1 = text8[i1 + 1] - 1
                            text91.append(str(text8[i1]))
                            for m1 in range(initial,next1):
                                l2 = str(l3[m1])
                                if '<p>&nbsp;</p>' or '<p class="hcp3">&nbsp;</p>' in l2:
                                    l2 = str(l3[m1]).replace('&nbsp;</p>','@11111</p>')
                                x1 = str(x1) + l2
                            if '<li class=kadov-p><p>' in x1:
                                x1 = x1.replace('<li class=kadov-p><p>', '<li class=kadov-p><p>@123444')
                            x1 = x1.encode('utf-8')
                            soup12 = BeautifulSoup(x1,"html.parser")
                            [td.decompose() for td in soup12.find_all('tr')]
                            c1 = l4 + '\n'
                            for h3 in soup12.find_all("h3"):
                                l4 = l4 + str(h3.get_text()).replace('\n ', '')
                                list3.append(str(h3.get_text()).replace('\n','')+'\n')
                                text5.append(x14 + ' - ' + str(h3.get_text()).replace('\n','')+'\n')
                            for h4 in soup12.find_all("h4"):
                                list3.append(str(h4.get_text()).replace('\n','')+'\n')
                                text5.append(x14 + ' - ' + str(h4.get_text()).replace('\n','')+'\n')
                            for img in soup12.find_all("img"):
                                text6.append(k)
                                text93.append(img['src'])
                            for p in soup12.find_all("p"):
                                x17 = ''
                                x17 = str(p.get_text()).replace('\n','').replace('Â','')
                                x17 = re.sub("\s\s+" , " ", x17)
                                x17 = x17.strip()
                                if x17.strip() not in text2:
                                    a = len(list3)
                                    list3[a-1] = list3[a-1] + x17
                                    c1 = c1 + str(p.get_text()).replace('\n ','')
                            for h2 in soup12.find_all("table"):
                                if path_in_str in text21:
                                    table1.append(path_in_str)
                                    x12 = x12 + 1
                                    list74.append(x12)
                                    k9 = len(list3)
                                    if table_flag:
                                        list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[text21.index(path_in_str)])
                                    else:
                                        list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[j7])
                                        j7 = j7 + 1
                                    table_flag = False
                                break
                            index_d[len(list3) - 1] = str(text93)
                            x2 = x1 = l2 = ''
                            line3 = line3 + c1
                            del text93[:]
                        list1.append(c1)
                        list2.append(path_in_str)
                        c1 = l4 = ' '
                line5 = line4 = ' '
                if len((line6+line3).split()) == 0:
                    with open(path_in_str, 'r', encoding="ISO-8859-1") as q:
                        soup1 = BeautifulSoup(q, "html.parser")
                        [td.decompose() for td in soup1.find_all('tr')]
                        if path_in_str in text21:
                            x12 = x12+1
                            table1.append(path_in_str)
                            list74.append(x12)
                            counter2 = counter2 + 1
                            text72.append(counter2)
                            k9 = len(list3)
                            if table_flag:
                                list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[text21.index(path_in_str)])
                            else:
                                list3[k9 - 1] = list3[k9 - 1] + '\n' + str(list7[j7])
                                j7 = j7 + 1
                        for tag in soup1.find_all('img'):
                            text6.append(k)
                            text93.append(tag['src'])
                        index_d[len(list3) - 1] = str(text93)
                        del text7[:]
                        del text93[:]
                        table_flag =False
                if (not(flag7) and not(flag8) and not(flag9)) is True:
                    soup13 = BeautifulSoup(q2,"html.parser")
                    [td.decompose() for td in soup13.find_all('tr')]
                    if path_in_str in text21:
                        x12 = x12+1
                        table1.append(path_in_str)
                        list74.append(x12)
                        x10 = text21.index(path_in_str)
                        if table_flag:
                            list3.append(str(list7[text21.index(path_in_str)]))
                        else:
                            list3.append(str(list7[j7]))
                            j7 = j7 + 1
                        list3.append(list7[x10])
                        for tag1 in soup13.find_all('img'):
                            text6.append(k)
                            text93.append(tag1['src'])
                        index_d[len(list3) - 1] = str(text93)
                        del text93[:]
                        table_flag = False
                flag7 = flag8 = flag9 = False
                line6 = line3 = ' '
        flag1 = False
        j7 = q5 = 0
        del text8[:]
        del dataset11[:]
        del list71[:]
        del list72[:]
        del list73[:]
        del datasets[:]
    sum1 = 0
    for i in range(len(list3)):
        if "<!--kadovFilePopupInit" in str(list3[i]):
            list3[i] = re.sub("<!--kadovFilePopupInit\(\'[a-zA-Z][0-9]+\'\);//-->", "", str(list3[i]))
        if '@11111' in str(text5[i]):
            text5[i] = str(text5[i]).replace('@11111', ' ')
        if '@11111' in str(list3[i]):
            list3[i] = str(list3[i]).replace('@11111', '\n')
        if '@123444' in str(list3[i]):
            list3[i] = str(list3[i]).replace('@123444','\n')
        list3[i] = str(list3[i]).replace('Â','')
        text5[i] = str(text5[i]).replace('Â','')
        print(i)
        print(text5[i])
        print(list3[i])
    for i in range(len(index_d)):
        index_d[i] = (str(index_d[i]).replace('%20',' '))
    return list3,text5,index_d
if __name__ == '__main__':
    parse_html()
