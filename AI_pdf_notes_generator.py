from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel 
from dotenv import load_dotenv
import fitz  # pymupdf
import streamlit as st

def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text
load_dotenv()

llm1= HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Pro',
    task='text-generation'
)

llm2 = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-72B-Instruct',
    task='text-generation'
)

model1= ChatHuggingFace(
    llm=llm1
)

model2=ChatHuggingFace(
    llm=llm2
)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2= PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']

)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
}
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

# ----------------------------
# STREAMLIT UI
# ----------------------------

st.set_page_config(page_title="AI PDF Notes Generator", layout="wide")

st.title("📚 AI PDF Notes + Quiz Generator")
st.write("Upload a PDF and get AI-generated notes, quiz, and summary")

pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

if pdf_file:
    with st.spinner("Reading PDF..."):
        text = extract_text_from_pdf(pdf_file)

    st.success("PDF loaded successfully!")

    if st.button("Generate Notes + Quiz"):
        with st.spinner("AI is thinking..."):
            result = chain.invoke({"text": text})

        st.subheader("📄 Final Output")
        st.write(result)