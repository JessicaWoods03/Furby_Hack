from abc import ABC, abstractmethod
from typing import Dict, Any

# Common interface that defines all logical flows in the three main pipelines
# Geography, Medical, environment pipelines
# Between Exploring_Extracting_Data_Entry_Point.ipynb and Node_Relationship_Processing.ipynb those
# where used as guildlines to understand the data we are working with and build pipelines to take on
# that data dynamically reguardless of the subject matter.

# this is subject to change but will do for now.
 
class SemanticPipeline(ABC):
    
    @abstractmethod
    def pre_clean_wiki_entries(self, raw_text: str) -> str:
        """
        Clean the raw text wiki entries by removing irrelevant data
        Return cleaned plain text.
        """
        pass
    
    @abstractmethod
    def select_best_entry(self, entries: List[Dict])-> Dict:
        
        """
        Given multiple candidate entries, select the best one based on 
        domain-specific logic (e.g. highest correlation score)
        """
        pass
    
    @abstractmethod
    def clean_data(self, raw_text:str) -> List[str]:
        """
        Preprocess raw text input into clean subunits (sentences, phrases, concepts)
        """
        pass

    @abstractmethod
    def embed_node(self, node_text: str)-> Any:
        """
        Returns and embedding for a node level or concept
        """
        pass
    
    @abstractmethod
    def semantic_to_ontology_type(self, label:str)-> str|None:
        pass

    @abstractmethod
    def build_graph(self, parent_child_structure: Dict[str, Dict[str,list]]}-> Dict[str, Any]:
        """
        Constructs a semantic graph from parent-child mappings.
        Returns a dict with:
        -'nodes': Dict[str, Dict] where each key is a node ID
        -'edges': List[Dict] with source, target, and relation
        """
        pass
