To locally run:

1. create virtual env: python -m venv venv
2. activate: source venv/bin/activate
3. pip install -r requirements.txt
4. download Ollama from ollama.com for local runs of models
5. download llama3.2 (smaller model with good performance - https://ollama.com/library/llama3.2)
   - ollama pull llama3.2
6. download embedding model (used to embed documents for our vector store)
   - ollama pull mxbai-embed-large
7. to verify model downloads: ollama list
