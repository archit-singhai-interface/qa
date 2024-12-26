# RAG Policy Analysis Bot

## Overview
This Retrieval Augmented Generation (RAG) Bot is designed to analyze and retrieve information from policy documents using advanced natural language processing techniques.

## Features
- Document analysis and summarization
- Semantic search across policy documents
- Comprehensive evaluation of retrieval and answer generation
- Modular and extensible architecture

## Prerequisites
- Python 3.11+
- OpenAI API Key
- Langsmith API Key (Optional)

## Installation
1. Clone the repository
2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file with the following:
```
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key  # Optional
```

## Running the Application
```bash
python -m src.main
```

## Project Structure
```
rag_project/
├── src/
│   ├── config/         # Configuration settings
│   ├── models/         # Data models
│   ├── services/       # Core business logic
│   ├── utils/          # Utility functions
│   └── main.py         # Application entry point
├── tests/              # Unit and integration tests
├── data/               # Policy documents
├── logs/               # Application logs
├── requirements.txt
└── README.md
```

## Testing
Run tests using pytest:
```bash
pytest tests/
```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Specify your license]

## Contact
[Your contact information]
