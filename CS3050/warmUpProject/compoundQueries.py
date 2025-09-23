import pyparsing as parser
from pyparsing import *
import firebase_admin
from firebase_admin import firestore, credentials, storage
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate(
    "../warmup-project-53374-firebase-adminsdk-fbsvc-5da6f56b50.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()  # connect to firestore


class Engine:
    def __init__(self) -> None:
        # Call firestore for JSON data
        self.field = OneOrMore(Word(alphas + "(" + ")")).set_parse_action(' '.join)
        self.value = parser.Word(parser.nums)
        self.operator = parser.one_of("< > == <= >=")
        self.condition = Group(self.field + self.operator + self.value)
        self.logical_op = parser.one_of("and or")
        self.query = self.condition + ZeroOrMore(self.logical_op + self.condition)

    def parse_input(self, input_string: str) -> list:
        parsed = self.query.parseString(input_string)
        return parsed.as_list()

    def query_firestore(self, query_list):

        
        # field = query_list[0]
        # operator = query_list[1]
        # value = int(query_list[2])
        connector_list=[]
        condition_list=[]

        for partOfQuery in query_list:
            if partOfQuery in ['or','and']:
                connector_list.append(partOfQuery)
                continue
            else:
                field = partOfQuery[0]
                operator = partOfQuery[1]
                value = partOfQuery[2]### how do we query non integer values??

                fetch = db.collection("Objects").where(
                    filter=FieldFilter("`" + field + "`", operator, value)).stream()
                condition_list.append(fetch)

        if connector_list[0] == "and":# written with a list incase a more than 2 condition query is required for the spec (not implement yet)
            fetch = db.collection("Objects")
            for field, operator, value in condition_list:
                fetch = fetch.where(filter=FieldFilter(field, operator, value))
            return fetch.stream()
        
        ## or block could possibly eb easily improve code using or_() a built in function but to save time this is what i got
        elif connector_list[0] == "or":
            results = {}
            for field, operator, value in condition_list:
                query = db.collection("Objects").where(
                    filter=FieldFilter(field, operator, value)
                ).stream()
            for doc in query:# works by creating a dictionary where duplicate data will just be merged therefore it can act like an or function in this case
                results[doc.id] = doc 
            return results.values()
    
        else:
            field, operator, value = condition_list[0]
            fetch = db.collection("Objects").where(
                filter=FieldFilter(field, operator, value)
            ).stream()
            return fetch
        
                    
        

    
                
