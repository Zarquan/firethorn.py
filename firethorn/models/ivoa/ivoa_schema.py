'''
Created on Feb 8, 2018

@author: stelios
'''

try:
    from base.base_schema import BaseSchema
    import ivoa
    import json
    import config as config
    import logging
    import urllib.request
except Exception as e:
    logging.exception(e)

class IvoaSchema(BaseSchema):
    """
    classdocs
    """


    def __init__(self, auth_engine, json_object=None, url=None):
        """
        Constructor
        """
        super().__init__(auth_engine, json_object, url) 
        

    def select_tables(self):
        table_list = []
        json_list = self.get_json(self.json_object.get("tables",""))

        for table in json_list:
            table_list.append(ivoa.IvoaTable(json_object=table, auth_engine=self.auth_engine))
            
        return table_list
    
    
    def select_table_by_ident(self, ident):
        return ivoa.IvoaTable(url=ident, auth_engine=self.auth_engine)
    
    
    def select_table_by_name(self,table_name):
        response_json = {}
        try :
            response_json = self.get_json( self.url + "/tables/select", {config.ivoa_table_select_by_name_param : table_name })
        except Exception as e:
            logging.exception(e)      
            
        return ivoa.IvoaTable(json_object = response_json, auth_engine=self.auth_engine)  
            
            