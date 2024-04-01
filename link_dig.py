import sys
import json
import os
import joblib
import re
from sklearn import svm
import yaml
import time
import psutil
import threading
abcde = time.time()
start = int(sys.argv[1])

length = int(sys.argv[2])

hlen = int(sys.argv[3])

inlist = os.listdir("./optc25")
#inlist = []


thread_flag = False
cout = open("monidetect%s.txt" % sys.argv[1], "w")
def gather(pid):
    global thread_flag
    p = psutil.Process(pid)

    while True:
        cpu_percent = p.cpu_percent(interval=5)
        
        #cpu_percent2 = psutil.cpu_percent(interval=5)  # 采样时间5秒 第二种方法
        mem_info = psutil.Process().memory_info()
        mem_percent = mem_info.rss
        
            # 打印数据
        print(
            f"CPU使用率 {cpu_percent}% 内存使用 {mem_percent} Bytes")
        
        cout.write(
            f"CPU使用率 {cpu_percent}% 内存使用 {mem_percent} Bytes" + "\n")
        
        if thread_flag: break
        import time 
        time.sleep(1)

cpu_process = psutil.Process()
pid = cpu_process.pid
print(pid)
Threader = threading.Thread(target=gather, args = (pid,))
Threader.start()


def tdfs(node, t, start, reachable):
    fin = open("./0925/%s.json" % (node))

    data = json.load(fin)
    fin.close()

    for v in matrix[node]:
        if v == 'flag':
            continue
        if v not in matrix:
            continue
        if matrix[v]['flag'] == 1 or v == start:
            continue
        #if v == "142.20.57.147":print("ok")
        d_flag = False
        #print(matrix[v])
        for i in range(len(data[v])):
            if data[v][i] > t:
                d_flag = True
                t_next = data[v][i]
                matrix[v]['flag'] = 1
                break

        if not d_flag:
            return
        else: 
            if v in reachable:
                reachable[start].add(v)
            #print(v)
            tdfs(v, t_next, start, reachable)
'''
with open("dfs.json") as f:
        matrix = json.load(f)
reachable = dict()
reachable["142.20.56.202"] = set()
reachable["142.20.57.147"] = set()
tdfs("142.20.56.202", 0, "142.20.56.202", reachable)
print(reachable)
exit()
'''

def inninn(node):
    if node.startswith("142.20"):
                return 1
    elif node.startswith("192.168"):
                return 1
    elif node.startswith("10."):
                return 1 
    elif node.startswith("172"):
        if int(node.split(".")[1]) >=16 and int(node.split(".")[1]) <=31:
                    return 1
        else: return 0
    else:
                return 0



# 需要用到的外部模型、文件

clf = joblib.load("./phish_model.pkl")

social_list = list()
with open("Socials.yml") as f:
    data = f.read()
    params = yaml.load(data, Loader=yaml.SafeLoader)
    for key in params:
        for domain in params[key]:
            social_list.append(domain)
print(len(social_list))

with open("netdisk_ips.txt") as f:
    netdisk_list = list()
    while True:
        line = f.readline().strip("\n")
        if not line:
            break
        netdisk_list.append(line)
print(netdisk_list)

with open ("./C2C/c2_feature_06%s_2.json" % start) as f:
    c2_data = json.load(f)
    print(len(c2_data))

with open("./yixin/nxdomain_09%s.json" % start) as f:
    nxdomain = json.load(f)
    print(len(nxdomain))

with open("./yixin/mining_09%s.json" % start) as f:
    mining = json.load(f)
    print(len(mining))

with open("./phd/phd09%s.json" % start) as f:
    phd = json.load(f)
    print(len(phd))

with open("./data_ex/data_exfil_09%s.json" % start) as f:
    exfil = json.load(f)
    print(len(exfil))

with open("./rdp/rdp09%s.json" % start) as f:
    rdp = json.load(f)
    print(len(rdp))

with open("./bothunter/09%s_0.log" % start) as f:
    scan = json.load(f)
    print(len(scan))

exfil = sorted(exfil.items(), key=lambda x: x[1])[-10:]

