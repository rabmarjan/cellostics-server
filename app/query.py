def getAll():
    return """select r.roleID, r.roledescription, r.menujson, l.createdon,
               l.loginID, l.name, l.status
               from Role r, Login l
               where r.roleID = l.roleID"""


def customQuery():
    return """select r.roleID, l.loginID, l.name, l.status
              from Role r, Login l where r.roleID = l.roleID"""

def queryWithParam(roleid):
    return "select l.loginID, l.name, l.status from Login l where l.roleid = '"+roleid+"'"


def customList(userid):
    return "select * from app_customlist where user_id = '"+userid+"'"