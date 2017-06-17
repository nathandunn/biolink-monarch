# swagger_client.BioentitysetslimmerApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_set_slimmer**](BioentitysetslimmerApi.md#get_entity_set_slimmer) | **GET** /bioentityset/slimmer/{category} | Summarize a set of objects


# **get_entity_set_slimmer**
> get_entity_set_slimmer(category, subject=subject, slim=slim)

Summarize a set of objects

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetslimmerApi()
category = 'category_example' # str | 
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) (optional)

try: 
    # Summarize a set of objects
    api_instance.get_entity_set_slimmer(category, subject=subject, slim=slim)
except ApiException as e:
    print("Exception when calling BioentitysetslimmerApi->get_entity_set_slimmer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

