# swagger_client.OntolsubgraphApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extract_ontology_subgraph_resource**](OntolsubgraphApi.md#get_extract_ontology_subgraph_resource) | **GET** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology
[**get_test_me**](OntolsubgraphApi.md#get_test_me) | **GET** /ontol/subgraph/testme | Extract a subgraph from an ontology


# **get_extract_ontology_subgraph_resource**
> get_extract_ontology_subgraph_resource(ontology, node, cnode=cnode, relation=relation)

Extract a subgraph from an ontology

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolsubgraphApi()
ontology = 'ontology_example' # str | ontology id, e.g. go, uberon, mp, hp)
node = 'node_example' # str | class id. E.g. UBERON:0002102
cnode = ['cnode_example'] # list[str] | Additional classes (optional)
relation = ['relation_example'] # list[str] | Additional classes (optional)

try: 
    # Extract a subgraph from an ontology
    api_instance.get_extract_ontology_subgraph_resource(ontology, node, cnode=cnode, relation=relation)
except ApiException as e:
    print("Exception when calling OntolsubgraphApi->get_extract_ontology_subgraph_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ontology** | **str**| ontology id, e.g. go, uberon, mp, hp) | 
 **node** | **str**| class id. E.g. UBERON:0002102 | 
 **cnode** | [**list[str]**](str.md)| Additional classes | [optional] 
 **relation** | [**list[str]**](str.md)| Additional classes | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_me**
> get_test_me(cnode=cnode, relation=relation)

Extract a subgraph from an ontology

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolsubgraphApi()
cnode = ['cnode_example'] # list[str] | Additional classes (optional)
relation = ['relation_example'] # list[str] | Additional classes (optional)

try: 
    # Extract a subgraph from an ontology
    api_instance.get_test_me(cnode=cnode, relation=relation)
except ApiException as e:
    print("Exception when calling OntolsubgraphApi->get_test_me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cnode** | [**list[str]**](str.md)| Additional classes | [optional] 
 **relation** | [**list[str]**](str.md)| Additional classes | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