print(exfil)
#需要用到的所有历史信息

#abc = input()

files = os.listdir("./smtp")


his_list = list()
for i in range(start - hlen, start):
    with open("./historyc/history09%s.json" % str(i)) as f:
        history = json.load(f)
        print("load %s ok" % str(i))
        his_list.append(history)

stat = dict()
for date in his_list:
    print("ok")
    for ip in date:
        if ip not in stat:
            stat[ip] = dict()
            stat[ip]['traffic'] = list()
            stat[ip]['domain'] = list()
            stat[ip]['connection'] = list()
            stat[ip]['flag'] = 0
            stat[ip]['appear'] = 0
        flag = 0
        if date[ip]['connection'] == 0: pass
        elif date[ip]['shabi'] / date[ip]['connection'] > 0.5 or date[ip]['single'] / date[ip]['connection'] > 0.9:
            if date[ip]['domain'] < 10:
                flag = 1
        if stat[ip]['flag'] == 1: continue
        else: stat[ip]['flag'] = flag

        stat[ip]['traffic'].append(date[ip]['traffic'])
        stat[ip]['domain'].append(date[ip]['domain'])
        stat[ip]['connection'].append(date[ip]['connection'])
        stat[ip]['appear'] += 1
        
with open("hishaha.json","w") as f:
    json.dump(stat,f)



# 钓鱼邮件检测

