# swagger_client.SearchApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_autocomplete**](SearchApi.md#get_autocomplete) | **GET** /search/entity/autocomplete/{term} | Returns list of matching concepts or entities using lexical search
[**get_search_entities**](SearchApi.md#get_search_entities) | **GET** /search/entity/{term} | Returns list of matching concepts or entities using lexical search


# **get_autocomplete**
> get_autocomplete(term, engine=engine, subclass_of=subclass_of, rows=rows, taxon=taxon, category=category)

Returns list of matching concepts or entities using lexical search

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
term = 'term_example' # str | 
engine = 'engine_example' # str | Name of engine to perform search (optional)
subclass_of = ['subclass_of_example'] # list[str] | restrict search to entities that are subclasses of the specified class (optional)
rows = 20 # int | number of rows (optional) (default to 20)
taxon = 'taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
category = ['category_example'] # list[str] | e.g. gene, disease (optional)

try: 
    # Returns list of matching concepts or entities using lexical search
    api_instance.get_autocomplete(term, engine=engine, subclass_of=subclass_of, rows=rows, taxon=taxon, category=category)
except ApiException as e:
    print("Exception when calling SearchApi->get_autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**|  | 
 **engine** | **str**| Name of engine to perform search | [optional] 
 **subclass_of** | [**list[str]**](str.md)| restrict search to entities that are subclasses of the specified class | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **category** | [**list[str]**](str.md)| e.g. gene, disease | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_entities**
> get_search_entities(term, engine=engine, subclass_of=subclass_of, rows=rows, taxon=taxon, category=category)

Returns list of matching concepts or entities using lexical search

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
term = 'term_example' # str | search string, e.g. shh, parkinson, femur
engine = 'engine_example' # str | Name of engine to perform search (optional)
subclass_of = ['subclass_of_example'] # list[str] | restrict search to entities that are subclasses of the specified class (optional)
rows = 20 # int | number of rows (optional) (default to 20)
taxon = 'taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
category = ['category_example'] # list[str] | e.g. gene, disease (optional)

try: 
    # Returns list of matching concepts or entities using lexical search
    api_instance.get_search_entities(term, engine=engine, subclass_of=subclass_of, rows=rows, taxon=taxon, category=category)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| search string, e.g. shh, parkinson, femur | 
 **engine** | **str**| Name of engine to perform search | [optional] 
 **subclass_of** | [**list[str]**](str.md)| restrict search to entities that are subclasses of the specified class | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **category** | [**list[str]**](str.md)| e.g. gene, disease | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

