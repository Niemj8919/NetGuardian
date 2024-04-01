
import pymysql

#conn = pymysql.connect(
#    host = "127.0.0.1",
#    port = 3306,
#    database = 'optc',
#    user = 'temp_root',
#    password = 'temp'
#)
#cursor = conn.cursor()
#sql = 'create table data1(id int unsigned not null auto_increment, action varchar(20) not null, src varchar(40) not null, s_port INT not null, dst varchar(40) not null, d_port INT not null, proto INT not null, direction varchar(30) not null, size INT not null, ts varchar(100) not null, aid varchar(100) not null, primary key (id))'
#cursor.execute(sql)
import json
import time
count = 0
ids = dict()
#db = list()
fout = open("test1out.txt","w")
with open("test1.json") as f:
    while True:
        line = f.readline()
        count += 1
        if count % 100000 == 0: print(count)
        #if count == 100000: break
        if not line : break

        a = json.loads(line)
        if a['object'] == "FLOW" and a['action'] != "OPEN":
            action = a['action']
            src = a['properties']['src_ip']
            s_port = a['properties']['src_port']
            dst = a['properties']['dest_ip']
            #if src.startswith("224.") or src.startswith("225.") or dst.startswith("224.") or dst.startswith("225."): continue
            d_port = a['properties']['dest_port']
            proto = a['properties']['l4protocol']
            direction = a['properties']['direction']
            try:    size = str(a['properties']['size'])
            except: size = '0'

            ts1 = a['timestamp'].split("T")[0]
            ttemp = a['timestamp'].split("T")[1].split("-")[0].split(".")
            min = ttemp[0]
            timeA = time.strptime(ts1 + " " + min, "%Y-%m-%d %H:%M:%S")
            
            if len(ttemp) == 2: ts = time.mktime(timeA) + int(ttemp[1]) / 100
            else: ts = time.mktime(timeA)
            id = a['actorID']
            if id not in ids:
                ids[id] = dict()
                ids[id]['size'] = int(size)
                ids[id]['ts'] = ts
                ids[id]['info'] = src + " " + s_port + " " + dst + " " + d_port + " " + proto
            else:
                ids[id]['size'] += int(size)
                if ts < ids[id]['ts']: ids[id]['ts'] = ts
            
            #db.append((action,src,s_port,dst,d_port,proto,direction,size,ts,id))
            #fout.write(action + " " + src + " " + s_port + " " + dst + " " + d_port + " " + proto  + " " + size + " " + ts + " " + id + "\n")
    
    #sql = "insert into data1(action, src,s_port,dst,d_port,proto,direction,size,ts,aid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    #cursor.executemany(sql, db)
    #conn.commit()
    for aid in ids:
        fout.write(aid + " " + str(ids[aid]['size']) + " " + ids[aid]['info'] + " " + str(ids[aid]['ts']))
        

        