def phish_detect(fname, clf):
    fin = open(fname)
    #print(fname)
    html = 0
    form = 0
    href = 0
    script = 0
    kw1 = 0
    kw2 = 0
    kw3 = 0
    kw4 = 0
    kw5 = 0

    lines = list()
    while True:
        try:
            line = fin.readline()
        except:
            return [0]
        if not line:
            break
        if "<HTML>" in line:
            html = 1
        if "<form" in line:
            form = 1
        if " href=" in line:
            href += 1
        if "<script" in line:
            script = 1
        if "升级" in line.lower():
            kw1 += 1
        if "确认" in line.lower():
            kw1 += 1
        if "用户" in line.lower():
            kw2 += 1
        if "顾客" in line.lower():
            kw2 += 1
        if "客户" in line.lower():
            kw2 += 1
        if "推迟" in line.lower():
            kw3 += 1
        if "限制" in line.lower():
            kw3 += 1
        if "hold" in line.lower():
            kw3 += 1
        if "验证" in line.lower():
            kw4 += 1
        if "账户" in line.lower():
            kw4 += 1
        if "登录" in line.lower():
            kw5 += 1
        if "用户名" in line.lower():
            kw5 += 1
        if "密码" in line.lower():
            kw5 += 1

        lines.append(line)             
    for i in range(len(lines)):
        if len(lines[i]) > 1:
            if lines[i][-2] == "=":
                lines[i] = lines[i][:-2]
        

        #pattern = re.compile(r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    lines = "".join(lines)
    
    ak = re.findall(pattern, lines)
    if len(ak) >=1:
        pass
        #print(ak)
        #print(lines)
        #print(name)
    #ak = ['https://wetransfer.com/?utm_campaign=3DWT_email_tracking&amp;utm_content=3Dgeneral&amp;utm_medium=3Dlogo&amp;utm_source=3Dnotify_recipient_email', 'https://www.google.com/url?q=3Dhttps://wetransfer.com/?utm_campaign%3DWT_email_tracking%26utm_content%3Dgeneral%26utm_medium%3Dlogo%26utm_source%3Dnotify_recipient_email&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw3qkIA-Bgc7O_r5-b_ekAIy', 'https://link.gmgb4.net/x/d?c=3D27562421&amp;l=3D5814f1de-f7e5-438c-b080-5fa1c1c5ce86&amp;r=3D90d60fd3-10cf-4a10-9022-00fc37f5e200', 'https://www.google.com/url?q=3Dhttps://wetransfer.com/downloads/2ddd705c3f9194e81aad04deb30acee820220818123211/d4c5b6a979dc7e842a4fffbb31f076cf20220818123235/46fe24?utm_campaign%3DWT_email_tracking%26utm_content%3Dgeneral%26utm_medium%3Ddownload_button%26utm_source%3Dnotify_recipient_email&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw2eVTZPLSUVWUuLm0ofFhxI', 'https://link.gmgb4.net/x/d?c=3D27562421&amp;l=3D5814f1de-f7e5-438c-b080-5fa1c1c5ce86&amp;r=3D90d60fd3-10cf-4a10-9022-00fc37f5e200', 'https://www.google.com/url?q=3Dhttps://wetransfer.com/downloads/2ddd705c3f9194e81aad04deb30acee820220818123211/d4c5b6a979dc7e842a4fffbb31f076cf20220818123235/46fe24&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw18NRerCecMJSBszbQgsKlh', 'https://<span', 'https://wetransfer.zendesk.com/hc/en-us/articles/204909429?utm_campaign=3DWT_email_tracking&amp;utm_source=3Dnotify_recipient_email&amp;utm_medium=3DAdd+Us+To+Your+Contacts+Link&amp;utm_content=3Dgeneral', 'https://www.google.com/url?q=3Dhttps://wetransfer.zendesk.com/hc/en-us/articles/204909429?utm_campaign%3DWT_email_tracking%26utm_source%3Dnotify_recipient_email%26utm_medium%3DAdd%2BUs%2BTo%2BYour%2BContacts%2BLink%26utm_content%3Dgeneral&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw1LchyioAN09a-ojAAgcv5c', 'https://wetransfer.com/about?utm_campaign=3DWT_email_tracking&amp;utm_content=3Dgeneral&amp;utm_medium=3Dabout_link&amp;utm_source=3Dnotify_recipient_email', 'https://www.google.com/url?q=3Dhttps://wetransfer.com/about?utm_campaign%3DWT_email_tracking%26utm_content%3Dgeneral%26utm_medium%3Dabout_link%26utm_source%3Dnotify_recipient_email&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw2iw3YmQLffytG_616tbaFu', 'https://wetransfer.zendesk.com/hc/en-us?utm_campaign=3DWT_email_tracking&amp;utm_source=3Dnotify_recipient_email&amp;utm_medium=3DFooter+Help+Link&amp;utm_content=3Dgeneral', 'https://www.google.com/url?q=3Dhttps://wetransfer.zendesk.com/hc/en-us?utm_campaign%3DWT_email_tracking%26utm_source%3Dnotify_recipient_email%26utm_medium%3DFooter%2BHelp%2BLink%26utm_content%3Dgeneral&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw05sR2S7z3LLNCS9PlhMHhK', 'https://wetransfer.com/legal/terms?utm_campaign=3DWT_email_tracking&amp;utm_content=3Dgeneral&amp;utm_medium=3Dlegal_link&amp;utm_source=3Dnotify_recipient_email', 'https://www.google.com/url?q=3Dhttps://wetransfer.com/legal/terms?utm_campaign%3DWT_email_tracking%26utm_content%3Dgeneral%26utm_medium%3Dlegal_link%26utm_source%3Dnotify_recipient_email&amp;source=3Dgmail&amp;ust=3D1663427697195000&amp;usg=3DAOvVaw1YhvSbw37YD4fbFmk-IwYB', 'https://wetransfer.zendesk.com/hc/en-us/requests/new?ticket_form_id=3D360000007663&amp;utm_campaign=3DWT_email_tracking&amp;utm_source=3Dnotify_recipient_email&amp;utm_medium=3DSpam+Support+Link&amp;utm_content=3Dgeneral&amp;token=3DeyJhbGciOiJub25lIn0.eyJyZXF1ZXN0X3N1YmplY3QiOiJSZXBvcnQgdGhpcyB0cmFuc2ZlciBhcyBzcGFtIiwicmVxdWVzdF9kZXNjcmlwdGlvbiI6Imh0dHBzOi8vd2V0cmFuc2Zlci5jb20vZG93bmxvYWRzLzJkZGQ3MDVjM2Y5MTk0ZTgxYWFkMDRkZWIzMGFjZWU4MjAyMjA4MTgxMjMyMTEvZDRjNWI2YTk3OWRjN2U4NDJhNGZmZmJiMzFmMDc2Y2YyMDIyM', 'https://www.google.com/url?q=3Dhttps://wetransfer.zendesk.com/hc/en-us/requests/new?ticket_form_id%3D360000007663%26utm_campaign%3DWT_email_tracking%26utm_source%3Dnotify_recipient_email%26utm_medium%3DSpam%2BSupport%2BLink%26utm_content%3Dgeneral%26token%3DeyJhbGciOiJub25lIn0.eyJyZXF1ZXN0X3N1YmplY3QiOiJSZXBvcnQgdGhpcyB0cmFuc2ZlciBhcyBzcGFtIiwicmVxdWVzdF9kZXNjcmlwdGlvbiI6Imh0dHBzOi8vd2V0cmFuc2Zlci5jb20vZG93bmxvYWRzLzJkZGQ3MDVjM2Y5MTk0ZTgxYWFkMDRkZWIzMGFjZWU4MjAyMjA4MTgxMjMyMT']
    
    
    num_url = 0
    num_subdomain = 0
    ip_based = 0
    relate_url = 0

    for url in ak:
        index = [match.start() for match in re.finditer("://", url)]
        num_url += len(index)
        for ind in index:
            try:
                sub_index = url.index("/", ind + 3)
                domain = url[ind + 3: sub_index]
                count = 0
                for letter in domain:
                    if letter == ".":
                        count += 1
                ip = re.findall('/([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))(\.([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))){3}/',domain)
                if len(ip) > 0:
                    ip_based = 1
                if info not in domain:
                    relate_url = 1
                num_subdomain += count
            except:
                pass
    if  num_url == 0:
        feature = [0,form,href,script,kw1,kw2,kw3,kw4,kw5,num_url,num_subdomain,ip_based,0]
    else:
        feature = [0,form,href,script,kw1,kw2,kw3,kw4,kw5,num_url,num_subdomain / num_url,ip_based,0]
    #print(feature)

    return clf.predict([feature])



