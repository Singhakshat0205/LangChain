from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st


llm= HuggingFacePipeline.from_model_id(
    model_id='meta-llama/Llama-3.1-8B-Instruct',
    task= 'text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_token=100
    )
)


model= ChatHuggingFace(llm=llm)


paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


st.header('Research Tool')
user_input= st.text_input('Enter your prompt')

if st.button('Summarize'):
    result= model.invoke(user_input)
    st.write(result.content)



