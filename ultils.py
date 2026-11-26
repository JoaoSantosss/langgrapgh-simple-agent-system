from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage

class State(TypedDict):
    messages: Annotated[list[HumanMessage], add_messages]

def user_input(state: State) -> State:
    query = input("Question: ")
    print(f"\nReceived query: {query}")

    if isinstance(query, str) and query.strip():
        return {"messages": [HumanMessage(content=query)]}
    else:
        raise ValueError("Query needs to be a non-empty string.")

def response_processing(state: State) -> State: 
   query = state["messages"][-1].content
   print(f"\nState on response processing: {state}")

   if isinstance(query, str) and query.strip(): 
      response = f"\nThe answer to your question '{query}' is: [simulated answer]\n"
      print(f"genereted response: {response}")
      return {"messages" : [response]}
   else:
      raise ValueError("Query needs to be a non-empty string.")

def output_response(state: State) -> State:
    print(f"State on output function: {state}")
    print(state["messages"][-1])
    return state