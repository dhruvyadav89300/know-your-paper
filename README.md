# know-your-paper

## Overview
This project enables users to interact with uploaded research papers, asking detailed questions and generating summaries. Developed to significantly reduce the time and effort required to understand complex research papers, it leverages Retrieval-Augmented Generation (RAG) technology, powered by the llama-3 Large Language Model (LLM) with 70 billion parameters for deep understanding and response accuracy. I used Groq AI inferencing, enhancing response times significantly. The user interface is built with Streamlit, providing a clean and user-friendly experience.

## Key Features
- **Interactive Q&A:** Ask detailed questions directly about the content of any uploaded research paper.
- **Summary Generation:** Get concise summaries of complex research documents to understand key points quickly.
- **High Performance:** Utilizes Groq's powerful processing capabilities for faster responses.
- **User-Friendly Interface:** Built with Streamlit for ease of use and accessibility.

## Technology Stack
- **LangChain:** Utilized to seamlessly integrate the LLM into the application, providing a framework for building language-based interactions.
- **Llama-3 LLM:** A cutting-edge 70 billion parameter model by Meta used for its powerful natural language processing capabilities. It processes user queries and generates insightful, context-aware responses.
- **OpenAI API:** Employs advanced algorithms to generate embeddings, which are crucial for the retrieval component of the RAG technology, enhancing the accuracy and relevance of information retrieval.
- **Streamlit:** Chosen for its simplicity and effectiveness, Streamlit forms the backbone of the user interface, making the application accessible and easy to use for all users.

## Instructions to run the application locally
### Clone this repository
### Create a .env file inside the cloned directory and add the following variables
    GROQ_API_KEY="Your Groq API key"
    OPENAI_API_KEY="Your OpenAI API key"
### Install the requirements.
    pip install -r requirements.txt
### Run the app.
    streamlit run main.py
## Future Scopes
- **Multilingual Support:** Adding support for papers written in multiple languages to cater to a global audience.
- **Enhanced Summary Customization:** Allowing users to specify the length or focus areas of the summaries generated. I also plan to fine-tune a model for this use case.
- **Integration with Academic Databases:** Automating the process of fetching papers directly from academic databases for analysis.
- **Full-Fledged Website Development:** Planning to develop a comprehensive website to host the project, enhancing user interaction and accessibility on a larger scale.
