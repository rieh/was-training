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
jaac = AdminTask.createAuthDataEntry('[-alias h2_login -user sa -password sa -description  ]')

#3 create datasource
datasource = AdminTask.createDatasource(providerId, '[-name h2_ds -jndiName jdbc/testds -dataStoreHelperClassName com.ibm.websphere.rsadapter.GenericDataStoreHelper -containerManagedPersistence true -componentManagedAuthenticationAlias ' + 'localhostNode01/h2_login' + ' ]')

addDatasourceProperty(datasource, 'URL', "jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE;INIT=RUNSCRIPT FROM \'~/init.sql\'")

AdminConfig.save()
