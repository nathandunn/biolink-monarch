# swagger_client.NlpannotateApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_annotate**](NlpannotateApi.md#get_annotate) | **GET** /nlp/annotate/{text} | Not yet implemented


# **get_annotate**
> list[Association] get_annotate(text, category=category)

Not yet implemented

For now using scigraph annotator directly

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NlpannotateApi()
text = 'text_example' # str | 
category = ['category_example'] # list[str] | E.g. phenotype (optional)

try: 
    # Not yet implemented
    api_response = api_instance.get_annotate(text, category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NlpannotateApi->get_annotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | 
 **category** | [**list[str]**](str.md)| E.g. phenotype | [optional] 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

