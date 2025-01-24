import streamlit as st
import spacy
from spacy import displacy

# Load spaCy models
MODEL_OPTIONS = {
    "Small (en_core_web_sm)": "en_core_web_sm",
    "Medium (en_core_web_md)": "en_core_web_md",
    "Large (en_core_web_lg)": "en_core_web_lg"
}

# Streamlit app UI
st.title("Named Entity Recognition (NER) App")
st.write("Enter text and select a model to analyze named entities.")

# Sidebar - model selection
selected_model_name = st.sidebar.selectbox("Choose a spaCy model:", list(MODEL_OPTIONS.keys()))
selected_model = MODEL_OPTIONS[selected_model_name]

# Load selected spaCy model
@st.cache_resource
def load_model(model_name):
    return spacy.load(model_name)

nlp = load_model(selected_model)

# Text input area
text_input = st.text_area("Enter your text here:", "Apple is looking at buying a startup in London for $1 billion.")

# Process the text and display NER visualization
if st.button("Analyze"):
    doc = nlp(text_input)
    
    # Convert entities to spaCy's displacy format
    html = displacy.render(doc, style="ent", page=False)
    
    # Render NER output
    st.subheader("Named Entity Recognition (NER) Visualization")
    st.write("Below is the visualization of named entities detected in your text:")
    st.components.v1.html(html, height=300, scrolling=True)

    # Show extracted entities in table format
    st.subheader("Extracted Entities")
    entity_data = [(ent.text, ent.label_) for ent in doc.ents]
    
    if entity_data:
        st.table(entity_data)
    else:
        st.write("No entities detected.")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit and spaCy.")
