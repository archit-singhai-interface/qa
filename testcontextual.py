from rag import PolicyAnalyzer

analyzer = PolicyAnalyzer("/home/dumball/Downloads/interface-qa-bot-main/server/bot/data/policies")
print(analyzer.load_stored_summaries())
