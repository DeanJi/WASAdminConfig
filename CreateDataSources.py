#
# Create DataSources
#
import sys, java

cellname = AdminControl.getCell()
nodename = AdminControl.getNode()
server = "server1"

JDBCProviderName = "Oracle JDBC Driver"
nodeId = "/Cell:" + cellname + "/Node:" + nodename + "/"
serverId = nodeId + "Server:" + server + "/"

def CreateDataSources():
	
	global AdminConfig
	global ds_props
	global ds
	global datasourceHelperClassname
	
	manageCachedHandles="false"
	logMissingTransactionContext="true"
	diagnoseConnectionUsage="false"
	statementCacheSize="10"
	authMechanismPreference="BASIC_PASSWORD"
	
	#create DataSource
	if provider == "Sybase" :
		providerType="Sybase JDBC 3 Driver"
		datasourceHelperClassname="com.ibm.websphere.rsadapter.SybaseDataStoreHelper"
	elif provider == "Oracle" :	
		providerType="Oracle JDBC Driver"
		datasourceHelperClassname="com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper"
	print providerType	
	print datasourceHelperClassname
	
	jdbcProvider = AdminConfig.getid(serverId+"JDBCProvider:"+providerType)
	print jdbcProvider
	
	authDataAliasAttr = ["authDataAlias", nodename+"/"+authDataAlias]
	authMechanismPreferenceAttr = ["authMechanismPreference", authMechanismPreference] 
	nameAttr = ["name", name] 
	jndiNameAttr = ["jndiName", jndiName]
	descriptionAttr = ["description", description] 
	datasourceHelperClassnameAttr = ["datasourceHelperClassname", datasourceHelperClassname]
	providerTypeAttr = ["providerType", providerType] 
	manageCachedHandlesAttr = ["manageCachedHandles", manageCachedHandles] 
	logMissingTransactionContextAttr = ["logMissingTransactionContext", logMissingTransactionContext] 
	diagnoseConnectionUsageAttr = ["diagnoseConnectionUsage", diagnoseConnectionUsage]
	statementCacheSizeAttr = ["statementCacheSize", statementCacheSize] 
	
	attrs = []
	attrs.append(authDataAliasAttr)
	attrs.append(authMechanismPreferenceAttr)
	attrs.append(jndiNameAttr)
	attrs.append(descriptionAttr)
	attrs.append(datasourceHelperClassnameAttr)
	attrs.append(manageCachedHandlesAttr)
	attrs.append(logMissingTransactionContextAttr)
	attrs.append(diagnoseConnectionUsageAttr)
	attrs.append(statementCacheSizeAttr)
	
	#===============================================================
	# Verify that exists, and if existed, modify it
	#===============================================================
	dss = AdminConfig.list("DataSource",jdbcProvider)
	dssList = dss.split(lineSeparator)
	for tDs in dssList :
		if tDs != "" :
			tDsName = AdminConfig.showAttribute(tDs,"name")
			if tDsName == name :
				print "==============================================================="
				print "The DataSource :"+name+" existed. Modify it!"
				print "==============================================================="
				ds = tDs
				AdminConfig.modify(tDs,attrs)
				AdminConfig.save()
				return
			
	attrs.append(nameAttr)
	attrs.append(providerTypeAttr) #属性 providerType 是只读属性
	ds = AdminConfig.create("DataSource", jdbcProvider, attrs)
	print ds
	
	#===============================================================
	# Verify that exists, and if existed, modify it
	#===============================================================
	dataSouce = AdminConfig.getid(serverId+"JDBCProvider:"+providerType+"/DataSource:"+name)
	dsps = AdminConfig.list("J2EEResourcePropertySet",dataSouce)
	dspsList = dsps.split(lineSeparator)
	for tDsps in dspsList :
		if tDsps != "" : 
			print "==============================================================="
			print "The J2EEResourcePropertySet :"+name+" existed!"
			print "==============================================================="
			return;
		
	
	#create propertySet
	ds_props = AdminConfig.create('J2EEResourcePropertySet', ds, [])
	print ds_props
	
	AdminConfig.save()


def CreatePropertySets():
	global AdminConfig
	global ds
	global ds_props
	
	if propery_name == "portNumber" :
		propery_type="java.lang.Integer"
	else :
		propery_type="java.lang.String" 				  
	
	nameAttr = ["name", propery_name] 
	typeAttr = ["type", propery_type]
	valueAttr = ["value", propery_value] 
	property_attrs = []
	property_attrs.append(nameAttr)
	property_attrs.append(typeAttr)
	property_attrs.append(valueAttr)
	
	dss = AdminConfig.list("J2EEResourcePropertySet", ds)
	dssList = dss.split(lineSeparator)
	ds_props = dssList[0]
	print ds_props
	#===============================================================
	# Verify that exists, and if existed, modify it
	#===============================================================
	rps = AdminConfig.list("J2EEResourceProperty",ds_props)
	rpsList = rps.split(lineSeparator)
	for trp in rpsList :
		if trp != "" :
			trpName = AdminConfig.showAttribute(trp, "name")
			if trpName == propery_name :
				print "==============================================================="
				print "The J2EEResourcePropertySet :"+name+", J2EEResourceProperty : "+propery_name +" existed! Modifyed !"
				print "==============================================================="
				AdminConfig.modify(trp, property_attrs)
				AdminConfig.save()
				return;
	
	#create propertys
	rp = AdminConfig.create("J2EEResourceProperty", ds_props, property_attrs)
	print rp
	
	AdminConfig.save()
	

#*****************************************************************	
#Sybase
#*****************************************************************
name="SybaseDataSource"
jndiName="jdbc/jndiSybase"
authDataAlias="authDataAliasSybase"
provider="Sybase"
description="New JDBC 3 Datasource."
CreateDataSources()

#property server name
propery_name="databaseName"	      			
propery_value="databaseNameSybase"
CreatePropertySets()

#create resourceProperties databaseName
propery_name="serverName"           
propery_value="serverNameSybase"
CreatePropertySets()

#property portNumber
propery_name="portNumber"             
propery_value="9999"
CreatePropertySets()



#*****************************************************************	
#Oracle
#*****************************************************************
name="OracleDataSource"
jndiName="jdbc/jndiOracle"
authDataAlias="authDataAliasOracle"
provider="Oracle"
description="New Oracle Datasource."
CreateDataSources()


#property server name
propery_name="URL"	      			
propery_value="jdbc:oracle:thin:@host:port:INSTANCE"
CreatePropertySets()


