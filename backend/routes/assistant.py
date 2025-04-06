@router.post("/chatbot")
def chat_with_bot(query: str):
    response = answer_question(query)
    return {"response": response}
