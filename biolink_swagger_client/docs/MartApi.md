# swagger_client.MartApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mart_case_associations_resource**](MartApi.md#get_mart_case_associations_resource) | **GET** /mart/case/{object_category}/{taxon} | Bulk download of case associations
[**get_mart_disease_associations_resource**](MartApi.md#get_mart_disease_associations_resource) | **GET** /mart/disease/{object_category}/{taxon} | Bulk download of disease associations
[**get_mart_gene_associations_resource**](MartApi.md#get_mart_gene_associations_resource) | **GET** /mart/gene/{object_category}/{taxon} | Bulk download of gene associations


# **get_mart_case_associations_resource**
> get_mart_case_associations_resource(object_category, taxon, slim=slim)

Bulk download of case associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
taxon = 'taxon_example' # str | taxon of case, must be of form NCBITaxon:9606
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try: 
    # Bulk download of case associations
    api_instance.get_mart_case_associations_resource(object_category, taxon, slim=slim)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_case_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **taxon** | **str**| taxon of case, must be of form NCBITaxon:9606 | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mart_disease_associations_resource**
> get_mart_disease_associations_resource(object_category, taxon, slim=slim)

Bulk download of disease associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
taxon = 'taxon_example' # str | taxon of disease, must be of form NCBITaxon:9606
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try: 
    # Bulk download of disease associations
    api_instance.get_mart_disease_associations_resource(object_category, taxon, slim=slim)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_disease_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **taxon** | **str**| taxon of disease, must be of form NCBITaxon:9606 | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mart_gene_associations_resource**
> get_mart_gene_associations_resource(object_category, taxon, slim=slim)

Bulk download of gene associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MartApi()
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
taxon = 'taxon_example' # str | taxon of gene, must be of form NCBITaxon:9606
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try: 
    # Bulk download of gene associations
    api_instance.get_mart_gene_associations_resource(object_category, taxon, slim=slim)
except ApiException as e:
    print("Exception when calling MartApi->get_mart_gene_associations_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **taxon** | **str**| taxon of gene, must be of form NCBITaxon:9606 | 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

