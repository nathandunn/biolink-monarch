# Association

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_extension** | [**list[AnnotationExtension]**](AnnotationExtension.md) |  | [optional] 
**slim** | **list[str]** | Objects mapped to a slim | [optional] 
**publications** | [**list[Publication]**](Publication.md) | Publications supporting association, extracted from evidence graph | [optional] 
**object** | [**BioObject**](BioObject.md) | Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330 | [optional] 
**id** | **str** | Association/annotation unique ID | [optional] 
**type** | **str** | Type of association, e.g. gene-phenotype | [optional] 
**evidence_graph** | [**Graph**](Graph.md) | An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object | [optional] 
**subject** | [**BioObject**](BioObject.md) | Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606 | [optional] 
**provided_by** | **list[str]** | Provider of association, e.g. Orphanet, ClinVar | [optional] 
**relation** | [**Relation**](Relation.md) | Relationship type connecting subject and object | [optional] 
**qualifiers** | [**list[AssociationPropertyValue]**](AssociationPropertyValue.md) |  | [optional] 
**object_extension** | [**list[AnnotationExtension]**](AnnotationExtension.md) |  | [optional] 
**evidence_types** | [**list[NamedObject]**](NamedObject.md) | Evidence types (ECO classes) extracted from evidence graph | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


