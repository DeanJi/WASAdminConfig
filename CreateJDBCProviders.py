#
# Creating Oracle JDBC Driver and Sybase JDBC 3 Driver 
#
import sys, java

cellname = AdminControl.getCell()
nodename = AdminControl.getNode()
server = "server1"
workSpace = "C:/myproject/"

JDBCProviderName = "Oracle JDBC Driver"
nodeId = "/Cell:" + cellname + "/Node:" + nodename + "/"
serverId = nodeId + "Server:" + server + "/"

def CreateJDBCProviders():

	global AdminConfig
	
	server = AdminConfig.getid(serverId)
	print server
	
	
	providerTypeAttr = ["providerType", providerType]
	nameAttr = ["name", name] 
	implementationClassNameAttr = ["implementationClassName", implementationClassName]
	descriptionAttr = ["description", description]
	xaAttr = ["xa", xa]
	classpathAttr =  ["classpath", classpath]
	nativepathAttr = ["nativepath", nativepath]
	
	attrs = []
	attrs.append(implementationClassNameAttr)
	attrs.append(descriptionAttr)
	attrs.append(xaAttr)
	attrs.append(classpathAttr)
	attrs.append(nativepathAttr)
	
	#===============================================================
	# Verify that exists, and if existed, modify it
	#===============================================================
	jps = AdminConfig.list("JDBCProvider", server)
	jpsList = jps.split(lineSeparator)
	print jpsList
	for sJps in jpsList :
		vhname = AdminConfig.showAttribute(sJps, 'name')
		if vhname == name :
			print "=============================================="
			print "The JDBCProvider :"+name+" existed. Modify it!"
			print "=============================================="
			AdminConfig.modify(sJps, attrs)
			AdminConfig.save()
			return
	
	attrs.append(nameAttr)	
	attrs.append(providerTypeAttr)   #providerType is readOnly can't modify
	qcf = AdminConfig.create("JDBCProvider", server, attrs)
	print qcf
	
	AdminConfig.save()
	
#oracle
providerType="Oracle JDBC Driver"
name="Oracle JDBC Driver"
implementationClassName="oracle.jdbc.pool.OracleConnectionPoolDataSource"
description="Oracle JDBC Driver"
xa="false"
classpath=workSpace+"config/lib/ojdbc6-11.2.0.2.0.jar" #${ORACLE_JDBC_DRIVER_PATH}
nativepath=""

CreateJDBCProviders()

#Sybase
providerType="Sybase JDBC 3 Driver"
name="Sybase JDBC 3 Driver"
implementationClassName="com.sybase.jdbc3.jdbc.SybConnectionPoolDataSource"
description="Sybase JDBC 3 Driver. This provider is only configurable in version 6.1 and later nodes"
xa="false"
classpath=workSpace+"config/lib/jconn3.jar" #${SYBASE_JDBC_DRIVER_PATH}
nativepath=""

CreateJDBCProviders()	