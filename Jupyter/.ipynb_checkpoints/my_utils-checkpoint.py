import requests
import json

print("Imported my_utils module")

host = "http://localhost:9200/"
index = "tmdb"
indexBaseUrl = host + index
headers = {"Content-Type": "application/json"}

def toJsonPrettyPrint(response):
    print(json.dumps(json.loads(response), indent=2))
    
def mergeDicts(dict1: dict, dict2: dict):
    mergedDict = dict()
    mergedDict.update(dict1)
    mergedDict.update(dict2)
    return mergedDict
    
def getSearchHits(indexBaseUrl: str, query: str):
    response = requests.get(indexBaseUrl + "/_search", data=json.dumps(query), headers=headers)
    return json.loads(response.text)['hits']

def getSearchHitsHits(indexBaseUrl: str, query: str):
    return getSearchHits(indexBaseUrl, query)['hits']

def parseSearchHits(searchHits: str):
    print("Num\tRelevanceScore\tMovie Title")
    for idx, hit in enumerate(searchHits['hits']):
        print("%s\t%s\t\t%s" %
              (idx+1, str(round(hit['_score'], 1)).rjust(4, ' '), hit['_source']['title']))
        
def titleFromHit(hit):
    return hit['_source']['title']

def explanationFromHit(hit):
    return hit['_explanation']


# explanation tree traversal    
def explanationNode(node, level: int, spaces: str=""):
    val = node['value']
    desc = node['description']
    return "%s└──%s (%s)" %(spaces, val, desc)

def printExplanationTree(node, maxLevel=None, level: int = 0, spaces: str=""):
    children = node['details']
    level += 1
    print(explanationNode(node, level, spaces))
    
    if maxLevel is not None and level == maxLevel:
        print("   %s..." %spaces)
        return
    
    if children:
        for child in children:
            printExplanationTree(child, maxLevel, level, "   " + spaces)      

def titleAndExplanation(hit, maxLevel=None):
    print("title: %s" %titleFromHit(hit))
    printExplanationTree(explanationFromHit(hit), maxLevel)

def printSummary(hit):
    print(json.dumps(titleAndExplanation(hit), indent = 2))
    
def getTokenStrings(analyzeResponse):
    responseJson = json.loads(analyzeResponse.text)
    tokenArray = responseJson['tokens']
    return list(map(lambda obj: obj['token'], tokenArray))

def getFieldFromHits(analyzeResponse, fieldName):
    responseJson = json.loads(analyzeResponse.text)
    fields = responseJson['hits']['hits']
    return list(map(lambda obj: obj['_source'][fieldName], fields))
        

    
