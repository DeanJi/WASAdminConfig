#
# Auto configure WebSphere
#
import os

baseDir = "C:/myfolder/"

# configure classpath, genericJvmArguments and jvm  Custom Properties
execfile(baseDir+"SetJVM.py")

# Create Oracle JDBC Driver and Sybase JDBC 3 Driver 
execfile(baseDir+"CreateJDBCProviders.py")

# Creating JAAS - J2C authentication data
execfile(baseDir+"CreateJAASAuthData.py")

# Create DataSources
execfile(baseDir+"CreateDataSources.py")


