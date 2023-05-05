import gradio as gr
import sys
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI

from llama_index import PromptHelper, LLMPredictor, SimpleDirectoryReader, GPTVectorStoreIndex, load_index_from_storage, \
    StorageContext, ServiceContext

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

def construct_index(directory_path):
    service_context = __create_service_context()
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    index.storage_context.persist()
    return index


def __create_service_context():
    # define prompt helper
    # set maximum input size
    max_input_size = 2048
    # set number of output tokens
    num_output = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=1))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor,
                                                   prompt_helper=prompt_helper,
                                                   )
    return service_context


def chatbot(input_text):
    storage_context = StorageContext.from_defaults(persist_dir='./storage',)
    service_context = __create_service_context()

    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(service_context=service_context,)
    response = query_engine.query(input_text)
    return response.response


iface = gr.Interface(fn=chatbot, inputs=gr.inputs.Textbox(lines=7, label="Enter your text"), outputs="text",
                     title="Custom-trained Al Chatbot")

# index = construct_index("docs")
iface.launch(share=True)