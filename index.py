#-*-coding:utf-8-*-

import datetime

import web

import mysql



ldb = mysql.MySQL(dbase="hello")

urls = (
    "/root/(.*)","root",
    "/log/(.*)","log",
    "/index","index",
    "/add/$","add",
    "/reply/$","reply",
    "/delete/$","delete",
    "/","hello"
    )
app = web.application(urls,globals())
db      = web.database(dbn="mysql",db="hello",user="root",pw="root")


render  = web.template.render("templates/",cache=False)
class root:
    def GET(self,form):
        form = {'id':u'','name':u'','passwd':u'','email':u'','sex':u'','result':''}
        #return form
        return render.root(form)
        pass
    def POST(self,form):
        #form = {'id': u'', 'name': u'', 'passwd': u'', 'email': u'', 'sex': u'', 'result': '','where':u'','menu':u''}
        form ={'id': u'','name': u'', 'passwd': u'', 'menu': u'select', 'where': u'name', 'email': u'', 'sex': u'','result':u''}
        i = web.input()
        i = dict(i)
        where = i["where"].encode("utf-8")
        menu =i["menu"].encode("utf-8")
        if menu =="select":
            if i[where] == '':
                return u"<p>Not be NULL</p> <a href='/root/'>back</a>"
            if where == "email":
                return u"<p>Not open</p> <a href='/root/'>back</a>"
            if where == "sex":
                return u"<p>Not open</p> <a href='/root/'>back</a>"

            sql = "select * from User where %s = '%s' " % (where, i.get(where))

            if where == "name" :
                try:
                    kt = ldb.selectSQL("User", sql)
                    kt =kt[0]
                    #return kt
                    kt["result"] = kt
                    kt["menu"]= form["menu"]
                    kt["where"]= form["where"]
                    return render.root(kt)
                except:
                    return
                    pass
            pass
        elif menu == "delete":
            allu = ldb.selectSQL("User","select id,name from User")
            les = len(allu)
            kt =[]
            for i in range(les):
                kt.append(allu[i])
                print i,kt
            if where == '' :
                return u"<p>Not be NULL</p> <a href='/root/'>back</a>"
            if where =='name':
                try:
                    sql = " WHERE %s = '%s' " % (where, i.get(where))
                    ldb.delete("User",where=sql)
                    #db.query(sql)
                    return  u"<p>delete success</p> <a href='/root/'>back</a>"
                except:
                    return u"<p>Somethin wrong</p> <a href='/root/'>back</a>"
                    pass
                pass
            elif where =='email':
                return u"<p>Not open</p> <a href='/root/'>back</a>"
                pass
            elif where =='sex':
                return u"<p>Not open</p> <a href='/root/'>back</a>"
                pass
            elif where =='id':
                return u"<p>Not open</p> <a href='/root/'>back</a>"
                pass
            else:
                pass
            pass
        elif menu == "update":
            return u"<p>Not open</p> <a href='/root/'>back</a>"
            pass
        elif menu == "insert":
            return u"<p>Not open</p> <a href='/root/'>back</a>"
            pass
        else:
            pass

    pass

class hello:
    def GET(self):
        raise web.seeother("/log/")
    def POST(self):
        raise web.seeother("/log/")
class log:

    def GET(self,name):
        return render.log(name)
        pass

    def POST(self,name):
        i = web.input()
        i = dict(i)
        if len(i) == 2:
            sql = "name = '%s'" % i["name"]
            if i.get("name") == u"":
                raise web.seeother("/log/Name can't be null")
            elif i.get("passwd") == u"":
                raise web.seeother("/log/Passwd can't be null")
            else:
                pass
            if i.get("name") == "root":
                raise web.seeother("/root/")
            data = ldb.select("User",where=sql)
            if data == None:
                raise web.seeother("/log/Can't find the User")
            else:
                if data["passwd"] == i["passwd"]:
                    raise web.seeother("/index")
                else:
                    raise web.seeother("/log/PasswdWrong")
        else:
            sql = "name = '%s'" % i["name"]
            if i.get("name") == u"":
                raise web.seeother("/log/Name can't be null")
            elif i.get("passwd") == u"":

                raise web.seeother("/log/Passwd can't be null")
            else:
                pass
            data = ldb.select("User", where=sql)
            if data == None:
                ldb.insert("User",name=i["name"],passwd=i["passwd"],email=i["email"],sex=i["sex"])
                raise web.seeother("/log/OK,Please Sign in")
            else:
                raise web.seeother("/log/Sorry,User is exits")
        pass


class index:
    def GET(self):
        result = db.query("select id,title,reply,content,date from guestbook order by id DESC")
        return render.index(result)


class add:
    def POST(self):
        info = web.input(title="",content="")
        if not info.title or not info.content:
            raise web.seeother("/index")
        ip = web.ctx.env["REMOTE_ADDR"]
        d  = datetime.datetime.now()
        reply = 'no reply'
        sql = "insert into guestbook (title,content,reply,ip,date) values('%s','%s','%s','%s','%s')" %(info.title,info.content,reply,ip,d)
        db.query(sql)
        raise web.seeother("/index")
class delete:
    def GET(self):
        info = web.input(id="")
        sql  = "delete from guestbook where id=%s" %info.id
        db.query(sql)
        raise web.seeother("/index")
class reply:
    def POST(self):
        info = web.input(content='no reply',id='')
        sql  = "update guestbook set reply='%s' where id=%s" %(info.content,info.id)
        db.query(sql)
        raise web.seeother("/index")
    def GET(self):
        info  = web.input(id="")
        sql   = "select id,title,content from guestbook where id = %s" % info.id
        result=db.query(sql)
        return render.reply(result[0])

if __name__=="__main__":
    app.run()

