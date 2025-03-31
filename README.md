## So What is this About ?

# 💭Problem Statement - TDS Solver - Project 2

You are a clever student who has joined IIT Madras’ Online Degree in Data Science. You have just enrolled in the Tools in Data Science course.

To make your life easier, you have decided to build an LLM-based application that can automatically answer any of the graded assignment questions.

Specifically, you are building and deploying an API that accepts any question from one of first 5 Graded Assignments.

###

## 🚀 **How to Run the App Locally?**  

### 🔹 **1. Clone the Project**  
First, download the project to your local machine:  
```bash
git clone https://github.com/IndianAccentDev/IITM-TDS-Project2.git
cd IITM-TDS-Project
```  

### 🔹 **2. Set Up a Virtual Environment**  
Create and activate a virtual environment:  
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
or use `uv`:  
```bash
uv venv
source venv/bin/activate
```  

### 🔹 **3. Install Dependencies**  
Install required packages:  
```bash
pip install -r requirements.txt
```  
or with `uv`:  
```bash
uv pip install -r requirements.txt
```  

### 🔹 **4. Set Up Environment Variables**  
Create a `.env` file and add your API key:  
```env
API_Key=your_openai_api_key
```  

### 🔹 **5. Run the App**  
Start the Flask server:  
```bash
python -m api.app
```  
The app runs at **http://127.0.0.1:5000** 🎉  

### 🔹 **6. Test the API**  
Use `curl` or Postman to send a request:  
```bash
curl -X POST "http://127.0.0.1:5000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=What is the output of code -s in VS Code?"
```  

---

## 🤖 **How It Works?**  
1️⃣ **User asks a question** (optionally uploads a file 📂).  
2️⃣ API **matches** the question to a predefined response.  
3️⃣ If needed, it extracts details using **AI (OpenAI)** 🧠.  
4️⃣ Calls the **correct function** to get the answer.  
5️⃣ Returns the answer in JSON format {}

Example response:  
```json
{ "answer": "VS Code version 1.52.1" }
```  