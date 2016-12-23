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

def createQM():

	global AdminConfig
	
	jmsProvider = AdminConfig.getid(JMSProviderNameId)
	print jmsProvider
	
	qcfNameAtrr = ["name", qcfName]
	qcfJndiNameAttr = ["jndiName", qcfJNDIName]
	qmNameAttr = ["queueManager", qmName] 
	hostAttr = ["host", host]
	portAttr = ["port", port]
	channelAttr =  ["channel", channel]
	transportTypeAttr = ["transportType", transportType]
	
	attrs = []
	attrs.append(qcfNameAtrr)
	attrs.append(qcfJndiNameAttr)
	attrs.append(qmNameAttr)
	attrs.append(hostAttr)
	attrs.append(portAttr)
	attrs.append(channelAttr)
	attrs.append(transportTypeAttr)
	
	qcf = AdminConfig.create("MQQueueConnectionFactory", jmsProvider, attrs)
	print qcf

	AdminConfig.save()
	

qcfName = "qcfName"
qcfJNDIName = "jms/qcfJNDIName"
qmName = "qmName"
host = "host"
port = "port"
channel = "0000.XXX.XXXX"
transportType="CLIENT"

createQM()
