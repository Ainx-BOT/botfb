import os,sys,time,requests,re,random
from time import sleep
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
"""
Project : bot facebook
author : fahmiapz
dibuat pada : 16 november 2021
"""
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}*{d}]{p}"
id_react=[]
id_komen=[]
id_post=[]
id_teman=[]
id_req=[]
id_rej=[]
id_unadd=[]
id_msg=[]
mbasic="https://mbasic.facebook.com{}"
def clear():
  os.system("cls" if os.name == "nt" else "clear")
def baner():
  clear()
  print(f'''

{d}   ╔╗ ┌─┐┌┬┐ {b} ╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─
{d}   ╠╩╗│ │ │  {b} ╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐
{d}   ╚═╝└─┘ ┴  {b} ╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴{d}
\033[90m----------------------------------------------
{d}Donate   : {g}https://saweria.co/FahmiDevs
{d}Message  : {g}https://wa.me/62881024612817
{d}Restapi  : {g}https://ainxbot-id.herokuapp.com
{d}Youtube  : {g}https://youtube.com/KuhakuTermux
{d}Github   : {g}https://github.com/Ainx-BOT
{d}Facebook : {g}https://facebook.com/kang.ngeue.313
\033[90m----------------------------------------------{d}''')

def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
        os.system("python run.py")
    elif lg == "n" or lg == "N":
        sys.exit(er+"Bye Bro")
        sleep(1)
        clear()
    else:
         print(er+"Wrong Input")
         sleep(1)
         cblg()
def process():
    for i in list("\|/-•"):
        print(f"\r{pr}Process\033[90m...{d}({r}{i}{d})",end="")
        sleep(0.2)
####################Login####################
def login():
  try:
    cokie=open("cookies").read()
  except FileNotFoundError:
    cokie=input(pr+"Your Cookies : "+c)
  cokie={"cookie":cokie}
  log=ses.get(mbasic.format("/me",verify=False),cookies=cokie).text
  if "mbasic_logout_button" in log:
    if "Apa yang Anda pikirkan sekarang" in log:
      with open('cookies','w') as ck:
        ck.write(cokie["cookie"])
    else:
      try:
        ses.get(bs(mbasic.format(log,"html.parser").find('a',string='Bahasa Indonesia')["href"],cookies=cokie))
      except:
        pass
    try:
        flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies=cokie).text
        flw=bs(flw,"html.parser").find('a',string='Ikuti')['href']
        ses.get(mbasic.format(flw),cookies=cokie)
    except:
        pass
    try:
        req=ses.get("https://mbasic.facebook.com/photo.php?fbid=378286914079137&id=100056934954432&set=a.117053000202531&lul&_rdr",cookies=cokie).text
        react=bs(req,"html.parser").find("a",href=lambda x: "/reactions/picker/?" in x)["href"]
        react=ses.get(mbasic.format(react),cookies=cokie).text
        love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
        care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
        wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
        angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
        ty=[love,care,wow,angry]
        type=random.choice(ty)
        ses.get(mbasic.format(type),cookies=cokie)
    except:
        pass
    try:
       komen=ses.get("https://mbasic.facebook.com/photo.php?fbid=378286914079137&id=100056934954432&set=a.117053000202531&lul&_rdr",cookies=cokie).text
       komen=bs(komen,"html.parser").find("form",action=lambda x: "comment.php" in x)
       url_komen=komen['action']
       data=komen.find_all("input",type="hidden")
       fbdtsg=data[0]["value"]
       jazoest=data[1]["value"]
       text=["Hi i'm user tools Ainx-BOT","Hi fahmi gans tools nya keren banget!","tools ini sangat berguna!","semoga rejekinya dilancarin amin"]
       komen_random=random.choice(text)
       ses.post(mbasic.format(url_komen),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":komen_random},cookies=cokie)
    except:
       pass
    return cokie["cookie"]
  else:
     print(er+'Cookie Invalid')
     sleep(2)
     os.system("rm cookies")
     os.system('python run.py')
##################Get Name & ID info########################
def userinfo():
    req=ses.get(mbasic.format("/me"),cookies=cokies).text
    name=bs(req,"html.parser").find("title").text
    id=re.findall(r'name="target" value="(.*?)"',req)[0]
    print(f"{d}Login as : {c}{name}")
    print(f"{d}ID       :{c} {id}")
    print("\033[90m----------------------------------------------\033[00m")
###################React######################
def react_people(username):
    global id_react
    if username.isdigit():
       username="/profile.php?id="+username+"&v=timeline"
    else:
       username="/"+username+"?v=timeline"
    req=ses.get(mbasic.format(username),cookies=cokies).text
    if "Tanggapi" in req:
        react=bs(req,"html.parser").find_all("a",string="Tanggapi")
    else:
        react=bs(req,"html.parser").find_all("a",href=lambda x: "/reactions/picker/?" in x)
    for x in react:
        id_react.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_react)}",end="")
    if "Lihat Berita Lain" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Berita Lain")["href"]
        if len(id_react) > 100:
            return id_react[:100]
        else:
            react_people(next)
    return id_react
