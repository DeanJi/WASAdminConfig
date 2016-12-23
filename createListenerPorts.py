#
# Creating Listener Ports
#
import sys, java

cellname = AdminControl.getCell()
nodename = AdminControl.getNode()
server = "server1"

nodeId = "/Cell:" + cellname + "/Node:" + nodename + "/"
serverId = nodeId + "Server:" + server + "/"

def createListenerPorts():

	global AdminConfig
	
	server = AdminConfig.getid(serverId)
	print server
	
	mls = AdminConfig.list('MessageListenerService', server)
	print mls
	
	connectionFactoryJNDINameAtrr = ["connectionFactoryJNDIName", connectionFactoryJNDIName]
	destinationJNDINameAttr = ["destinationJNDIName", destinationJNDIName]
	maxMessagesAttr = ["maxMessages", maxMessages] 
	maxRetriesAttr = ["maxRetries", maxRetries]
	maxSessionsAttr = ["maxSessions", maxSessions]
	nameAttr =  ["name", lpName]
	
	attrs = []
	attrs.append(connectionFactoryJNDINameAtrr)
	attrs.append(destinationJNDINameAttr)
	attrs.append(maxMessagesAttr)
	attrs.append(maxRetriesAttr)
	attrs.append(maxSessionsAttr)
	attrs.append(nameAttr)
	
	lp = AdminConfig.create('ListenerPort', mls, attrs)
	print lp
	print AdminConfig.create('StateManageable', lp, [['initialState', 'START']])
	
	AdminConfig.save()	

connectionFactoryJNDIName = "jms/connectionFactoryJNDIName"
destinationJNDIName = "jms/destinationJNDIName"
maxMessages = "1"
maxRetries = "3"
maxSessions = "10"
lpName = "Test_Listener"

createListenerPorts()	



