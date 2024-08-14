# 🧬 Pneumonia Classification 🧬

This project features an AI model for diagnosing pneumonia from chest X-ray images. Users can upload a chest X-ray image through the app, and the model will classify it.

## 🚀 Features

- **AI Model**: A CNN (Convolutional Neural Network) model trained using Keras.
- **User Interface**: A simple and intuitive web interface built with Streamlit.
- **Visual Feedback**: Classification results are displayed immediately below the uploaded image.
- **Background Image**: The application uses a custom background image.

## 🛠 Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/username/Image-Classification-WebApp.git
    ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    streamlit run main.py
    ```
# 🗃️ Data

- **Data:** https://data.mendeley.com/datasets/rscbjbr9sj/2
- **License:** CC BY 4.0
- **Citation:** http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5

## 📂 File Structure

- **app.py**: The main application file.
- **model/**: Directory containing the trained model and class labels.
- **bgs/**: Directory with background images for the app.
- **util.py**: File containing utility functions.

## 📊 Usage

1. After starting the app, upload a chest X-ray image on the webpage that opens in your browser.
2. The model will analyze the image and display the classification result.
3. The result will show as either "Normal" or "Pneumonia", along with a confidence score.

## 📝 License

This project is licensed under the MIT License. 

---

Thank you and happy coding! 😊
