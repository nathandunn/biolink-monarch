# swagger_client.IdentifiermapperApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prefix_collection**](IdentifiermapperApi.md#get_prefix_collection) | **GET** /identifier/mapper/{source}/{target}/ | TODO maps a list of identifiers from a source to a target


# **get_prefix_collection**
> list[Association] get_prefix_collection(source, target)

TODO maps a list of identifiers from a source to a target

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentifiermapperApi()
source = 'source_example' # str | 
target = 'target_example' # str | 

try: 
    # TODO maps a list of identifiers from a source to a target
    api_response = api_instance.get_prefix_collection(source, target)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifiermapperApi->get_prefix_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **target** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

