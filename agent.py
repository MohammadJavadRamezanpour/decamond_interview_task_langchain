from langgraph.graph import StateGraph
from nodes import input_node, processing_node, recommendation_node

builder = StateGraph(state_schema=dict) 

builder.add_node("input", input_node)
builder.add_node("process", processing_node)
builder.add_node("recommend", recommendation_node)

builder.set_entry_point("input")
builder.add_edge("input", "process")
builder.add_edge("process", "recommend")
builder.set_finish_point("recommend")

graph = builder.compile()
