# swagger_client.PubpubsApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_foo**](PubpubsApi.md#get_foo) | **GET** /pub/pubs/{term} | TODO Returns list of matches


# **get_foo**
> list[Association] get_foo(term)

TODO Returns list of matches

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PubpubsApi()
term = 'term_example' # str | 

try: 
    # TODO Returns list of matches
    api_response = api_instance.get_foo(term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PubpubsApi->get_foo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

