from langgraph.graph import StateGraph, START, END
from IPython.display import Image
from ultils import *

graph = StateGraph(State)

graph.add_node("input", user_input)
graph.add_node("processing", response_processing)
graph.add_node("output", output_response)

graph.add_edge(START, "input")
graph.add_edge("input", "processing")
graph.add_edge("processing", "output")
graph.add_edge("output", END)

compiled = graph.compile()

while True:
    compiled.invoke({"messages": [HumanMessage(content="How can I help you?")]})
    continue_conversation = input("Do you want to continue? (y/n)")
    if continue_conversation.lower() != "s":
        break

Image(compiled.get_graph().draw_mermaid_png())