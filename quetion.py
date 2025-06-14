class QA:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

qa_data = [
    QA("こんにちは", "こんにちは！ご質問はありますか？"),
    QA("あなたの名前", "私はミミだよ！あなたのAIアシスタントです。"),
    QA("何ができ", "私は質問に答えたり、情報を提供したりできますよ！"),
    QA("", "もちろんPythonです！"),
]

def dict_bot(question):
    # 完全一致を優先
    for qa in qa_data:
        if qa.question == question:
            return qa.answer
    # 部分一致（大文字小文字無視）
    q_lower = question.lower()
    for qa in qa_data:
        if qa.question.lower() in q_lower or q_lower in qa.question.lower():
            return qa.answer
    return "すみません、その質問にはまだ対応していません。"

def add_question(question, answer):
    """Add or update a question-answer pair in the database."""
    qa_data.append(QA(question, answer))

def remove_question(question):
    """Remove a question from the database."""
    global qa_data
    qa_data = [qa for qa in qa_data if qa.question != question]

def list_questions():
    """List all questions in the database."""
    return [qa.question for qa in qa_data]
