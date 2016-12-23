#
# set classpath and set jvm  Custom Properties
#
import sys, java

cellname = AdminControl.getCell()
nodename = AdminControl.getNode()
server = "server1"
workSpace = "C:/myproject/"

JDBCProviderName = "Oracle JDBC Driver"
nodeId = "/Cell:" + cellname + "/Node:" + nodename + "/"
serverId = nodeId + "Server:" + server + "/"
jvmId = serverId + "JavaProcessDef:/JavaVirtualMachine:/"

genericJvmArguments="-Xquickstart -Ddefault.client.encoding=GBK -Dfile.encoding=GBK -Duser.language=en_EN -Duser.region=CN"

def setClasspath():

	global AdminConfig
	
	jvm = AdminConfig.getid(jvmId)
	print jvm
	
	classpathAttr = ["classpath", classpath]
	genericJvmArgumentsAttr = ["genericJvmArguments", genericJvmArguments]
	
	attrs = []
	attrs.append(classpathAttr)
	
	AdminConfig.modify(jvm, [["classpath", ""]])
	AdminConfig.modify(jvm, attrs)
	AdminConfig.save()
	
def setCustomProperties():
	global AdminConfig
	
	jvm = AdminConfig.getid(jvmId)
	print jvm
	
	nameAttr = ["name", name]
	valueAttr = ["value", value]
	
	attrs = []
	attrs.append(valueAttr)
	
	#===============================================================
	# Verify that exists, and if existed, modify it
	#===============================================================
	jvms = AdminConfig.list("Property",jvm)
	jvmList = jvms.split(lineSeparator)
	for tJvm in jvmList :
		if tJvm != "" :
			tJvmName = AdminConfig.showAttribute(tJvm, "name")
			if tJvmName == 	name :
				print "============================================================================"
				print "The Java Virtual Machine > Custom Properties :"+name+" existed. Modify it!"
				print "============================================================================"
				AdminConfig.modify(tJvm, attrs)
				AdminConfig.save()
				return
	
	attrs.append(nameAttr)			
	AdminConfig.create("Property",jvm, attrs)
	AdminConfig.save()
	
#set classpath
classpath="C:\myproject\config"	
setClasspath()


#set Custom Properties
name="configPath"
value="C:\myproject\config"
setCustomProperties()





