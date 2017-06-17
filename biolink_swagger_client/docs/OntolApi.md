# swagger_client.OntolApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_information_content_resource**](OntolApi.md#get_information_content_resource) | **GET** /ontol/information_content/{subject_category}/{object_category}/{subject_taxon} | Returns information content (IC) for a set of relevant ontology classes


# **get_information_content_resource**
> get_information_content_resource(subject_category, object_category, subject_taxon, evidence=evidence)

Returns information content (IC) for a set of relevant ontology classes

``` IC = -log2( freq(t) / popSize ) ```  Here the frequency and population is calculated for a particular dataset: e.g. all human disease-phenotype associations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OntolApi()
subject_category = 'subject_category_example' # str | 
object_category = 'object_category_example' # str | 
subject_taxon = 'subject_taxon_example' # str | 
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)

try: 
    # Returns information content (IC) for a set of relevant ontology classes
    api_instance.get_information_content_resource(subject_category, object_category, subject_taxon, evidence=evidence)
except ApiException as e:
    print("Exception when calling OntolApi->get_information_content_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_category** | **str**|  | 
 **object_category** | **str**|  | 
 **subject_taxon** | **str**|  | 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

