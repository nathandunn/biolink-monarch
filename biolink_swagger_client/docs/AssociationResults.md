# AssociationResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | Cursor position | [optional] 
**num_found** | **int** | total number of associations matching query | [optional] 
**facet_pivot** | **object** | Populated in facet_pivots is passed | [optional] 
**facet_counts** | **object** | Mapping between field names and association counts | [optional] 
**associations** | [**list[Association]**](Association.md) | Complete representation of full association object, plus evidence | [optional] 
**compact_associations** | [**list[CompactAssociationSet]**](CompactAssociationSet.md) | Compact representation in which objects (e.g. phenotypes) are collected for subject-predicate pairs | [optional] 
**objects** | **list[str]** | List of distinct objects used | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


