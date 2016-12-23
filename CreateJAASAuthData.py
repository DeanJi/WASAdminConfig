#
# Creating JAAS - J2C authentication data
#
import sys, java

cellname = AdminControl.getCell()
nodename = AdminControl.getNode()

nodeId = "/Cell:" + cellname + "/"
securityId = nodeId + "Security:"+"/"
print securityId     		#cells/NWHKG000Node01Cell/security.xml

def CreateJAASAuthData():
	
	global AdminConfig
	
	security = AdminConfig.getid(securityId)
	print security
	
	aliasAttr = ["alias", nodename+"/"+alias]
	userIdAttr = ["userId", userId] 
	passwordAttr = ["password", password]
	
	attrs = []
	attrs.append(userIdAttr)
	attrs.append(passwordAttr)
	
	#===============================================================
	# Verify that exists, and if existed, modify it
	#===============================================================
	j2c = AdminConfig.list("JAASAuthData", security)
	j2cList = j2c.split(lineSeparator)
	print j2cList
	if(len(j2cList) > 1) :
		for tJ2c in j2cList :
			tJ2cName = AdminConfig.showAttribute(tJ2c,"alias")
			if tJ2cName == nodename+"/"+alias :
				print "==============================================================="
				print "The JAASAuthData :"+nodename+"/"+alias+" existed. Modify it!"
				print "==============================================================="
				AdminConfig.modify(tJ2c,attrs)
				AdminConfig.save()
				return
	
	attrs.append(aliasAttr)
	qcf = AdminConfig.create("JAASAuthData", security, attrs) 
	print qcf
	
	AdminConfig.save()


#STARR_HK
alias="alias"
userId="userId"
password="password"

CreateJAASAuthData()


