# swagger_client.BioentitysetApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_set_associations**](BioentitysetApi.md#get_entity_set_associations) | **GET** /bioentityset/associations/ | Returns compact associations for a given input set
[**get_entity_set_graph_resource**](BioentitysetApi.md#get_entity_set_graph_resource) | **GET** /bioentityset/graph/ | TODO Graph object spanning all entities
[**get_entity_set_over_representation_analysis**](BioentitysetApi.md#get_entity_set_over_representation_analysis) | **GET** /bioentityset/ora/ | TODO Over-representation analysis
[**get_entity_set_over_representation_analysis_0**](BioentitysetApi.md#get_entity_set_over_representation_analysis_0) | **GET** /bioentityset/ora/{object_category}/ | TODO Over-representation analysis
[**get_entity_set_summary**](BioentitysetApi.md#get_entity_set_summary) | **GET** /bioentityset/descriptor/counts/ | Summary statistics for objects associated


# **get_entity_set_associations**
> list[AssociationResults] get_entity_set_associations(background=background, subject=subject, object_category=object_category, object_slim=object_slim)

Returns compact associations for a given input set

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try: 
    # Returns compact associations for a given input set
    api_response = api_instance.get_entity_set_associations(background=background, subject=subject, object_category=object_category, object_slim=object_slim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_graph_resource**
> get_entity_set_graph_resource(background=background, subject=subject, object_category=object_category, object_slim=object_slim)

TODO Graph object spanning all entities

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try: 
    # TODO Graph object spanning all entities
    api_instance.get_entity_set_graph_resource(background=background, subject=subject, object_category=object_category, object_slim=object_slim)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_graph_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_over_representation_analysis**
> get_entity_set_over_representation_analysis(object_category, object_category2, background=background, subject=subject, object_slim=object_slim)

TODO Over-representation analysis

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
object_category2 = 'object_category_example' # str | E.g. phenotype, function
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try: 
    # TODO Over-representation analysis
    api_instance.get_entity_set_over_representation_analysis(object_category, object_category2, background=background, subject=subject, object_slim=object_slim)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_over_representation_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **object_category2** | **str**| E.g. phenotype, function | 
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_over_representation_analysis_0**
> get_entity_set_over_representation_analysis_0(object_category, object_category2, background=background, subject=subject, object_slim=object_slim)

TODO Over-representation analysis

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
object_category2 = 'object_category_example' # str | E.g. phenotype, function
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try: 
    # TODO Over-representation analysis
    api_instance.get_entity_set_over_representation_analysis_0(object_category, object_category2, background=background, subject=subject, object_slim=object_slim)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_over_representation_analysis_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **object_category2** | **str**| E.g. phenotype, function | 
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_set_summary**
> get_entity_set_summary(background=background, subject=subject, object_category=object_category, object_slim=object_slim)

Summary statistics for objects associated

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentitysetApi()
background = ['background_example'] # list[str] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests (optional)
subject = ['subject_example'] # list[str] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 (optional)
object_category = 'object_category_example' # str | E.g. phenotype, function (optional)
object_slim = 'object_slim_example' # str | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED (optional)

try: 
    # Summary statistics for objects associated
    api_instance.get_entity_set_summary(background=background, subject=subject, object_category=object_category, object_slim=object_slim)
except ApiException as e:
    print("Exception when calling BioentitysetApi->get_entity_set_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **background** | [**list[str]**](str.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subject** | [**list[str]**](str.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **object_category** | **str**| E.g. phenotype, function | [optional] 
 **object_slim** | **str**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

