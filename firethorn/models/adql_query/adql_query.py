'''
Created on Feb 8, 2018

@author: stelios
'''

try:
    import logging
    from models.base.base_object import BaseObject
    import os
    import core as core
    import adql
    import time
except Exception as e:
    logging.exception(e)
    
    
class AdqlQuery(BaseObject):
    """
    classdocs
    """


    def __init__(self, adql_resource, json_object=None, url=None):
        """
        Constructor    
        """
        self.adql_resource = adql_resource
        super().__init__(self.adql_resource.account, json_object, url) 
        self.query_engine = core.query_engine.QueryEngine(self.account)
        
        
    def ident(self):
        if (self.json_object==None):
            if (self.url!=None):
                self.json_object = self.get_json(self.url)
                return os.path.basename(self.json_object.get("self",""))
        else:
            return os.path.basename(self.json_object.get("self",""))
         
        
    def resource(self):
        if (self.json_object!=None):
            return adql.AdqlResource(account=self.account, url=self.json_object.get("workspace",""))
        else:
            return None 
        
        
    def osql(self):
        if (self.json_object==None):
            if (self.url!=None):
                self.json_object = self.get_json(self.url)
                return self.json_object.get("osql","")
        else:
            return self.json_object.get("osql","")
        
        
    def adql(self):
        if (self.json_object==None):
            if (self.url!=None):
                self.json_object = self.get_json(self.url)
                return self.json_object.get("adql","")
        else:
            return self.json_object.get("adql","")


    def error (self):
        """Get Error message
        """
        error = ""
        try: 
            error = self.json_object.get("syntax").get("friendly",None)
        except Exception as e:
            logging.exception(e) 
               
        return error

        
    def status(self, refresh=True):
        if (refresh):
            self.json_object = self.get_json(self.url)
            return self.json_object.get("status","").upper()
        else:
            if (self.json_object==None):
                if (self.url!=None):
                    self.json_object = self.get_json(self.url)
                    return self.json_object.get("status","").upper()
            else:
                return self.json_object.get("status","").upper()
        
        
    def results(self):
        if (self.json_object==None):
            if (self.url!=None):
                self.json_object = self.get_json(self.url)
                return self.json_object.get("results","")
        else:
            return self.json_object.get("results","")


    def table(self):
        if (self.json_object==None):
            if (self.url!=None):
                self.json_object = self.get_json(self.url)
                return self.json_object.get("results","").get("table",None)
        else:
            return self.json_object.get("results","").get("table",None)  
        
        
    def getAttr(self, attribute):
        if (self.json_object==None):
            if (self.url!=None):
                self.json_object = self.get_json(self.url)
                return self.json_object.get(attribute,"")
        else:
            return self.json_object.get(attribute,"")
        
    
    def update(self, adql_query_input=None, adql_query_status_next=None, adql_query_wait_time=None):
        return self.query_engine.update_query(adql_query_input=adql_query_input, adql_query_status_next=adql_query_status_next, adql_query=self, adql_query_wait_time=adql_query_wait_time)


    def run_sync(self):
        self.update(adql_query_status_next="COMPLETED")
        while self.status()=="RUNNING" or self.status()=="READY":
            time.sleep(3)
        
        return 
             
             
    def isRunning(self):
        """
        Check if a Query is running
        """
        
        if (self.status(True)=="RUNNING" or self.status(True)=="READY"):
            return True
        else:
            return False           
        
