import logging
from models.query import Query, AsyncQuery
from core.firethorn_engine import FirethornEngine
import models.adql as adql
import urllib
import json
from models.adql import adql_resource


class Workspace(object):
    """
    Workspace client class
         
    Attributes
    ----------
      
    ident: string, optional
        The identity URL of the Workspace
        
    queryspace: string, optional
        The URL of the query schema of the workspace
        
    """

    def __init__(self, adql_resource=None, ident=None, url=None, firethorn_engine=None):
        self.firethorn_engine = firethorn_engine
        self.ident = ident
        self.url = url             
        self.adql_resource = adql_resource
        return        


    @property
    def ident(self):
        return self.__ident
        
        
    @ident.setter
    def ident(self, ident):
        self.__ident = ident 


    @property
    def url(self):
        return self.__url
                

    @url.setter
    def url(self, url):
        self.__url = url 


    @property
    def adql_resource(self):
        return self.__adql_resource

                
    @adql_resource.setter
    def adql_resource(self, adql_resource):
        self.__adql_resource = adql_resource    

    
    def import_schema(self, adql_schema=None, schema_name=None):
        """
        Import a Schema into the workspace
        """
        
        if adql_schema==None:
            adql_schema = self.adql_resource.select_schema_by_name(schema_name)
      
        self.adql_resource.import_adql_schema(adql_schema, schema_name)

    
    def get_schema(self, schema_name=None):
        """
        Get a copy of the schema by name
        """
        adql_schema = self.adql_resource.select_schema_by_name(schema_name)
        return adql_schema

    
    def query(self, query=""):
        """        
        Run a query on the imported resources
        
        Parameters
        ----------
        query : str, required
            The query string
            
        Returns
        -------
        query : `Query`
            The created Query
        """
        
        query = Query(querystring=query, adql_resource=self.adql_resource, firethorn_engine = self.firethorn_engine)
        query.run()
        return query
    
    
    def query_async(self, query=""):
        """        
        Run am Asynchronous query on the imported resources
        
        Parameters
        ----------
        query : str, required
            The query string
            
        Returns
        -------
        query : `AsyncQuery`
            The created AsyncQuery
        """
             
        return AsyncQuery(querystring=query, adql_resource=self.adql_resource, firethorn_engine = self.firethorn_engine)
    

    def get_schemas(self):
        """Get list of schemas in a workspace
        """

        schemas = []
        
        try:
            req = urllib.request.Request( self.adql_resource.url + "/schemas/select", headers=self.firethorn_engine.identity.get_identity_as_headers())
            with urllib.request.urlopen(req) as response:
                schemas_json =  json.loads(response.read().decode('utf-8'))
            response.close()
            for val in schemas_json:
                schemas.append(val["name"])

        except Exception as e:
            logging.exception(e)

        return schemas   
    
    
    def get_tables(self, schemaname):
        """Get list of tables
        
        Parameters
        ----------
        schemaname: string, required
            The name of the schema for which to return the children tables
         
        Returns
        -------
        table_list: list
            List of table names
        """
        schemaident = self.adql_resource.select_schema_by_name(schemaname)
        response_json = None
        table_list = []
        
        try :
            req_exc = urllib.request.Request( schemaident.url + "/tables/select", headers=self.firethorn_engine.identity.get_identity_as_headers())
            with urllib.request.urlopen(req_exc) as response:
                response_json =  json.loads(response.read().decode('utf-8'))
            for val in response_json:
                table_list.append(val["name"])
     
        except Exception as e:
            logging.exception(e)
            
        return table_list

    

