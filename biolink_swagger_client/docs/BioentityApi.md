# swagger_client.BioentityApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allele_object**](BioentityApi.md#get_allele_object) | **GET** /bioentity/allele/{id} | TODO Returns allele object
[**get_anatomy_gene_associations**](BioentityApi.md#get_anatomy_gene_associations) | **GET** /bioentity/anatomy/{id}/genes/ | TODO Returns associations between anatomical entity and genes
[**get_anatomy_object**](BioentityApi.md#get_anatomy_object) | **GET** /bioentity/anatomy/{id} | TODO Returns anatomical entity
[**get_anatomy_phenotype_associations**](BioentityApi.md#get_anatomy_phenotype_associations) | **GET** /bioentity/anatomy/{id}/phenotypes/ | TODO Returns associations between anatomical entity and phenotypes
[**get_disease_anatomy_associations**](BioentityApi.md#get_disease_anatomy_associations) | **GET** /bioentity/disease/{id}/anatomy/ | TODO Returns anatomical locations associated with a disease
[**get_disease_function_associations**](BioentityApi.md#get_disease_function_associations) | **GET** /bioentity/disease/{id}/function/ | TODO Returns biological functions associated with a disease
[**get_disease_gene_associations**](BioentityApi.md#get_disease_gene_associations) | **GET** /bioentity/disease/{id}/genes/ | Returns genes associated with a disease
[**get_disease_model_associations**](BioentityApi.md#get_disease_model_associations) | **GET** /bioentity/disease/{id}/models/ | Returns associations to models of the disease
[**get_disease_model_taxon_associations**](BioentityApi.md#get_disease_model_taxon_associations) | **GET** /bioentity/disease/{id}/models/{taxon} | Same as &#x60;/disease/&lt;id&gt;/models&#x60; but constrain models by taxon
[**get_disease_object**](BioentityApi.md#get_disease_object) | **GET** /bioentity/disease/{id} | TODO Returns disease object
[**get_disease_phenotype_associations**](BioentityApi.md#get_disease_phenotype_associations) | **GET** /bioentity/disease/{id}/phenotypes/ | Returns phenotypes associated with disease
[**get_disease_substance_associations**](BioentityApi.md#get_disease_substance_associations) | **GET** /bioentity/disease/{id}/substance/ | Returns substances associated with a disease
[**get_disease_substance_associations_0**](BioentityApi.md#get_disease_substance_associations_0) | **GET** /bioentity/substance/{id}/treats/ | Returns substances associated with a disease
[**get_environment_object**](BioentityApi.md#get_environment_object) | **GET** /bioentity/environment/{id} | TODO Returns environment entity
[**get_environment_phenotype_associations**](BioentityApi.md#get_environment_phenotype_associations) | **GET** /bioentity/environment/{id}/phenotypes/ | TODO Returns list of associations
[**get_gene_disease_associations**](BioentityApi.md#get_gene_disease_associations) | **GET** /bioentity/gene/{id}/diseases/ | Returns diseases associated with gene
[**get_gene_expression_associations**](BioentityApi.md#get_gene_expression_associations) | **GET** /bioentity/gene/{id}/expressed/ | TODO Returns expression events for a gene
[**get_gene_function_associations**](BioentityApi.md#get_gene_function_associations) | **GET** /bioentity/gene/{id}/function/ | Returns function associations for a gene
[**get_gene_homolog_associations**](BioentityApi.md#get_gene_homolog_associations) | **GET** /bioentity/gene/{id}/homologs/ | Returns homologs for a gene
[**get_gene_interactions**](BioentityApi.md#get_gene_interactions) | **GET** /bioentity/gene/{id}/interactions/ | Returns interactions for a gene
[**get_gene_object**](BioentityApi.md#get_gene_object) | **GET** /bioentity/gene/{id} | Returns gene object
[**get_gene_phenotype_associations**](BioentityApi.md#get_gene_phenotype_associations) | **GET** /bioentity/gene/{id}/phenotypes/ | Returns phenotypes associated with gene
[**get_gene_publication_list**](BioentityApi.md#get_gene_publication_list) | **GET** /bioentity/gene/{id}/pubs/ | TODO Returns expression events for a gene
[**get_geneproduct_object**](BioentityApi.md#get_geneproduct_object) | **GET** /bioentity/geneproduct/{id} | TODO Returns gene product object
[**get_generic_associations**](BioentityApi.md#get_generic_associations) | **GET** /bioentity/{id}/associations/ | Returns associations for an entity regardless of the type
[**get_generic_object**](BioentityApi.md#get_generic_object) | **GET** /bioentity/{id} | TODO Returns object of any type
[**get_genotype_disease_associations**](BioentityApi.md#get_genotype_disease_associations) | **GET** /bioentity/genotype/{id}/diseases/ | Returns diseases associated with a genotype
[**get_genotype_gene_associations**](BioentityApi.md#get_genotype_gene_associations) | **GET** /bioentity/genotype/{id}/genes/ | Returns genes associated with a genotype
[**get_genotype_genotype_associations**](BioentityApi.md#get_genotype_genotype_associations) | **GET** /bioentity/genotype/{id}/genotypes/ | Returns genotypes-genotype associations
[**get_genotype_object**](BioentityApi.md#get_genotype_object) | **GET** /bioentity/genotype/{id} | Returns genotype object
[**get_genotype_phenotype_associations**](BioentityApi.md#get_genotype_phenotype_associations) | **GET** /bioentity/genotype/{id}/phenotypes/ | Returns phenotypes associated with a genotype
[**get_goterm_gene_associations**](BioentityApi.md#get_goterm_gene_associations) | **GET** /bioentity/goterm/{id}/genes/ | TODO Returns associated genes
[**get_goterm_object**](BioentityApi.md#get_goterm_object) | **GET** /bioentity/goterm/{id} | TODO Returns GO class object
[**get_goterm_phenotype_associations**](BioentityApi.md#get_goterm_phenotype_associations) | **GET** /bioentity/goterm/{id}/phenotype/ | TODO Returns associated phenotypes
[**get_literature_disease_associations**](BioentityApi.md#get_literature_disease_associations) | **GET** /bioentity/literature/{id}/diseases/ | Returns associations between a lit entity and a disease
[**get_literature_gene_associations**](BioentityApi.md#get_literature_gene_associations) | **GET** /bioentity/literature/{id}/genes/ | Returns associations between a lit entity and a gene
[**get_literature_genotype_associations**](BioentityApi.md#get_literature_genotype_associations) | **GET** /bioentity/literature/{id}/genotypes/ | Returns associations between a lit entity and a genotype
[**get_parent_object**](BioentityApi.md#get_parent_object) | **GET** /bioentity/individual/{id} | TODO Returns individual
[**get_parent_object_0**](BioentityApi.md#get_parent_object_0) | **GET** /bioentity/investigation/{id} | TODO Returns investigation object
[**get_pathway_gene_associations**](BioentityApi.md#get_pathway_gene_associations) | **GET** /bioentity/pathway/{id}/genes/ | TODO Returns list of genes associated with a pathway
[**get_pathway_object**](BioentityApi.md#get_pathway_object) | **GET** /bioentity/pathway/{id} | TODO Returns pathway object
[**get_pathway_participant_associations**](BioentityApi.md#get_pathway_participant_associations) | **GET** /bioentity/pathway/{id}/participants/ | TODO Returns associations to participants (molecules, etc) for a pathway
[**get_phenotype_anatomy_associations**](BioentityApi.md#get_phenotype_anatomy_associations) | **GET** /bioentity/phenotype/{id}/anatomy/ | Returns anatomical entities associated with a phenotype
[**get_phenotype_function_associations**](BioentityApi.md#get_phenotype_function_associations) | **GET** /bioentity/phenotype/{id}/function/ | TODO Returns biological functions associated with a Phenotype
[**get_phenotype_gene_associations**](BioentityApi.md#get_phenotype_gene_associations) | **GET** /bioentity/phenotype/{id}/gene/{taxid}/ids | Returns gene ids for all genes for a particular phenotype in a taxon
[**get_phenotype_gene_associations_0**](BioentityApi.md#get_phenotype_gene_associations_0) | **GET** /bioentity/phenotype/{id}/genes/ | TODO Returns associated phenotypes
[**get_phenotype_object**](BioentityApi.md#get_phenotype_object) | **GET** /bioentity/phenotype/{id} | TODO Returns phenotype class object
[**get_phenotype_phenotype_associations**](BioentityApi.md#get_phenotype_phenotype_associations) | **GET** /bioentity/phenotype/{id}/phenotype/ | TODO Returns associated phenotypes
[**get_pub_object**](BioentityApi.md#get_pub_object) | **GET** /bioentity/literature/{id} | TODO Returns publication object
[**get_sequence_feature_object**](BioentityApi.md#get_sequence_feature_object) | **GET** /bioentity/sequence_feature/{id} | TODO Returns seqfeature
[**get_substance_exposures**](BioentityApi.md#get_substance_exposures) | **GET** /bioentity/substance/{id}/exposures/ | TODO Returns associations between a substance and related exposures
[**get_substance_interactions**](BioentityApi.md#get_substance_interactions) | **GET** /bioentity/substance/{id}/interactions/ | TODO Returns associations between given drug and interactions
[**get_substance_object**](BioentityApi.md#get_substance_object) | **GET** /bioentity/substance/{id} | TODO Returns substance entity
[**get_substance_participant_in_associations**](BioentityApi.md#get_substance_participant_in_associations) | **GET** /bioentity/substance/{id}/participant_in/ | Returns associations between an activity and process and the specified substance
[**get_substance_relationships**](BioentityApi.md#get_substance_relationships) | **GET** /bioentity/substance/{id}/substances/ | TODO Returns associations between a substance and other substances
[**get_substance_role_associations**](BioentityApi.md#get_substance_role_associations) | **GET** /bioentity/substance/{id}/roles/ | Returns associations between given drug and roles
[**get_substance_target_associations**](BioentityApi.md#get_substance_target_associations) | **GET** /bioentity/substance/{id}/targets/ | TODO Returns associations between given drug and targets
[**get_variant_gene_associations**](BioentityApi.md#get_variant_gene_associations) | **GET** /bioentity/variant/{id}/genes/ | Returns genes associated with a variant
[**get_variant_genotype_associations**](BioentityApi.md#get_variant_genotype_associations) | **GET** /bioentity/variant/{id}/genotypes/ | Returns genotypes associated with a variant
[**get_variant_object**](BioentityApi.md#get_variant_object) | **GET** /bioentity/variant/{id} | TODO Returns sequence variant entity
[**get_variant_phenotype_associations**](BioentityApi.md#get_variant_phenotype_associations) | **GET** /bioentity/variant/{id}/phenotypes/ | Returns phenotypes associated with a variant


# **get_allele_object**
> list[Allele] get_allele_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns allele object

This is a composition of multiple smaller operations, including fetching allele metadata, plus allele associations  TODO - should allele be subsumed into variant?

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns allele object
    api_response = api_instance.get_allele_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_allele_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Allele]**](Allele.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anatomy_gene_associations**
> list[Association] get_anatomy_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations between anatomical entity and genes

Typically encompasses genes expressed in a particular location.  INFERENCE: part-of

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations between anatomical entity and genes
    api_response = api_instance.get_anatomy_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_anatomy_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anatomy_object**
> get_anatomy_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns anatomical entity

Anatomical entities span ranges from the subcellular (e.g. nucleus) through cells to tissues, organs and organ systems.  When returning associations, inference over the appropriate relation will be used. For example, for gene expression, part-of will be used.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns anatomical entity
    api_instance.get_anatomy_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_anatomy_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anatomy_phenotype_associations**
> list[Association] get_anatomy_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations between anatomical entity and phenotypes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations between anatomical entity and phenotypes
    api_response = api_instance.get_anatomy_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_anatomy_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_anatomy_associations**
> list[Association] get_disease_anatomy_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns anatomical locations associated with a disease

For example, neurodegeneratibe disease located in nervous system. For cancer, this may include both site of original and end location.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns anatomical locations associated with a disease
    api_response = api_instance.get_disease_anatomy_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_anatomy_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_function_associations**
> list[Association] get_disease_function_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns biological functions associated with a disease

This may come from a combination of asserted knowledge (e.g. Fanconi Anemia affects DNA repair) or from data-driven approach (cf Translator)  Results are typically represented as GO classes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns biological functions associated with a disease
    api_response = api_instance.get_disease_function_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_function_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_gene_associations**
> AssociationResults get_disease_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns genes associated with a disease

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns genes associated with a disease
    api_response = api_instance.get_disease_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_model_associations**
> AssociationResults get_disease_model_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations to models of the disease

In the association object returned, the subject will be the disease, and the object will be the model. The model may be a gene or genetic element.  If the query disease is a general class, the association subject may be to a specific disease.  In some cases the association will be *direct*, for example if a paper asserts a genotype is a model of a disease.  In other cases, the association will be *indirect*, for example, chaining over orthology. In these cases the chain will be reflected in the *evidence graph*  * TODO: provide hook into owlsim for dynamic computation of models by similarity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations to models of the disease
    api_response = api_instance.get_disease_model_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_model_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_model_taxon_associations**
> AssociationResults get_disease_model_taxon_associations(id, taxon, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Same as `/disease/<id>/models` but constrain models by taxon

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
taxon = 'taxon_example' # str | CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:6239 (C elegans).   Higher level taxa may be used
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Same as `/disease/<id>/models` but constrain models by taxon
    api_response = api_instance.get_disease_model_taxon_associations(id, taxon, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_model_taxon_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **taxon** | **str**| CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:6239 (C elegans).   Higher level taxa may be used | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_object**
> get_disease_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns disease object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns disease object
    api_instance.get_disease_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_phenotype_associations**
> AssociationResults get_disease_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns phenotypes associated with disease

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns phenotypes associated with disease
    api_response = api_instance.get_disease_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_substance_associations**
> get_disease_substance_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns substances associated with a disease
    api_instance.get_disease_substance_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_substance_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disease_substance_associations_0**
> get_disease_substance_associations_0(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns substances associated with a disease
    api_instance.get_disease_substance_associations_0(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_disease_substance_associations_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_object**
> get_environment_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns environment entity

TODO consider renaming exposure

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns environment entity
    api_instance.get_environment_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_environment_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_phenotype_associations**
> list[Association] get_environment_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns list of associations

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns list of associations
    api_response = api_instance.get_environment_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_environment_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_disease_associations**
> AssociationResults get_gene_disease_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns diseases associated with gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750, Orphanet:173505. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns diseases associated with gene
    api_response = api_instance.get_gene_disease_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750, Orphanet:173505. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_expression_associations**
> AssociationResults get_gene_expression_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns expression events for a gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns expression events for a gene
    api_response = api_instance.get_gene_expression_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_expression_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_function_associations**
> AssociationResults get_gene_function_associations(id, use_compact_associations=use_compact_associations, homology_type=homology_type, homolog_taxon=homolog_taxon, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns function associations for a gene

IMPLEMENTATION DETAILS ----------------------  Note: currently this is implemented as a query to the GO/AmiGO solr instance. This directly supports IDs such as:   - ZFIN e.g. ZFIN:ZDB-GENE-050417-357  Note that the AmiGO GOlr natively stores MGI annotations to MGI:MGI:nn. However, the standard for biolink is MGI:nnnn, so you should use this (will be transparently mapped to legacy ID)  Additionally, for some species such as Human, GO has the annotation attached to the UniProt ID. Again, this should be transparently handled; e.g. you can use NCBIGene:6469, and this will be mapped behind the scenes for querying.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
homology_type = 'homology_type_example' # str | P, O or LDO (paralog, ortholog or least-diverged). (optional)
homolog_taxon = 'homolog_taxon_example' # str | Taxon CURIE of homolog, e.g. NCBITaxon:9606. Can be intermediate note, includes inferred by default (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns function associations for a gene
    api_response = api_instance.get_gene_function_associations(id, use_compact_associations=use_compact_associations, homology_type=homology_type, homolog_taxon=homolog_taxon, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_function_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **homology_type** | **str**| P, O or LDO (paralog, ortholog or least-diverged). | [optional] 
 **homolog_taxon** | **str**| Taxon CURIE of homolog, e.g. NCBITaxon:9606. Can be intermediate note, includes inferred by default | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_homolog_associations**
> AssociationResults get_gene_homolog_associations(id, use_compact_associations=use_compact_associations, homology_type=homology_type, homolog_taxon=homolog_taxon, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns homologs for a gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
homology_type = 'homology_type_example' # str | P, O or LDO (paralog, ortholog or least-diverged). (optional)
homolog_taxon = 'homolog_taxon_example' # str | Taxon CURIE of homolog, e.g. NCBITaxon:9606. Can be intermediate note, includes inferred by default (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns homologs for a gene
    api_response = api_instance.get_gene_homolog_associations(id, use_compact_associations=use_compact_associations, homology_type=homology_type, homolog_taxon=homolog_taxon, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_homolog_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **homology_type** | **str**| P, O or LDO (paralog, ortholog or least-diverged). | [optional] 
 **homolog_taxon** | **str**| Taxon CURIE of homolog, e.g. NCBITaxon:9606. Can be intermediate note, includes inferred by default | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_interactions**
> AssociationResults get_gene_interactions(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns interactions for a gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns interactions for a gene
    api_response = api_instance.get_gene_interactions(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_object**
> list[Gene] get_gene_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns gene object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:84570
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns gene object
    api_response = api_instance.get_gene_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:84570 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_phenotype_associations**
> AssociationResults get_gene_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns phenotypes associated with gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns phenotypes associated with gene
    api_response = api_instance.get_gene_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene_publication_list**
> AssociationResults get_gene_publication_list(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns expression events for a gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns expression events for a gene
    api_response = api_instance.get_gene_publication_list(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_gene_publication_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_geneproduct_object**
> get_geneproduct_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns gene product object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns gene product object
    api_instance.get_geneproduct_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_geneproduct_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_associations**
> AssociationResults get_generic_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations for an entity regardless of the type

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations for an entity regardless of the type
    api_response = api_instance.get_generic_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_generic_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_object**
> list[BioObject] get_generic_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns object of any type

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | id, e.g. NCBIGene:84570
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns object of any type
    api_response = api_instance.get_generic_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_generic_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id, e.g. NCBIGene:84570 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[BioObject]**](BioObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_disease_associations**
> AssociationResults get_genotype_disease_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns diseases associated with a genotype

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286 (if non-human will return models)
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns diseases associated with a genotype
    api_response = api_instance.get_genotype_disease_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286 (if non-human will return models) | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_gene_associations**
> AssociationResults get_genotype_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns genes associated with a genotype

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns genes associated with a genotype
    api_response = api_instance.get_genotype_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_genotype_associations**
> AssociationResults get_genotype_genotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns genotypes-genotype associations

Genotypes may be related to one another according to the GENO model

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns genotypes-genotype associations
    api_response = api_instance.get_genotype_genotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_object**
> list[Genotype] get_genotype_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns genotype object

The genotype object will have the following association sets populated:   * gene  * phenotype  * disease

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns genotype object
    api_response = api_instance.get_genotype_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Genotype]**](Genotype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_genotype_phenotype_associations**
> AssociationResults get_genotype_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns phenotypes associated with a genotype

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns phenotypes associated with a genotype
    api_response = api_instance.get_genotype_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_genotype_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goterm_gene_associations**
> AssociationResults get_goterm_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associated genes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associated genes
    api_response = api_instance.get_goterm_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_goterm_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goterm_object**
> get_goterm_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns GO class object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | GO class CURIE identifier, e.g GO:0016301 (kinase activity)
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns GO class object
    api_instance.get_goterm_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_goterm_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GO class CURIE identifier, e.g GO:0016301 (kinase activity) | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goterm_phenotype_associations**
> list[Association] get_goterm_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associated phenotypes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associated phenotypes
    api_response = api_instance.get_goterm_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_goterm_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_literature_disease_associations**
> list[Association] get_literature_disease_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations between a lit entity and a disease

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations between a lit entity and a disease
    api_response = api_instance.get_literature_disease_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_literature_disease_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_literature_gene_associations**
> list[Association] get_literature_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations between a lit entity and a gene

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations between a lit entity and a gene
    api_response = api_instance.get_literature_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_literature_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_literature_genotype_associations**
> list[Association] get_literature_genotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations between a lit entity and a genotype

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations between a lit entity and a genotype
    api_response = api_instance.get_literature_genotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_literature_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_object**
> get_parent_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns individual

Individuals may typically encompass patients, but can be individuals of any species

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns individual
    api_instance.get_parent_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_parent_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_object_0**
> get_parent_object_0(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns investigation object

Investigations encompass clinical trials, molecular biology experiments or any kind of study

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns investigation object
    api_instance.get_parent_object_0(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_parent_object_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pathway_gene_associations**
> list[Association] get_pathway_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns list of genes associated with a pathway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns list of genes associated with a pathway
    api_response = api_instance.get_pathway_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pathway_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pathway_object**
> get_pathway_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns pathway object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE any pathway element. May be a GO ID or a pathway database ID
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns pathway object
    api_instance.get_pathway_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pathway_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE any pathway element. May be a GO ID or a pathway database ID | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pathway_participant_associations**
> list[Association] get_pathway_participant_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations to participants (molecules, etc) for a pathway

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations to participants (molecules, etc) for a pathway
    api_response = api_instance.get_pathway_participant_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pathway_participant_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_anatomy_associations**
> list[NamedObject] get_phenotype_anatomy_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns anatomical entities associated with a phenotype

Example IDs:   * ZP:0004204   * MP:0008521 abnormal Bowman membrane  For example, *abnormal limb development* will map to *limb*

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns anatomical entities associated with a phenotype
    api_response = api_instance.get_phenotype_anatomy_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_anatomy_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[NamedObject]**](NamedObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_function_associations**
> list[Association] get_phenotype_function_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns biological functions associated with a Phenotype

This may come from a combination of asserted knowledge (e.g. abnormal levels of metabolite to corresponding GO activity) or from data-driven approach (cf Translator)  Results are typically represented as GO classes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns biological functions associated with a Phenotype
    api_response = api_instance.get_phenotype_function_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_function_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_gene_associations**
> get_phenotype_gene_associations(id, taxid, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns gene ids for all genes for a particular phenotype in a taxon

For example, + NCBITaxon:10090 (mouse)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
taxid = 'taxid_example' # str | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns gene ids for all genes for a particular phenotype in a taxon
    api_instance.get_phenotype_gene_associations(id, taxid, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | 
 **taxid** | **str**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_gene_associations_0**
> list[Association] get_phenotype_gene_associations_0(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associated phenotypes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associated phenotypes
    api_response = api_instance.get_phenotype_gene_associations_0(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_gene_associations_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_object**
> get_phenotype_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns phenotype class object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns phenotype class object
    api_instance.get_phenotype_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phenotype_phenotype_associations**
> list[Association] get_phenotype_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associated phenotypes

Includes phenologs, as well as equivalent phenotypes in other species

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associated phenotypes
    api_response = api_instance.get_phenotype_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_phenotype_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pub_object**
> get_pub_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns publication object

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns publication object
    api_instance.get_pub_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_pub_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_feature_object**
> get_sequence_feature_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns seqfeature

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns seqfeature
    api_instance.get_sequence_feature_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_sequence_feature_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_exposures**
> list[Association] get_substance_exposures(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations between a substance and related exposures

E.g. between pesticide and occupational exposure class

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations between a substance and related exposures
    api_response = api_instance.get_substance_exposures(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_exposures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_interactions**
> list[Association] get_substance_interactions(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations between given drug and interactions

Interactions can encompass drugs or environments

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations between given drug and interactions
    api_response = api_instance.get_substance_interactions(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_interactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_object**
> list[Substance] get_substance_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns substance entity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns substance entity
    api_response = api_instance.get_substance_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Substance]**](Substance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_participant_in_associations**
> list[Association] get_substance_participant_in_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations between an activity and process and the specified substance

Examples relationships:   * substance is a metabolite of a process  * substance is synthesized by a process  * substance is modified by an activity  * substance elicits a response program/pathway  * substance is transported by activity or pathway  For example, CHEBI:40036 (amitrole)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations between an activity and process and the specified substance
    api_response = api_instance.get_substance_participant_in_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_participant_in_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_relationships**
> list[Association] get_substance_relationships(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations between a substance and other substances

E.g. metabolite-of, tautomer-of, parent-of, ...

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations between a substance and other substances
    api_response = api_instance.get_substance_relationships(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_role_associations**
> list[Association] get_substance_role_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns associations between given drug and roles

Roles may be human-oriented (e.g. pesticide) or molecular (e.g. enzyme inhibitor)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns associations between given drug and roles
    api_response = api_instance.get_substance_role_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_role_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_substance_target_associations**
> list[Association] get_substance_target_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns associations between given drug and targets

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | 
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns associations between given drug and targets
    api_response = api_instance.get_substance_target_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_substance_target_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**list[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_gene_associations**
> AssociationResults get_variant_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns genes associated with a variant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns genes associated with a variant
    api_response = api_instance.get_variant_gene_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_gene_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_genotype_associations**
> AssociationResults get_variant_genotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns genotypes associated with a variant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns genotypes associated with a variant
    api_response = api_instance.get_variant_genotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_genotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_object**
> get_variant_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

TODO Returns sequence variant entity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # TODO Returns sequence variant entity
    api_instance.get_variant_object(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variant_phenotype_associations**
> AssociationResults get_variant_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)

Returns phenotypes associated with a variant

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BioentityApi()
id = 'id_example' # str | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
use_compact_associations = true # bool | If true, returns results in compact associations format (optional)
unselect_evidence = true # bool | If set, excludes evidence objects in response (optional)
exclude_automatic_assertions = true # bool | If set, excludes associations that involve IEAs (ECO:0000501) (optional)
slim = ['slim_example'] # list[str] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID (optional)
rows = 20 # int | number of rows (optional) (default to 20)
evidence = 'evidence_example' # str | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      (optional)
fetch_objects = true # bool | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload (optional) (default to true)

try: 
    # Returns phenotypes associated with a variant
    api_response = api_instance.get_variant_phenotype_associations(id, use_compact_associations=use_compact_associations, unselect_evidence=unselect_evidence, exclude_automatic_assertions=exclude_automatic_assertions, slim=slim, rows=rows, evidence=evidence, fetch_objects=fetch_objects)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BioentityApi->get_variant_phenotype_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **use_compact_associations** | **bool**| If true, returns results in compact associations format | [optional] 
 **unselect_evidence** | **bool**| If set, excludes evidence objects in response | [optional] 
 **exclude_automatic_assertions** | **bool**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] 
 **slim** | [**list[str]**](str.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **rows** | **int**| number of rows | [optional] [default to 20]
 **evidence** | **str**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 
 **fetch_objects** | **bool**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to true]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

