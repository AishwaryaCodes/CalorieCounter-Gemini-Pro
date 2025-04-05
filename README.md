# 🥗 Calorie Counter AI 🍱

An AI-powered nutrition assistant built with **Streamlit** and **Gemini 1.5 Pro** that estimates the calorie count of meals from images. Upload a photo of your food, and get a breakdown of food items, estimated calories, and a health assessment, all using Google’s powerful multimodal AI.

---

## 🚀 Live Demo

👉 [Try the App](https://caloriecounter-gemini-pro-v3cgaybvyvagb945mxebtd.streamlit.app/)

---

## 🧠 Features

- 📷 Upload an image of a meal or food item
- 🔎 Gemini 1.5 Pro processes the image and analyzes food contents
- 🧾 Get per-item calorie estimates and total calorie count
- ✅ Nutritional feedback on whether the food is healthy
- 💡 Built using Python, Streamlit, Gemini Pro API, and PIL

---

## 📁 Folder Structure

```
calorie-counter-ai/
│
├── app.py              # Streamlit app code
├── .env                # Environment variables (not committed)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Tech Stack
- Frontend/UI: Streamlit

- AI Model: Google Gemini 1.5 Pro (Multimodal)

- Language: Python

- Image Processing: Pillow (PIL)

- Environment Management: python-dotenv

---

## Future Improvements

 - Add support for multiple image uploads

 - Save meal history for logged-in users

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/calorie-counter-ai.git
cd calorie-counter-ai

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

GOOGLE_API_KEY=your_api_key_here

streamlit run app.py

```


