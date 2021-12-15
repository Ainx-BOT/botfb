import requests,re
from bs4 import BeautifulSoup as bs
id_post=[]
id_people=[]
id_group=[]
id_msg=[]
mbasic="https://mbasic.facebook.com{}"

def dump_post(ses,cokie,url,type,dari):
    if type == "react":
       req=ses.get(url,cookies=cokie).text
       if "Tanggapi" in req:
          rc=bs(req,"html.parser").find_all("a",string="Tanggapi")
       else:
          rc=bs(req,"html.parser").find_all("a",href=lambda x: "/reactions/picker/?" in x)
       for x in rc:
           id_post.append(x["href"])
       if dari in req:
           next=bs(req,"html.parser").find("a",string=dari)["href"]
           if len(id_post) > 200:
              return id_post[:200]
           else:
              dump_post(ses,cokie,mbasic.format(next),type,dari)
       return id_post
    elif type == "komen":
       req=ses.get(url,cookies=cokie).text
       kmn=bs(req,"html.parser").find_all("a",string="Berita Lengkap")
       for x in kmn:
           id_post.append(x["href"])
       if dari in req:
          next=bs(req,"html.parser").find("a",string=dari)["href"]
          if len(id_post) > 200:
             return id_post[:200]
          else:
             dump_post(ses,cokie,mbasic.format(next),type,dari)
       return id_post
    elif type == "delete":
       req=ses.get(url,cookies=cokie).text
       dlt=bs(req,"html.parser").find_all("a",string="Lainnya")
       for x in dlt:
           id_post.append(x["href"])
       if dari in req:
           next=bs(req,"html.parser").find("a",string=dari)["href"]
           dump_post(ses,cokie,mbasic.format(next),type,dari)
       return id_post
    else:
       return False

def people(ses,cokie,url,type):
    if type == "teman":
       req=ses.get(url,cookies=cokie).text
       tmn=re.findall(r'middle"><a class=".." href="(.*?)">',req)
       for x in tmn:
           id_people.append(x)
       if "Lihat Teman Lain" in req:
           next=bs(req,"html.parser").find("a",string="Lihat Teman Lain")["href"]
           people(ses,cokie,mbasic.format(next),type)
       return id_people
    elif type == "temanonline":
       req=ses.get(url,cookies=cokie).text
       on=bs(req,"html.parser").find_all("a",href=lambda x: x and "/messages/read/?fbid=" in x)
       for x in on:
           id_people.append(re.findall(r'=(\d*)',x["href"])[0])
       return id_people
    elif type == "reqteman":
       req=ses.get(url,cookies=cokie).text
       res=bs(req,"html.parser").find_all("a",string="Konfirmasi")
       for x in res:
           id_people.append(x["href"])
       if "Lihat selengkapnya" in req:
          next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
          people(ses,cokie,mbasic.format(next),type)
       return id_people
    elif type == "rejteman":
       req=ses.get(url,cookies=cokie).text
       res=bs(req,"html.parser").find_all("a",string="Hapus Permintaan")
       for x in res:
           id_people.append(x["href"])
       if "Lihat selengkapnya" in req:
          next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
          people(ses,cokie,mbasic.format(next),type)
       return id_people
    elif type == "reqsent":
       req=ses.get(url,cookies=cokie).text
       res=bs(req,"html.parser").find_all("a",string="Batalkan Permintaan")
       for x in res:
           id_people.append(x["href"])
       if "Lihat selengkapnya" in req:
          next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
          people(ses,cokie,mbasic.format(next),type)
       return id_people
    else:
       return False

def find(ses,cokie,url,type):
    if type == "group":
       req=ses.get(url,cookies=cokie).text
       mygroup=re.findall(r'<td class=".."><a href="(.*?)">(.*?)</a></td>',req)
       for x in mygroup:
           id_group.append(x[0].replace("https://mbasic.facebook.com/groups/","").split("/")[0]+"|"+x[1])
       return id_group
    elif type == "people":
       req=ses.get(url,cookies=cokie).text
       horang=re.findall(r'</a></td><td class=".. .."><a href="(.*?)"><div class=".."><div class="..">(.*?)</div></div>',req)
       for x in horang:
           if "Profil telah Diverifikasi" in x[1]:
              name=x[1].split("<")[0]+"\033[00m(\033[1;94m√\033[00m)"
           else:
              name=x[1]
           if "profile" in x[0]:
              id_people.append(re.findall(r'=(\d*)',x[0])[0]+"|"+name)
           else:
              id_people.append(x[0].split("?")[0].replace("/","")+"|"+name)
       if "Lihat Hasil Selanjutnya" in req:
          next=bs(req,"html.parser").find("a",string="Lihat Hasil Selanjutnya")["href"]
          find(ses,cokie,next,type)
       return id_people
    elif type == "msg":
       req=ses.get(url,cookies=cokie).text
       dlt=bs(req,"html.parser").find_all("a",href=lambda x: "/messages/read/" in x)
       for x in dlt:
           id_msg.append(x["href"])
       if "Lihat Pesan Sebelumnya" in req:
           next=bs(req,"html.parser").find("a",string="Lihat Pesan Sebelumnya")["href"]
           find(ses,cokie,mbasic.format(next),type)
       return id_msg
    else:
       return False

def add_friend(cokie,url,type):
    if type == "saran":
       req=requests.get(url,cookies=cokie).text
       pp=bs(req,"html.parser").find_all("a",href=lambda x: "/a/mobile/friends/add_friend.php?" in x)
       for x in pp:
           id_people.append(re.findall(r'id=(\d*)',x["href"])[0])
       if "Lihat selengkapnya" in req:
           next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
           add_friend(cokie,mbasic.format(next),type)
       return id_people
    if type == "search":
       req=requests.get(url,cookies=cokie).text
       pp=bs(req,"html.parser").find_all("a",href=lambda x: "/a/mobile/friends/add_friend.php?" in x)
       for x in pp:
           id_people.append(re.findall(r'id=(\d*)',x["href"])[0])
       if "Lihat selengkapnya" in req:
           next=bs(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]
           add_friend(cokie,mbasic.format(next),type)
       return id_people
    elif type == "friend":
       req=requests.get(url,cookies=cokie).text
       pp=bs(req,"html.parser").find_all("a",href=lambda x: "/a/mobile/friends/add_friend.php?" in x)
       for x in pp:
           id_people.append(re.findall(r'id=(\d*)',x["href"])[0])
       if "Lihat Teman Lain" in req:
           next=bs(req,"html.parser").find("a",string="Lihat Teman Lain")["href"]
           add_friend(cokie,mbasic.format(next),type)
       return id_people
    else:
       return False