def reacthome(url):
    global id_react
    req=requests.get(url,cookies=cokies).text
    if "Tanggapi" in req:
        react=bs(req,"html.parser").find_all('a',string='Tanggapi')
    else:
        react=bs(req,"html.parser").find_all("a",href=lambda x: "/reactions/picker/?" in x)
    for x in react:
        id_react.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_react)}",end="")
    if "Lihat Berita Lain" in req:
        next=bs(req,"html.parser").find('a',string='Lihat Berita Lain')["href"]
        if len(id_react) > 100:
            return id_react[:100]
        else:
            reacthome(mbasic.format(next))
    return id_react
####################Komen#####################
def komenpeople(user):
    global id_komen
    if user.isdigit():
       user="/profile.php?id="+user+"&v=timeline"
    else:
       user="/"+user+"?v=timeline"
    req=ses.get(mbasic.format(user),cookies=cokies).text
    komen=bs(req,"html.parser").find_all("a",string="Berita Lengkap")
    for x in komen:
        id_komen.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_komen)}",end="")
    if "Lihat Berita Lain" in req:
        next=bs(req,"html.parser").find('a',string='Lihat Berita Lain')["href"]
        if len(id_komen) > 100:
            return id_komen[:100]
        else:
            komenpeople(next)
    return id_komen
def komenhome(url):
    global id_komen
    req=ses.get(url,cookies=cokies).text
    komen=bs(req,"html.parser").find_all("a",string="Berita Lengkap")
    for x in komen:
        id_komen.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_komen)}",end="")
    if "Lihat Berita Lain" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Berita Lain")["href"]
        if len(id_komen) > 100:
            return id_komen[:100]
        else:
            komenhome(mbasic.format(next))
    return id_komen
###################Post#######################
def delpost(url):
    global id_post
    req=ses.get(url,cookies=cokies).text
    dlt=bs(req,"html.parser").find_all("a",string="Lainnya")
    for x in dlt:
        id_post.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_post)}",end="")
    if "Lihat Berita Lain" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Berita Lain")["href"]
        delpost(mbasic.format(next))
    return id_post
###################Unfriend##################
def unf(url):
    global id_teman
    req=ses.get(url,cookies=cokies).text
    tmn=re.findall(r'middle"><a class=".." href="(.*?)">',req)
    for x in tmn:
        id_teman.append(x)
        print(f"\r{pr}Getting Data : {c}{len(id_teman)}",end="")
    if "Lihat Teman Lain" in req:
        next=bs(req,"html.parser").find("a",string="Lihat Teman Lain")["href"]
        unf(mbasic.format(next))
    return id_teman
##############AcceptRejectUnadd##################
def reqfriend(url):
    global id_req
    req=ses.get(url,cookies=cokies).text
    res=bs(req,"html.parser").find_all("a",string="Konfirmasi")
    for x in res:
        id_req.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_req)}",end="")
    if "Lihat selengkapnya" in req:
        next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
        reqfriend(mbasic.format(next))
    return id_req
def rejfriend(url):
    global id_rej
    req=ses.get(url,cookies=cokies).text
    res=bs(req,"html.parser").find_all("a",string="Hapus Permintaan")
    for x in res:
        id_rej.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_rej)}",end="")
    if "Lihat selengkapnya" in req:
        next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
        rejfriend(mbasic.format(next))
    return id_rej
