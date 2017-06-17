# Gene

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
**description** | **str** | full text description | [optional] 
**consider** | **list[str]** |  | [optional] 
**xrefs** | **list[str]** | Database cross-references. These are usually CURIEs, but may also be URLs. E.g. ENSEMBL:ENSG00000099940  | [optional] 
**taxon** | [**Taxon**](Taxon.md) | Taxon to which the object belongs | [optional] 
**transcripts** | [**list[Transcript]**](Transcript.md) | All transcripts belonging to this gene | [optional] 
**sequence_features** | [**list[SequenceFeature]**](SequenceFeature.md) | Sequence feature representing particular instance on a genome | [optional] 
**function_associations** | [**list[Association]**](Association.md) | GO assocations for wild type gene | [optional] 
**chromosome** | [**Chromosome**](Chromosome.md) | chromosome on which this gene is located. This may be redundant with information in sequence_feature objects but is included here for convenience | [optional] 
**full_name** | **str** | full name, e.g. Synaptosome Associated Protein 29 | [optional] 
**homology_associations** | [**list[Association]**](Association.md) | orthology and paralogy assocations for this gene | [optional] 
**pathway_associations** | [**list[Association]**](Association.md) | Assocations to pathways in which this gene is involved, including LEGO models | [optional] 
**literature_associations** | [**list[Association]**](Association.md) | publications for this gene | [optional] 
**interaction_associations** | [**list[Association]**](Association.md) | associations to genes that interact (may be physical or genetic) | [optional] 
**disease_associations** | [**list[Association]**](Association.md) | diseases associated with alterations of gene | [optional] 
**phenotype_associations** | [**list[Association]**](Association.md) | phenotypes associated with alterations of gene | [optional] 
**summaries** | [**list[SummaryPropertyValue]**](SummaryPropertyValue.md) | Attributed textual summaries | [optional] 
**genotype_associations** | [**list[Association]**](Association.md) | associations to genotypes in which this gene is altered | [optional] 
**families** | [**list[NamedObject]**](NamedObject.md) | Families, superfamilies etc to which these gene belongs | [optional] 
**systematic_name** | **str** | E.g. SPBC428.08c for clr4 in PomBase | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


