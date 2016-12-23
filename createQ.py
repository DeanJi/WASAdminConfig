#
# Creating StaRR Queue Connection Factory 
#

import sys, java

cellname = AdminControl.getCell()
nodename = AdminControl.getNode()
server = "server1"

JMSProviderName = "WebSphere MQ JMS Provider"
nodeId = "/Cell:" + cellname + "/Node:" + nodename + "/"
serverId = nodeId + "Server:" + server + "/"

JMSProviderNameId = serverId + "JMSProvider:" + JMSProviderName + "/"

def createQ():

	global AdminConfig
	
	jmsProvider = AdminConfig.getid(JMSProviderNameId)
	print jmsProvider
	
	qNameAtrr = ["name", qName]
	qJndiNameAttr = ["jndiName", qJNDIName]
	baseQNameAttr = ["baseQueueName", baseQName] 
	
	attrs = []
	attrs.append(qNameAtrr)
	attrs.append(qJndiNameAttr)
	attrs.append(baseQNameAttr)
	
	q = AdminConfig.create("MQQueue", jmsProvider, attrs)
	print q

	AdminConfig.save()
		
#---------------------------------------------
# COPS Queues
#---------------------------------------------
qName = "qName"
qJNDIName = "jms/qJNDIName"
baseQName = "XXX.XXX.AF000.REQUEST"
createQ()
