import streamlit as st
from keras.models import load_model
from PIL import Image
from util import classify, set_background

set_background('./bgs/bg2.jpg')

# title
st.title('🧬 Pneumonia classification 🧬')
st.title(' ')

# header
st.header('Please upload a chest X-ray image:')
st.markdown("<h5 style='color:gray;'><strong>* The results are below the picture.</strong></h5>", unsafe_allow_html=True)
# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/pneumonia_classifier.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()
print(class_names)

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("# {}".format(class_name))
    # st.write("### Score: {:.2%}".format(conf_score))
    st.markdown(f"<h3>Score: <span style='color:red;'>{conf_score:.2%}</span></h3>", unsafe_allow_html=True)
