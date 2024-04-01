'''
for i in range(2015, 2023):
    f = open("phishing-%s.txt" % str(i),encoding="ISO-8859-1")
    j = 0
    fout = open("./phish/%s_%s.txt" % (str(i), str(j)), "w")
    while True:
        line = f.readline()
        if not line:
            break
        if line == "\n":
             continue
        if "From " in line:
            fout.close()
            j += 1
            fout = open("./phish/%s_%s.txt" % (str(i), str(j)), "w", encoding="utf8")
        fout.write(line)

'''
import os 
import re
import json

legal = os.listdir("./legal")
phish = os.listdir("./phish")

res = dict()

count = 0
for name in phish:
    fin = open("./phish/%s" % name)
    lines = list()
    
    html = 0
    form = 0
    href = 0
    script = 0
    kw1 = 0
    kw2 = 0
    kw3 = 0
    kw4 = 0
    kw5 = 0
    

    while True:
        
        line = fin.readline()
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
        if "From " in line:
            try:
                info = ".".join(line.split()[1].split("@")[1].split(".")[-2:])
            except:
                info = "happy"
                pass
        if "update" in line.lower():
            kw1 += 1
        if "confirm" in line.lower():
            kw1 += 1
        if "user" in line.lower():
            kw2 += 1
        if "customer" in line.lower():
            kw2 += 1
        if "client" in line.lower():
            kw2 += 1
        if "suspend" in line.lower():
            kw3 += 1
        if "restrict" in line.lower():
            kw3 += 1
        if "hold" in line.lower():
            kw3 += 1
        if "verify" in line.lower():
            kw4 += 1
        if "account" in line.lower():
            kw4 += 1
        if "login" in line.lower():
            kw5 += 1
        if "username" in line.lower():
            kw5 += 1
        if "password" in line.lower():
            kw5 += 1
        
                
        #line = line.split("\n")
        #print(line)
        #for  i in range(len(line)):
        #    line[i] = line[i][:-1]
        
        #print(line)
        lines.append(line)             
    for i in range(len(lines)):
        if len(lines[i]) > 1:
            if lines[i][-2] == "=":
                lines[i] = lines[i][:-2]
        

        #pattern = re.compile(r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    lines = "".join(lines)
    
    print(name)
    ak = re.findall(pattern, lines)
    if len(ak) >=1:
        print(ak)
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
        feature = [html,form,href,script,kw1,kw2,kw3,kw4,kw5,num_url,num_subdomain,ip_based,relate_url,1]
    else:
        feature = [html,form,href,script,kw1,kw2,kw3,kw4,kw5,num_url,num_subdomain / num_url,ip_based,relate_url,1]
    print(feature)
    res[name] = feature

print(len(res))

with open("phish.json","w") as f:
    json.dump(res,f)