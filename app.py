import streamlit as st
import os
import time
import tempfile
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from prompts import check_prompt, prompt, summarizer_prompt
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS 
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
groq_api_key = os.environ["GROQ_API_KEY"]

st.title("Know Your Paper Better!")
llm = ChatGroq(api_key=groq_api_key,
               model_name = "llama3-70b-8192")
pdf = st.file_uploader("Upload the Paper you want to know better (Only in PDF Formats)", type="pdf")

def vector_embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(pdf.read())
            temp_file_path = temp_file.name
        st.session_state.loader = PyPDFLoader(temp_file_path)
        st.session_state.documents = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.documents)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
def get_from_scihub():
    pass
def is_research_paper():
    documents_chain = create_stuff_documents_chain(llm, check_prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, documents_chain)
    check = retrieval_chain.invoke({"input": "Is this a research paper?"})
    return check["answer"]
def generate_summary():
    documents_chain = create_stuff_documents_chain(llm, summarizer_prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, documents_chain)
    summary = retrieval_chain.invoke({"input": "Generate the summary of the paper"})
    return summary["answer"]
input_prompt = st.text_input("Ask anything about the paper")
submit = st.button("Ask")
summarize = st.button("Summarize")
if submit and input_prompt:
    if pdf:
        vector_embeddings()
        ans = is_research_paper()
        if ans == "No":
            st.write("This is not a research paper please upload a research paper and try again")
        if ans == "Yes":
            st.write("Vectors generated")
            documents_chain = create_stuff_documents_chain(llm, prompt)
            retriever = st.session_state.vectors.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, documents_chain)
            start = time.process_time()
            response = retrieval_chain.invoke({"input":input_prompt})
            st.write("Response time : ", time.process_time()-start)
            st.write(response["answer"])
if summarize:
    if pdf:
        vector_embeddings()
        ans = is_research_paper()
        if ans == "No":
            st.write("This is not a research paper please upload a research paper and try again")
        if ans == "Yes":
            summary = generate_summary()
            st.write(summary)