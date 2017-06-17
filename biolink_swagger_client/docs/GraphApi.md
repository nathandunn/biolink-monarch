# swagger_client.GraphApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_edge_resource**](GraphApi.md#get_edge_resource) | **GET** /graph/edges/from/{id} | Returns edges emanating from a node
[**get_node_resource**](GraphApi.md#get_node_resource) | **GET** /graph/node/{id} | Returns a graph node


# **get_edge_resource**
> list[Graph] get_edge_resource(id)

Returns edges emanating from a node

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | CURIE e.g. HP:0000465

try: 
    # Returns edges emanating from a node
    api_response = api_instance.get_edge_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->get_edge_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE e.g. HP:0000465 | 

### Return type

[**list[Graph]**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_resource**
> list[Graph] get_node_resource(id)

Returns a graph node

A node is an abstract representation of some kind of entity. The entity may be a physical thing such as a patient, a molecular entity such as a gene or protein, or a conceptual entity such as a class from an ontology.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GraphApi()
id = 'id_example' # str | CURIE e.g. HP:0000465

try: 
    # Returns a graph node
    api_response = api_instance.get_node_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->get_node_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE e.g. HP:0000465 | 

### Return type

[**list[Graph]**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

