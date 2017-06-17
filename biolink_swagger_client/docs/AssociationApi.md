# swagger_client.AssociationApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_association_object**](AssociationApi.md#get_association_object) | **GET** /association/{id} | Returns the association with a given identifier
[**get_association_search**](AssociationApi.md#get_association_search) | **GET** /association/find/ | Generalized search over complete corpus of associations
[**get_association_search_0**](AssociationApi.md#get_association_search_0) | **GET** /association/find/{subject_category}/ | Returns list of matching associations
[**get_association_search_1**](AssociationApi.md#get_association_search_1) | **GET** /association/find/{subject_category}/{object_category}/ | Returns list of matching associations
[**get_associations_from**](AssociationApi.md#get_associations_from) | **GET** /association/between/{subject}/{object} | Returns associations connecting two entities
[**get_associations_from_0**](AssociationApi.md#get_associations_from_0) | **GET** /association/from/{subject} | Returns list of matching associations starting from a given subject (source)
[**get_associations_to**](AssociationApi.md#get_associations_to) | **GET** /association/to/{object} | Returns list of matching associations pointing to a given object (target)


# **get_association_object**
> list[Association] get_association_object(id, fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)

Returns the association with a given identifier

An association connects, at a minimum, two things, designated subject and object, via some relationship. Associations also include evidence, provenance etc.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
id = 'id_example' # str | 
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
subject = 'subject_example' # str | SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene (optional)
object = 'object_example' # str | OBJECT id, e.g. HP:0011927. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
rows = 10 # int | number of rows (optional) (default to 10)
page = 1 # int | Page number (optional) (default to 1)
graphize = true # bool | If set, includes graph object in response (optional)

try: 
    # Returns the association with a given identifier
    api_response = api_instance.get_association_object(id, fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **subject** | **str**| SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene | [optional] 
 **object** | **str**| OBJECT id, e.g. HP:0011927. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]
 **graphize** | **bool**| If set, includes graph object in response | [optional] 

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_search**
> list[AssociationResults] get_association_search(fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)

Generalized search over complete corpus of associations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
subject = 'subject_example' # str | SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene (optional)
object = 'object_example' # str | OBJECT id, e.g. HP:0011927. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
rows = 10 # int | number of rows (optional) (default to 10)
page = 1 # int | Page number (optional) (default to 1)
graphize = true # bool | If set, includes graph object in response (optional)

try: 
    # Generalized search over complete corpus of associations
    api_response = api_instance.get_association_search(fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **subject** | **str**| SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene | [optional] 
 **object** | **str**| OBJECT id, e.g. HP:0011927. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]
 **graphize** | **bool**| If set, includes graph object in response | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_search_0**
> list[AssociationResults] get_association_search_0(subject_category, object_category, fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)

Returns list of matching associations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
subject_category = 'subject_category_example' # str | CATEGORY of entity at link SUBJECT (source), e.g. gene, disease, genotype
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
subject = 'subject_example' # str | SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene (optional)
object = 'object_example' # str | OBJECT id, e.g. HP:0011927. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
rows = 10 # int | number of rows (optional) (default to 10)
page = 1 # int | Page number (optional) (default to 1)
graphize = true # bool | If set, includes graph object in response (optional)

try: 
    # Returns list of matching associations
    api_response = api_instance.get_association_search_0(subject_category, object_category, fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_search_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_category** | **str**| CATEGORY of entity at link SUBJECT (source), e.g. gene, disease, genotype | 
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **subject** | **str**| SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene | [optional] 
 **object** | **str**| OBJECT id, e.g. HP:0011927. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]
 **graphize** | **bool**| If set, includes graph object in response | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_search_1**
> list[AssociationResults] get_association_search_1(subject_category, object_category, fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)

Returns list of matching associations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
subject_category = 'subject_category_example' # str | CATEGORY of entity at link SUBJECT (source), e.g. gene, disease, genotype
object_category = 'object_category_example' # str | CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
subject = 'subject_example' # str | SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene (optional)
object = 'object_example' # str | OBJECT id, e.g. HP:0011927. Includes inferred by default (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default (optional)
rows = 10 # int | number of rows (optional) (default to 10)
page = 1 # int | Page number (optional) (default to 1)
graphize = true # bool | If set, includes graph object in response (optional)

try: 
    # Returns list of matching associations
    api_response = api_instance.get_association_search_1(subject_category, object_category, fl_excludes_evidence=fl_excludes_evidence, subject=subject, map_identifiers=map_identifiers, object=object, evidence=evidence, subject_taxon=subject_taxon, rows=rows, page=page, graphize=graphize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_association_search_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_category** | **str**| CATEGORY of entity at link SUBJECT (source), e.g. gene, disease, genotype | 
 **object_category** | **str**| CATEGORY of entity at link OBJECT (target), e.g. phenotype, disease | 
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **subject** | **str**| SUBJECT id, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357. Includes inferred by default | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene | [optional] 
 **object** | **str**| OBJECT id, e.g. HP:0011927. Includes inferred by default | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]
 **graphize** | **bool**| If set, includes graph object in response | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations_from**
> list[AssociationResults] get_associations_from(object, subject, use_compact_associations=use_compact_associations, fl_excludes_evidence=fl_excludes_evidence, map_identifiers=map_identifiers, subject_taxon=subject_taxon, graphize=graphize, evidence=evidence, subject_category=subject_category, rows=rows, page=page, object_category=object_category, slim=slim)

Returns associations connecting two entities

Given two entities (e.g. a particular gene and a particular disease), if these two entities are connected (directly or indirectly), then return the association objects describing the connection.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
object = 'object_example' # str | E.g. e.g. MP:0013765, can also be a biological entity such as a gene
subject = 'subject_example' # str | E.g. e.g. MGI:1342287
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene, HP, OMIM, DOID (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferences by default (higher level taxa can be used) (optional)
graphize = true # bool | If set, includes graph object in response (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_category = 'subject_category_example' # str | e.g. gene, genotype, disease, function (todo: use enum) (optional)
rows = 10 # int | limit on number of rows (optional) (default to 10)
page = 1 # int | Return results starting with this row number (optional) (default to 1)
object_category = 'object_category_example' # str | e.g. disease, phenotype, gene (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try: 
    # Returns associations connecting two entities
    api_response = api_instance.get_associations_from(object, subject, use_compact_associations=use_compact_associations, fl_excludes_evidence=fl_excludes_evidence, map_identifiers=map_identifiers, subject_taxon=subject_taxon, graphize=graphize, evidence=evidence, subject_category=subject_category, rows=rows, page=page, object_category=object_category, slim=slim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_associations_from: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| E.g. e.g. MP:0013765, can also be a biological entity such as a gene | 
 **subject** | **str**| E.g. e.g. MGI:1342287 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene, HP, OMIM, DOID | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferences by default (higher level taxa can be used) | [optional] 
 **graphize** | **bool**| If set, includes graph object in response | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_category** | **str**| e.g. gene, genotype, disease, function (todo: use enum) | [optional] 
 **rows** | **int**| limit on number of rows | [optional] [default to 10]
 **page** | **int**| Return results starting with this row number | [optional] [default to 1]
 **object_category** | **str**| e.g. disease, phenotype, gene | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations_from_0**
> list[AssociationResults] get_associations_from_0(subject, use_compact_associations=use_compact_associations, fl_excludes_evidence=fl_excludes_evidence, map_identifiers=map_identifiers, subject_taxon=subject_taxon, graphize=graphize, evidence=evidence, subject_category=subject_category, rows=rows, page=page, object_category=object_category, slim=slim)

Returns list of matching associations starting from a given subject (source)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
subject = 'subject_example' # str | Return associations emanating from this node, e.g. specifying NCBIGene:84570 will return gene-phenotype, gene-function etc for this gene
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene, HP, OMIM, DOID (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferences by default (higher level taxa can be used) (optional)
graphize = true # bool | If set, includes graph object in response (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_category = 'subject_category_example' # str | e.g. gene, genotype, disease, function (todo: use enum) (optional)
rows = 10 # int | limit on number of rows (optional) (default to 10)
page = 1 # int | Return results starting with this row number (optional) (default to 1)
object_category = 'object_category_example' # str | e.g. disease, phenotype, gene (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try: 
    # Returns list of matching associations starting from a given subject (source)
    api_response = api_instance.get_associations_from_0(subject, use_compact_associations=use_compact_associations, fl_excludes_evidence=fl_excludes_evidence, map_identifiers=map_identifiers, subject_taxon=subject_taxon, graphize=graphize, evidence=evidence, subject_category=subject_category, rows=rows, page=page, object_category=object_category, slim=slim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_associations_from_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Return associations emanating from this node, e.g. specifying NCBIGene:84570 will return gene-phenotype, gene-function etc for this gene | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene, HP, OMIM, DOID | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferences by default (higher level taxa can be used) | [optional] 
 **graphize** | **bool**| If set, includes graph object in response | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_category** | **str**| e.g. gene, genotype, disease, function (todo: use enum) | [optional] 
 **rows** | **int**| limit on number of rows | [optional] [default to 10]
 **page** | **int**| Return results starting with this row number | [optional] [default to 1]
 **object_category** | **str**| e.g. disease, phenotype, gene | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associations_to**
> list[AssociationResults] get_associations_to(object, use_compact_associations=use_compact_associations, fl_excludes_evidence=fl_excludes_evidence, map_identifiers=map_identifiers, subject_taxon=subject_taxon, graphize=graphize, evidence=evidence, subject_category=subject_category, rows=rows, page=page, object_category=object_category, slim=slim)

Returns list of matching associations pointing to a given object (target)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationApi()
object = 'object_example' # str | Return associations pointing to this node. E.g. specifying MP:0013765 will return all genes, variants, strains etc annotated with this term. Can also be a biological entity such as a gene
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
fl_excludes_evidence = true # bool | If set, excludes evidence objects in response (optional)
map_identifiers = 'map_identifiers_example' # str | Prefix to map all IDs to. E.g. NCBIGene, HP, OMIM, DOID (optional)
subject_taxon = 'subject_taxon_example' # str | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferences by default (higher level taxa can be used) (optional)
graphize = true # bool | If set, includes graph object in response (optional)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
subject_category = 'subject_category_example' # str | e.g. gene, genotype, disease, function (todo: use enum) (optional)
rows = 10 # int | limit on number of rows (optional) (default to 10)
page = 1 # int | Return results starting with this row number (optional) (default to 1)
object_category = 'object_category_example' # str | e.g. disease, phenotype, gene (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)

try: 
    # Returns list of matching associations pointing to a given object (target)
    api_response = api_instance.get_associations_to(object, use_compact_associations=use_compact_associations, fl_excludes_evidence=fl_excludes_evidence, map_identifiers=map_identifiers, subject_taxon=subject_taxon, graphize=graphize, evidence=evidence, subject_category=subject_category, rows=rows, page=page, object_category=object_category, slim=slim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationApi->get_associations_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Return associations pointing to this node. E.g. specifying MP:0013765 will return all genes, variants, strains etc annotated with this term. Can also be a biological entity such as a gene | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **fl_excludes_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **map_identifiers** | **str**| Prefix to map all IDs to. E.g. NCBIGene, HP, OMIM, DOID | [optional] 
 **subject_taxon** | **str**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferences by default (higher level taxa can be used) | [optional] 
 **graphize** | **bool**| If set, includes graph object in response | [optional] 
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **subject_category** | **str**| e.g. gene, genotype, disease, function (todo: use enum) | [optional] 
 **rows** | **int**| limit on number of rows | [optional] [default to 10]
 **page** | **int**| Return results starting with this row number | [optional] [default to 1]
 **object_category** | **str**| e.g. disease, phenotype, gene | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

[**list[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

