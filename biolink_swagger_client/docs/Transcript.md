# Transcript

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
**exons** | [**list[Exon]**](Exon.md) | All exons used in this transcript | [optional] 
**cds** | [**list[CDS]**](CDS.md) | All cds used in this transcript | [optional] 
**sequence_features** | [**list[SequenceFeature]**](SequenceFeature.md) | Sequence feature representing this particular instance on a genome | [optional] 
**genes** | [**list[EntityReference]**](EntityReference.md) | References to any gene objects that have this transcript. This may not be populated if this is contained in a gene object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