# initial compromise检测


http = dict()
email = dict()
s1 = dict()
s2 = dict()
s3 = dict()
s3_ = dict()
s3_2 = dict()
s4 = dict()



for i in range(start, start + length):
    
    with open("./historyc/history09%s.json" % str(i)) as f:
        history = json.load(f)
    
    c = 0
    lnks = dict()
    with open("smtp0718.log") as f:
        count = 0
        while True:
            line = f.readline()
            count += 1
            if not line: break
            if count <= 8: continue
            info = line.split()
            if len(info) <= 3:
                print("oh")
                continue
            
            name = info[-2].split(",")[0]
            names = info[-2].split(",")[-1]
            #print(name)
            if "(empty)" in name: continue
            if "(empty)" in names: continue
            c += 1
            for file in files:
                #print(file)
                #for fill in name:
                #if names in file:
                #    lnk = os.popen("file -i ./smtp/%s" % file).read()
                #    if 'x-ms-shortcut' in lnk or 'application/vnd.ms-htmlhel' in lnk or 'application/x-chm' in lnk:
                #        if not inninn(info[2]): lnks[info[2]] = 1
                #        if not inninn(info[4]): lnks[info[4]] = 1
                if name in file:
                    #lnk = os.popen("file -i ./smtp/%s" % file).read()
                    # lnk和chm格式的附件及其可疑
                    
                    flag = phish_detect("./smtp/%s" % file, clf)[0]
                    if c % 100 == 0:
                        print(c)
                    if flag:
                        s1[info[4]] = 1.1
                        #lnk = os.popen("file -i ./smtp/%s" % file).read()
                        #if 'x-ms-shortcut' in lnk or 'application/vnd.ms-htmlhel' in lnk or 'application/x-chm' in lnk:
                        #   if not inninn(info[2]): lnks[info[2]] = 1
                        #   if not inninn(info[4]): lnks[info[4]] = 1
    for ip in lnks:
        if ip in s1:
            s1[ip] += 1
        else: s1[ip] = 1
    print(s1)
    
    #exit()
    
    #print(c)
    #print((s1))
    


    '''
    fin = open("./http_7_%s.log" % str(i))
    count = 0
    
    while True:
        line = fin.readline()
        count += 1
        if not line: break
        if count <= 8: continue

        info = line.split()
        if len(info) <= 3:
            print("oh")
            continue
        mime = info[-1]

        if "image" in mime and info[4] in social_list:
            if info[2] not in s2:
                s2[info[2]] = 1
            else: s2[info[2]] += 1
        
        if "image" in mime and info[4] in netdisk_list:
            if info[2] not in s2:
                s2[info[2]] = 1
            else: s2[info[2]] += 1
        

        if info[4] not in stat:
            if info[2] not in s2:
                s2[info[2]] = 1
            else: s2[info[2]] += 1

        if info[4] in stat and stat[info[4]]['flag'] == 1:
            if inninn(info[2]):
                if info[2] not in s2:
                    s2[info[2]] = 1
                else: s2[info[2]] += 1
    
        if info[2] in stat and stat[info[2]]['flag'] == 1:
            if inninn(info[4]):
                if info[4] not in s2:
                    s2[info[4]] = 1
                else: s2[info[4]] += 1
        
    s2['10.10.34.168'] = 1
    fin.close()
    
    #print(s2)
    #print(len(s2))     
    '''


    # 中间步骤检测，需要把C2模型也加上去

    
    fin = open("./2019-09-%s/conn1.log" % str(i))
    #fin = open("06%s.log" % str(i))
    count = 0
    tpo = dict()
    exo = dict()
    lmo = dict()

    while True:
        line = fin.readline()
        if not line: break
        count += 1
        if count <= 8: continue
        if count % 100000 == 0: print(count)

        #if "10.157.228.124" not in line: continue

        info = line.split()
        if len(info) <= 3:
            print("oh")
            continue

        if inninn(info[2]):
            if info[2] not in tpo:
                tpo[info[2]] = [0,0,0,0,0,0,0,0]
            if info[2] not in exo:
                exo[info[2]] = [0,0,0]
            if info[4] in stat and stat[info[4]]['flag'] == 1:
                tpo[info[2]][0] = 1
            if info[4] not in history: print("haha")
            elif history[info[4]]['connection'] == 0: pass
            elif history[info[4]]['domain'] < 5 and not inninn(info[4]) and history[info[4]]['shabi'] > 0:
                if info[9] == "-" or info[10] == '0': pass
                elif float(info[9]) / float(info[10]) > 20:
                    exo[info[2]][0] = 1
            if info[2] not in lmo:
                lmo[info[2]] = [0,0,0,0,0,0]
            if info[5] == "445":# or info[5] == "22":
                lmo[info[2]][5] += 0.05
            #if info[2] not in s3:
            #    s3[info[2]] = list()
            #s3[info[2]].append(info)
            
        if inninn(info[4]):
            if info[4] not in tpo:
                tpo[info[4]] = [0,0,0,0,0,0,0,0]
            if info[2] in stat and stat[info[2]]['flag'] == 1:
                tpo[info[4]][0] = 1

        ##########
        '''
        if info[4] in stat and stat[info[4]]['flag'] == 1:
            if inninn(info[2]):
                if info[2] not in s2:
                    s2[info[2]] = 0.5

                if info[2] not in s3:
                    s3[info[2]] = list()
                if inninn(info[2]): s3[info[2]].append(info)
    
        if info[2] in stat and stat[info[2]]['flag'] == 1:
            if inninn(info[4]):
                if info[4] not in s2:
                    s2[info[4]] = 0.5
        '''
        #########
    #if "10.157.228.124" in tpo:
    #    print("ok")
    count = 0
    for file in inlist:
        fhi = open("./optc25/%s" % file)
        print("./optc25/%s" % file)
        while True:
            line = fhi.readline()
            if not line: break
            count += 1
            info = line.split()
            if info[0] not in tpo:
                tpo[info[0]] = [0,0,0,0,0,0,0,0,0]
            if info[0] not in exo:
                exo[info[0]] = [0,0,0]
            if info[0] not in lmo:
                lmo[info[0]] = [0,0,0,0,0,0,0]
            
            if info[0] not in s3_2:
                s3_2[info[0]] = list()
            s3_2[info[0]].append([info[3],info[4]])
            if count % 100000 == 0: print(count)




    ct = 0
    for ip in tpo:
        if "10.10.254." in ip:
            continue

        for pair in c2_data:
            pair = pair.split("#####")
            if ip in pair:
                print(pair)
                tpo[ip][1] = 1
        
        if ip in nxdomain and nxdomain[ip] > 20000:
            tpo[ip][2] = 1

        if ip in mining and mining[ip] > 20:
            tpo[ip][3] = 1
        
        if "202.120." in ip: pass
        elif ip in phd:
            if phd[ip][1] > 100:
                tpo[ip][4] = 1
            if phd[ip][2] > 100:
                tpo[ip][5] = 1
            if phd[ip][3] > 100:
                ct += 1
                tpo[ip][6] = 1
   
    
    #s2['10.157.228.124'] = 3.0
    print(ct)
    #exit()
    for ip in exo:
        for ex in exfil:
            if ip in ex:
                exo[ip][1] = 1

        for pair in c2_data:
            pair = pair.split("#####")
            if ip in pair:
                print(pair)
                exo[ip][2] = 1
    
    for ip in exo:
        rank = 0.5 * exo[ip][0] + exo[ip][2] + 2 * exo[ip][1]
        
        if rank >= 1.5:
            s4[ip] = rank

    print(s2)
    print(len(s2))
    print(len(s4))


    #exit()

                #if info[4] not in s3:
                #    s3[info[4]] = list()
                #if inninn(info[4]): s3[info[4]].append(info)
        

        # 这里是为了检测数据泄露，有点简略，需要吧de-scan也加上去
    #for ip in tpo:
    #    if history[ip]['connection'] == 0: pass
        #elif 
        #if history[info[4]]['connection'] == 0: pass
        #elif history[info[4]]['domain'] < 5 and not inninn(info[4]) and history[info[4]]['shabi'] > 0:
        #    s4[info[2]] = history[info[4]]['shabi'] / history[info[4]]['domain']
        

        #if info[2] not in s2:
        #    continue

        #if info[2] not in s3: s3[info[2]] = list()
        #if inninn(info[4]): s3[info[2]].append(info)


    #print(s3)

    # 将其中有横向移动行为的分拣出来，需要把Scanhunter也加上去
    #exit()

    for ip in s3:
        traffic = 0
        dst = dict()
        for flow in s3[ip]:
            if flow[9] == "-": continue
            else:
                traffic += int(flow[9])
                traffic += int(flow[10])
            if flow[4] not in dst:
                dst[flow[4]] = [flow[5]]
            else:
                dst[flow[4]].append(flow[5])
        print(str(len(dst)) + " " + ip)
        if len(dst) >= 30:
            lmo[ip][0] = 1
    
    for ip in s3_2:
        dst = dict()
        dst['dst'] = set()
        dst['icmp'] = 0 
        dst['hihihaha'] = 0
        for flow in s3_2[ip]:
            if flow[1] == "1":
                dst['icmp'] += 1
                #dst['dst'].add(flow[2])
            if flow[0] == "445" or flow[0] == "22":
               dst['hihihaha'] += 1
        if dst['icmp'] >= 30:
            lmo[ip][4] += 1
        if dst["hihihaha"] >= 10:
            lmo[ip][5] = 1
        
        
        
    
    for ip in lmo:
        for pair in c2_data:
            pair = pair.split("#####")
            if ip in pair:
                print(pair)
                lmo[ip][1] = 1
        
        if ip in scan:
            total = scan[ip]['total']
            dst = scan[ip]['dst']
            sc2 = scan[ip]['s2']
            sc3 = scan[ip]['s3']
            ratio = sc2 / total

            if sc2 / total > 0.9 and dst >= 10:
                lmo[ip][2] = 1
            if sc3 > 0.9 and dst >= 10:
                lmo[ip][3] = 1
    
    fhh = open("./2019-09-%s/http1.log" % sys.argv[1])
    #fhh = open("http06%s.log" % sys.argv[1])
    count = 0
    while True:
        line = fhh.readline()
        if not line: break
        count += 1
        if count <= 8: continue
        info = line.split()
        if len(info) <= 3: continue
        if info[5] != "80" and 'x-possible-ps' in info[-1]:
            tpo[info[2]][7] = 1
        if  "x-dosexec" in info[-1]:
            lmo[info[2]][4] = 1
            if info[14] == "0" and int(info[15]) >= 1024*1024:
                lmo[info[2]][4] = 2

    for ip in tpo:
        rank = 2*tpo[ip][1] + 0.5*(tpo[ip][0] + tpo[ip][2] + tpo[ip][3] + tpo[ip][4] + tpo[ip][5]) + tpo[ip][6] + tpo[ip][7]

        if rank >= 1:
            s2[ip] = rank

    for ip in lmo:
        rank = 0.5*(lmo[ip][0]+lmo[ip][1]) + lmo[ip][2] + 2 * lmo[ip][3] + 2 * lmo[ip][4] + 0.5 * lmo[ip][5]

        if rank >= 1.5:
            s3_[ip] = rank
    #s3_['142.20.59.207'] = 2.0
    print(len(s1))
    print(len(s2))
    print(len(s3_))
    print(len(s4))
    s1 = dict()
    
    #again = input()

    with open("s125.json","w") as f:
        json.dump(s1,f)

    with open("s225.json","w") as f:
        json.dump(s2,f)

    with open("s325.json","w") as f:
        json.dump(s3_,f)

    with open("s425.json","w") as f:
        json.dump(s4,f)
    
    print("meimei")
    #a = input()
    import json
    #START = "101.94.251.160"

    with open("s125.json") as f:
        s1 = json.load(f)
    with open("s225.json") as f:
        s2 = json.load(f)
    with open("s325.json") as f:
        s3_ = json.load(f)
    with open("s425.json") as f:
        s4 = json.load(f)

    reachable = dict()
    for ip in s1:
        reachable[ip] = set()
    for ip in s2:
        reachable[ip] = set()
    for ip in s3_:
        reachable[ip] = set()
    for ip in s4:
        reachable[ip] = set()
    
    

    with open("tpo25.json",'w') as f:
        json.dump(tpo, f)
    
    with open("exo25.json",'w') as f:
        json.dump(exo, f)
    
    with open("lmo25.json",'w') as f:
        json.dump(lmo, f)

    #maxi=input()

    with open("dfs0925.json") as f:
        matrix = json.load(f)

    for ip in s1:
        print("s124")
        tdfs(ip, 0, ip, reachable)
        for ip in matrix:
            matrix[ip]['flag'] = 0
    for ip in s2:
        print("s224")
        tdfs(ip, 0, ip, reachable)
        for ip in matrix:
            matrix[ip]['flag'] = 0

    for ip in s3_:
        print("s324")
        print(ip)
        tdfs(ip, 0, ip, reachable)
        for ip in matrix:
            matrix[ip]['flag'] = 0
    
    #for ip in s4:
    #    count("s4")
    #    tdfs(ip, 0, ip, reachable)
    #    for ip in matrix:
    #        matrix[ip]['flag'] = 0
    for ip in reachable:
        reachable[ip] = list(reachable[ip])
    with open("finally25.json", "w") as f:
        json.dump(reachable, f)

edcba = time.time() - abcde
thread_flag = True
print(edcba)
    





        

    # S3: 对于所有在S2中的节点，判断其是否有端口扫描行为。
    # 1.统计所有边，分析是否存在横向、纵向扫描（若干ip、同一ip若干端口）
    # 2.该节点与其历史情况相比，是否这一天流量异常增多 
    # S4:主要看shabi，次要看C2。

        

        








