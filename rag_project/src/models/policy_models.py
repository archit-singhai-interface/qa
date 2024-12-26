from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class PolicyEvaluationResult:
    """
    Represents the result of a comprehensive policy evaluation.
    
    Attributes:
        query (str): The original query
        retrieved_docs (List[Dict[str, str]]): List of retrieved documents
        metrics (Dict[str, float]): Evaluation metrics
    """
    query: str
    retrieved_docs: List[Dict[str, str]] = field(default_factory=list)
    metrics: Dict[str, float] = field(default_factory=dict)

@dataclass
class RAGEvaluationResults:
    """
    Comprehensive results from RAG system evaluation.
    
    Attributes:
        query_evaluations (List[PolicyEvaluationResult]): Detailed evaluation for each query
        overall_metrics (Dict[str, float]): Aggregated metrics across all queries
    """
    query_evaluations: List[PolicyEvaluationResult] = field(default_factory=list)
    overall_metrics: Dict[str, float] = field(default_factory=dict)

    def add_query_evaluation(self, evaluation: PolicyEvaluationResult):
        """
        Add a query evaluation to the results.
        
        Args:
            evaluation (PolicyEvaluationResult): Evaluation result to add
        """
        self.query_evaluations.append(evaluation)

    def calculate_overall_metrics(self):
        """
        Calculate overall metrics from individual query evaluations.
        """
        if not self.query_evaluations:
            return

        # Initialize metrics dictionary
        self.overall_metrics = {
            metric: sum(
                eval.metrics.get(metric, 0) 
                for eval in self.query_evaluations
            ) / len(self.query_evaluations)
            for metric in set().union(*(eval.metrics.keys() for eval in self.query_evaluations))
        }