def unadd(url):
    global id_unadd
    req=ses.get(url,cookies=cokies).text
    un=bs(req,"html.parser").find_all("a",string="Batalkan Permintaan")
    for x in un:
        id_unadd.append(x["href"])
        print(f"\r{pr}Getting Data : {c}{len(id_unadd)}",end="")
    if "Lihat selengkapnya" in req:
        next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
        unadd(mbasic.format(next))
    return id_unadd
###################DeleteMessage#####################
def delmes(url):
   global id_msg
   req=ses.get(url,cookies=cokies).text
   dlt=bs(req,"html.parser").find_all("a",href=lambda x: "/messages/read/" in x)
   for x in dlt:
       id_msg.append(x["href"])
       print(f"\r{pr}Getting Data : {c}{len(id_msg)}",end="")
   if "Lihat Pesan Sebelumnya" in req:
       next=bs(req,"html.parser").find("a",string="Lihat Pesan Sebelumnya")["href"]
       delmes(mbasic.format(next))
   return id_msg
###################FindId############################
def find(user):
    try:
        req=ses.get(mbasic.format("/search/top/?q="+user+"&_rdr"),cookies=cokies).text
        tmn=bs(req,"html.parser").find("a",href=lambda x: "/messages/thread/" in x)["href"]
        tmn=re.findall(r'/messages/thread/(.*?)/',tmn)[0]
        res=ses.get(mbasic.format("/profile.php?id="+tmn),cookies=cokies).text
        name=bs(res,"html.parser").find("title").text
        print(f"{dn} {tmn} {c}= {p}{name}")
        print(f"{er}copy the ID and please return to the menu")
        input(f"{d}[{c} Press Enter To Back {d}]")
        os.system("python run.py")
    except:
        print(f"{er}Friend Not Found")
        sleep(2)
        os.system("python run.py")
##################thread#########################
def gt(url):
    ses.get(url,cookies=cokies)
def pst(url,data):
    ses.post(url,data=data,cookies=cokies)
