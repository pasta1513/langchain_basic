from langchain_core.messages import HumanMessage, AIMessage

history: list = []
_store: dict[str, list] = {}

def get_history(userid: str) -> list:
    return _store.setdefault(userid, [])

def add_turn(userid: str, human_msg: str, ai_msg: str) -> None:
    history = get_history(userid)
    history.append(HumanMessage(content=human_msg))
    history.append(AIMessage(content=ai_msg))