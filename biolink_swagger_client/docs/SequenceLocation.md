# SequenceLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **list[str]** |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**replaced_by** | **list[str]** |  | [optional] 
**synonyms** | [**list[SynonymPropertyValue]**](SynonymPropertyValue.md) | list of synonyms or alternate labels | [optional] 
**label** | **str** | RDFS Label | [optional] 
**deprecated** | **bool** | True if the node is deprecated/obsoleted. | [optional] 
**id** | **str** | ID or CURIE e.g. MGI:1201606 | [optional] 
**description** | **str** | Descriptive text for the entity. For ontology classes, this will be a definition. | [optional] 
**consider** | **list[str]** |  | [optional] 
**xrefs** | **list[str]** | Database cross-references. These are usually CURIEs, but may also be URLs. E.g. ENSEMBL:ENSG00000099940  | [optional] 
**taxon** | [**Taxon**](Taxon.md) | Taxon to which the object belongs | [optional] 
**start** | [**SequencePosition**](SequencePosition.md) |  | [optional] 
**end** | [**SequencePosition**](SequencePosition.md) |  | [optional] 
**strand** | **int** | Strand direction: 1&#x3D;&#x3D;&#39;+&#39;, -1&#x3D;&#x3D;&#39;-&#39;, 0 or null infers unknown. | [optional] 
**phase** | **int** |  | [optional] 
**score** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


