# functions
def addDatasourceProperty (datasourceId, name, value):
    params = ["-propertyName", name, "-propertyValue", value]
    AdminTask.setResourceProperty(datasourceId, params)

#0 find out the environment
cell = AdminControl.getCell()
node = AdminControl.getNode()
server="server1"
scope="/Node:"+node+"/Server:"+server

#1 create JDBC provider
providerName="H2 JDBC Provider"
providerId = AdminConfig.getid(scope+"/JDBCProvider:\""+providerName+"\"/" )

#2 create JAAS login


#3 create datasource


#4 save changes
AdminConfig.save()
