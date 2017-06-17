# swagger_client.EvidencegraphApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_association_object**](EvidencegraphApi.md#get_association_object) | **GET** /evidence/graph/{id} | Returns evidence graph object for a given association
[**get_association_object_0**](EvidencegraphApi.md#get_association_object_0) | **GET** /evidence/graph/{id}/image | Returns evidence graph as a png


# **get_association_object**
> list[Graph] get_association_object(id)

Returns evidence graph object for a given association

Note that every association is assumed to have a unique ID

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvidencegraphApi()
id = 'id_example' # str | association id, e.g. cfef92b7-bfa3-44c2-a537-579078d2de37

try: 
    # Returns evidence graph object for a given association
    api_response = api_instance.get_association_object(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvidencegraphApi->get_association_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| association id, e.g. cfef92b7-bfa3-44c2-a537-579078d2de37 | 

### Return type

[**list[Graph]**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_object_0**
> get_association_object_0(id)

Returns evidence graph as a png

TODO - requires matplotlib which is hard to install

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EvidencegraphApi()
id = 'id_example' # str | association id, e.g. cfef92b7-bfa3-44c2-a537-579078d2de37

try: 
    # Returns evidence graph as a png
    api_instance.get_association_object_0(id)
except ApiException as e:
    print("Exception when calling EvidencegraphApi->get_association_object_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| association id, e.g. cfef92b7-bfa3-44c2-a537-579078d2de37 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

