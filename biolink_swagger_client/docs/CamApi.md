# swagger_client.CamApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activity_collection**](CamApi.md#get_activity_collection) | **GET** /cam/activity/ | Returns list of models
[**get_instance**](CamApi.md#get_instance) | **GET** /cam/instance/{id} | Returns list of matches
[**get_model**](CamApi.md#get_model) | **GET** /cam/model/{id} | Returns a complete model
[**get_model_collection**](CamApi.md#get_model_collection) | **GET** /cam/model/ | Returns list of ALL models
[**get_model_collection_0**](CamApi.md#get_model_collection_0) | **GET** /cam/model/properties/ | Returns list of all properties used across all models
[**get_model_collection_1**](CamApi.md#get_model_collection_1) | **GET** /cam/model/property_values/ | Returns list property-values for all models
[**get_model_collection_2**](CamApi.md#get_model_collection_2) | **GET** /cam/model/query/ | Returns list of models matching query
[**get_model_contibutors**](CamApi.md#get_model_contibutors) | **GET** /cam/instances/ | Returns list of all instances
[**get_model_contibutors_0**](CamApi.md#get_model_contibutors_0) | **GET** /cam/model/contributors/ | Returns list of all contributors across all models
[**get_physical_interaction**](CamApi.md#get_physical_interaction) | **GET** /cam/physical_interaction/ | Returns list of models


# **get_activity_collection**
> get_activity_collection(contributor=contributor, title=title)

Returns list of models

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)
title = 'title_example' # str | string to search for in title of model (optional)

try: 
    # Returns list of models
    api_instance.get_activity_collection(contributor=contributor, title=title)
except ApiException as e:
    print("Exception when calling CamApi->get_activity_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor** | **str**| string to search for in contributor of model | [optional] 
 **title** | **str**| string to search for in title of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance**
> list[Association] get_instance(id, contributor=contributor, title=title)

Returns list of matches

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
id = 'id_example' # str | 
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)
title = 'title_example' # str | string to search for in title of model (optional)

try: 
    # Returns list of matches
    api_response = api_instance.get_instance(id, contributor=contributor, title=title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CamApi->get_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **contributor** | **str**| string to search for in contributor of model | [optional] 
 **title** | **str**| string to search for in title of model | [optional] 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> get_model(id)

Returns a complete model

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
id = 'id_example' # str | 

try: 
    # Returns a complete model
    api_instance.get_model(id)
except ApiException as e:
    print("Exception when calling CamApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_collection**
> get_model_collection()

Returns list of ALL models

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()

try: 
    # Returns list of ALL models
    api_instance.get_model_collection()
except ApiException as e:
    print("Exception when calling CamApi->get_model_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_collection_0**
> get_model_collection_0(contributor=contributor, title=title)

Returns list of all properties used across all models

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)
title = 'title_example' # str | string to search for in title of model (optional)

try: 
    # Returns list of all properties used across all models
    api_instance.get_model_collection_0(contributor=contributor, title=title)
except ApiException as e:
    print("Exception when calling CamApi->get_model_collection_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor** | **str**| string to search for in contributor of model | [optional] 
 **title** | **str**| string to search for in title of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_collection_1**
> get_model_collection_1(contributor=contributor, title=title)

Returns list property-values for all models

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)
title = 'title_example' # str | string to search for in title of model (optional)

try: 
    # Returns list property-values for all models
    api_instance.get_model_collection_1(contributor=contributor, title=title)
except ApiException as e:
    print("Exception when calling CamApi->get_model_collection_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor** | **str**| string to search for in contributor of model | [optional] 
 **title** | **str**| string to search for in title of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_collection_2**
> get_model_collection_2(contributor=contributor, title=title)

Returns list of models matching query

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)
title = 'title_example' # str | string to search for in title of model (optional)

try: 
    # Returns list of models matching query
    api_instance.get_model_collection_2(contributor=contributor, title=title)
except ApiException as e:
    print("Exception when calling CamApi->get_model_collection_2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor** | **str**| string to search for in contributor of model | [optional] 
 **title** | **str**| string to search for in title of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_contibutors**
> get_model_contibutors()

Returns list of all instances

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()

try: 
    # Returns list of all instances
    api_instance.get_model_contibutors()
except ApiException as e:
    print("Exception when calling CamApi->get_model_contibutors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_contibutors_0**
> get_model_contibutors_0()

Returns list of all contributors across all models

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()

try: 
    # Returns list of all contributors across all models
    api_instance.get_model_contibutors_0()
except ApiException as e:
    print("Exception when calling CamApi->get_model_contibutors_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_physical_interaction**
> get_physical_interaction(contributor=contributor, title=title)

Returns list of models

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CamApi()
contributor = 'contributor_example' # str | string to search for in contributor of model (optional)
title = 'title_example' # str | string to search for in title of model (optional)

try: 
    # Returns list of models
    api_instance.get_physical_interaction(contributor=contributor, title=title)
except ApiException as e:
    print("Exception when calling CamApi->get_physical_interaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contributor** | **str**| string to search for in contributor of model | [optional] 
 **title** | **str**| string to search for in title of model | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

