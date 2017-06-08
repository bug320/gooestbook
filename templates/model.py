# -*- utf-8 -*-
import mysql

def selectOrderName(ldb,form):
    ldb.select("")
    pass
def selectOrderID(ldb,form):
    pass
def selectOrderSex(ldb,form):
    pass
def selectOrderEmail(ldb,form):
    pass

def select(ldb,form,where):
    sql = "%s == '%s'"  % (where,form[where])
    k = ldb.select("User",where = sql)
    return k
    pass