###################Menu########################
def menu_react():
    baner()
    userinfo()
    print(f"""
{c}01. {p}like
{c}02. {p}love
{c}03. {p}care
{c}04. {p}haha
{c}05. {p}wow
{c}06. {p}sad
{c}07. {p}angry
{c}00. {p}back
\033[90m----------------------------------------------""")
    choice=input(pr+"Select : "+c)
    if choice =="01" or choice =="1":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[:jum]:
                process()
                try:
                    like=ses.get(mbasic.format(x),cookies=cokies).text
                    like=bs(like,"html.parser").find("a",href=lambda x: "&reaction_type=1&" in x)["href"]
                    ex.submit(gt,(mbasic.format(like)))
                    done+=1
                except:
                    die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done} {p}Total failed : {c}{die}{d}")
       cblg()
    elif choice =="02" or choice =="2":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   love=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
                   ex.submit(gt,(mbasic.format(love)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice =="03" or choice =="3":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                    req=ses.get(mbasic.format(x),cookies=cokies).text
                    care=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
                    ex.submit(gt,(mbasic.format(care)))
                    done+=1
                except:
                    die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice =="04" or choice =="4":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                    req=ses.get(mbasic.format(x),cookies=cokies).text
                    haha=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=4&" in x)["href"]
                    ex.submit(gt,(mbasic.format(haha)))
                    done+=1
                except:
                    die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice =="05" or choice =="5":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   wow=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
                   ex.submit(gt,(mbasic.format(wow)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice =="06" or choice =="6":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                    req=ses.get(mbasic.format(x),cookies=cokies).text
                    sad=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=7&" in x)["href"]
                    ex.submit(gt,(mbasic.format(sad)))
                    done+=1
                except:
                    die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice =="07" or choice =="7":
       name=input(f"{pr}Username/ID : {c}")
       username=react_people(name)
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[0:jum]:
                process()
                try:
                    req=ses.get(mbasic.format(x),cookies=cokies).text
                    angry=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
                    ex.submit(gt,(mbasic.format(angry)))
                    done+=1
                except:
                    die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice =="00" or choice =="0":
       spam_react()
    else:
       print(er+"Wrong input")
       sleep(2)
       menu_react()
def react_home():
    baner()
    userinfo()
    print(f"""
{c}01. {p}like
{c}02. {p}love
{c}03. {p}care
{c}04. {p}haha
{c}05. {p}wow
{c}06. {p}sad
{c}07. {p}angry
{c}00. {p}back
\033[90m----------------------------------------------""")
    choice=input(pr+"Select : "+c)
    if choice == "01" or choice == "1":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[0:jum]:
                process()
                try:
                   like=ses.get(mbasic.format(x),cookies=cokies).text
                   like=bs(like,"html.parser").find('a',href=lambda x: '&reaction_type=1&' in x)["href"]
                   ex.submit(gt,(mbasic.format(like)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "02" or choice == "2":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:      
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   love=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
                   ex.submit(gt,(mbasic.format(love)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "03" or choice == "3":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   care=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
                   ex.submit(gt,(mbasic.format(care)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "04" or choice == "4":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   haha=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=4&" in x)["href"]
                   ex.submit(gt,(mbasic.format(haha)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "05" or choice == "5":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   wow=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
                   ex.submit(gt,(mbasic.format(wow)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "06" or choice == "6":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   sad=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=7&" in x)["href"]
                   ex.submit(gt,(mbasic.format(sad)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "07" or choice == "7":
       username=reacthome(mbasic.format("/home.php"))
       print()
       jum=input(f"{pr}React Count : {c}")
       jum=int(jum)
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                   req=ses.get(mbasic.format(x),cookies=cokies).text
                   angry=bs(req,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
                   ex.submit(gt,(mbasic.format(angry)))
                   done+=1
                except:
                   die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "00" or choice == "0":
       spam_react()
    else:
       print(f"{er}Wrong Input")
       sleep(2) 
       react_home()
def menu():
    baner()
    userinfo()
    print(f'''
{c}01. {p}spam react
{c}02. {p}spam comment
{c}03. {p}auto delete post
{c}04. {p}auto unfriend
{c}05. {p}auto accept request friend
{c}06. {p}auto reject request friend
{c}07. {p}auto unadd not unfriend
{c}08. {p}spam message
{c}09. {p}auto delete message
{c}10. {p}find friend
{c}00. {p}exit
\033[90m----------------------------------------------''')
    choice=input(pr+"Select : "+c)
    if choice == "01" or choice == "1":
       spam_react()
    elif choice == "02" or choice == "2":
       spam_comment()
    elif choice == "03" or choice == "3":
        username=delpost(mbasic.format("/me?v=timeline"))
        print()
        jum=input(f"{pr}Delete Count : {c}")
        jum=int(jum)
        die=0
        done=0
        with ThreadPoolExecutor(max_workers=30) as ex:
             for x in username[0:jum]:
                 process()
                 try:
                    dlt=ses.get(mbasic.format(x),cookies=cokies).text
                    dlt=bs(dlt,"html.parser").find("form",action=lambda x: "/nfx/basic/handle_action/?" in x)
                    url_dlt=dlt["action"]
                    data=dlt.find_all("input",type="hidden")
                    fbdtsg=data[0]["value"]
                    jazoest=data[1]["value"]
                    ex.submit(pst,(mbasic.format(url_dlt)),({"fb_dtsg":fbdtsg,"jazoest":jazoest,"action_key":"DELETE","submit":"Kirim"}))
                    done+=1
                 except:
                    die+=1
        print()
        print(f"{dn}Done.")
        print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
        cblg()
    elif choice == "04" or choice == "4":
         req=ses.get(mbasic.format("/me"),cookies=cokies).text
         tmn=bs(req,"html.parser").find('a',string='Teman')["href"]
         username=unf(mbasic.format(tmn))
         print()
         jum=input(f"{pr}Unfriend Count : {c}")
         jum=int(jum)
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:
              for x in username[0:jum]:
                  process()
                  rmv=ses.get(mbasic.format(x),cookies=cokies).text
                  nm=bs(rmv,"html.parser").find("title").text
                  try:
                     hps=bs(rmv,"html.parser").find("a",string="Batalkan pertemanan")["href"]
                     hps=ses.get(mbasic.format(hps),cookies=cokies).text
                     hps=bs(hps,"html.parser").find("form",action=lambda x: "/a/friends/remove/?" in x)
                     data=hps.find_all("input",type="hidden")
                     fbdtsg=data[0]["value"]
                     jazoest=data[1]["value"]
                     ex.submit(pst,(mbasic.format(hps["action"])),({"fb_dtsg":fbdtsg,"jazoest":jazoest,"confirm":"Konfirmasi"}))
                     print(f"\r{dn}Si {nm} success di unfriend")
                     done+=1
                  except:
                     print(f"\r{er}Si {nm} gagal di unfriend")
                     die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "05" or choice == "5":
         username=reqfriend(mbasic.format("/friends/center/requests/#friends_center_main"))
         print()
         jum=input(f"{pr}Accept Count : {c}")
         jum=int(jum)
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:
              for x in username[0:jum]:
                  process()
                  try:
                     ex.submit(gt,(mbasic.format(x)))
                     done+=1
                  except:
                     die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "06" or choice == "6":
         username=rejfriend(mbasic.format("/friends/center/requests/#friends_center_main"))
         print()
         jum=input(f"{pr}Reject Count : {c}")
         jum=int(jum)
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:       
              for x in username[0:jum]:
                  process()
                  try:
                     ex.submit(gt,(mbasic.format(x)))
                     done+=1
                  except:
                     die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "07" or choice == "7":
         username=unadd(mbasic.format("/friends/center/requests/outgoing/#friends_center_main"))
         print()
         jum=input(f"{pr}Unadd Count : {c}")
         jum=int(jum)
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:
             for x in username[0:jum]:
                 process()
                 try:
                    ex.submit(gt,(mbasic.format(x)))
                    done+=1
                 except:
                    die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "08" or choice == "8":
         name=input(f"{pr}Username/ID : {c}")
         if name.isdigit():
            name="/profile.php?id="+name
         else:
            name="/"+name
         jum=input(f"{pr}Send Count : {c}")
         jum=int(jum)
         text=input(f"{pr}Send Here : {c}")
         die=0
         done=0
         req=ses.get(mbasic.format(name),cookies=cokies).text
         snd=bs(req,"html.parser").find("a",href=lambda x: "/messages/thread/" in x)
         snd=ses.get(mbasic.format(snd["href"]),cookies=cokies).text
         krm=bs(snd,"html.parser").find("form",action=lambda x: "/messages/send/?icm=1" in x)
         data=krm.find_all("input",type="hidden")
         if not "&refid=" in krm["action"]:
            fbdtsg=data[0]["value"]
            jazoest=data[1]["value"]
            ids=data[2]["value"]
            tids=data[3]["value"]
            param={"fb_dtsg":fbdtsg,"jazoest":jazoest,"ids["+ids+"]":ids,"text_ids["+ids+"]":tids,"body":text,"Send":"Kirim"}
         else:
            fbdtsg=data[0]["value"]
            jazoest=data[1]["value"]
            tids=data[2]["value"]
            wup=data[3]["value"]
            ids=data[4]["value"]
            cv=data[7]["value"]
            cs=data[8]["value"]
            param={"fb_dtsg":fbdtsg,"jazoest":jazoest,"body":text,"send":"Kirim","tids":tids,"wwwupp":wup,"ids["+ids+"]":ids,"referrer":"","ctype":"","cver":cv,"csid":cs}
         with ThreadPoolExecutor(max_workers=30) as ex:
              for i in range(0,jum):
                  process()
                  try:
                     ex.submit(pst,(mbasic.format(krm["action"])),(param))
                     done+=1
                  except:
                     die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "09" or choice == "9":
         username=delmes(mbasic.format("/messages/"))
         print()
         jum=input(f"{pr}Delete Count : {c}")
         jum=int(jum)
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:       
              for x in username[0:jum]:
                  process()
                  try:
                      req=ses.get(mbasic.format(x),cookies=cokies).text
                      dlt=bs(req,"html.parser").find("form",action=lambda x: "/messages/action_redirect?" in x)
                      data=dlt.find_all("input",type="hidden")
                      fbdtsg=data[0]["value"]
                      jazoest=data[1]["value"]
                      last=ses.post(mbasic.format(dlt["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"delete":"Hapus"},cookies=cokies).text
                      last=bs(last,"html.parser").find("a",string="Hapus")["href"]
                      ex.submit(gt,(mbasic.format(last)))
                      done+=1
                  except:
                      die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "10":
         name=input(f"{pr}Find By Name : {c}")
         find(name)
    elif choice == "00" or choice == "0":
         sys.exit(er+"Bye bro")
         sleep(2)
         clear()
    else:
         print(er+"Wrong input")
         sleep(2)
         menu()
def spam_react():
    baner()
    userinfo()
    print(f'''
{c}01. {p}spam react in people
{c}02. {p}spam react in home
{c}00. {p}back
\033[90m----------------------------------------------''')
    choice=input(pr+"Select : "+c)
    if choice == "01" or choice == "1":
       menu_react()
    elif choice == "02" or choice == "2":
       react_home()
    elif choice == "00" or choice == "0":
        menu()
    else:
        print(er+"Wrong input")
        sleep(2)
        baner()
        spam_react()
def spam_comment():
    baner()
    userinfo()
    print(f'''
{c}01. {p}spam comment in people
{c}02. {p}spam comment in home
{c}03. {p}spam comment in post target
{c}00. {p}back''')
    choice=input(f"{pr}Select : {c}")
    if choice == "01" or choice == "1":
       name=input(f"{pr}Username/ID : {c}")
       username=komenpeople(name)
       print()
       jum=input(f"{pr}Comment Count : {c}")
       jum=int(jum)
       text=input(f"{pr}Comment Here : {c}")
       die=0
       done=0
       with ThreadPoolExecutor(max_workers=30) as ex:       
            for x in username[0:jum]:
                process()
                try:
                    komen=ses.get(mbasic.format(x),cookies=cokies).text
                    komen=bs(komen,"html.parser").find("form",action=lambda x: "comment.php" in x)
                    url_komen=komen['action']
                    data=komen.find_all("input",type="hidden")
                    fbdtsg=data[0]["value"]
                    jazoest=data[1]["value"]
                    ex.submit(pst,(mbasic.format(url_komen)),({"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":text}))
                    done+=1
                except:
                    die+=1
       print()
       print(f"{dn}Done.")
       print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
       cblg()
    elif choice == "02" or choice == "2":
         username=komenhome(mbasic.format("/home.php"))
         print()
         jum=input(f"{pr}Comment Count : {c}")
         jum=int(jum)
         text=input(f"{pr}Comment Here : {c}")
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:
              for x in username[0:jum]:
                  process()
                  try:
                     komen=ses.get(mbasic.format(x),cookies=cokies).text
                     komen=bs(komen,"html.parser").find("form",action=lambda x: "comment.php" in x)
                     url_komen=komen['action']
                     data=komen.find_all("input",type="hidden")
                     fbdtsg=data[0]["value"]
                     jazoest=data[1]["value"]
                     ex.submit(pst,(mbasic.format(url_komen)),({"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":text}))
                     done+=1
                  except:
                     die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "03" or choice == "3":
         url=input(f"{pr}PostUrl? : {c}")
         if "www" in url:
             url=url.replace("www","mbasic")
         elif "m.facebook" in url:
             url=url.replace("m.facebook","mbasic.facebook")
         else:
             print(f"{er}Invalid Url")
             sleep(1)
             spam_comment()
         jum=input(f"{pr}Comment Count : ")
         jum=int(jum)
         text=input(f"{pr}Comment Here : ")
         die=0
         done=0
         with ThreadPoolExecutor(max_workers=30) as ex:
              for i in range(0,jum):
                  process()
                  try:
                      req=ses.get(url,cookies=cokies).text
                      komen=bs(req,"html.parser").find("form",action=lambda x: "comment.php" in x)
                      url_komen=komen['action']
                      data=komen.find_all("input",type="hidden")
                      fbdtsg=data[0]["value"]
                      jazoest=data[1]["value"]
                      ex.submit(pst,(mbasic.format(url_komen)),({"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":text}))
                      done+=1
                  except:
                      die+=1
         print()
         print(f"{dn}Done.")
         print(f"{pr}Total Success : {c}{done}{p} Total Failed : {c}{die}")
         cblg()
    elif choice == "00" or choice == "0":
         menu()
    else:
         print(er+"Wrong Input")
         sleep(2)
         spam_comment()
if __name__=="__main__":
  baner()
  ses=requests.Session()
  ses.headers.update({"user-agent":"Mozilla/5.0(Linux; Android 10; Redmi 4A)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.186 Mobile Safari/537.36"})
  log=login()
  cokies={"cookie":log}
  menu()
