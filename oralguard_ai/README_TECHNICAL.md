# Technical Architecture & System Flow — OralGuard AI

This document explains the **technical workflow, data flow diagrams (DFDs), and internal system logic** of OralGuard AI.

---

## 🔁 System Flow (High-Level)

User → Web Interface → Backend API → AI Model → Prediction → User

---

## 📊 Data Flow Diagram (DFD – Level 1)

1. **User**
   - Uploads oral cavity image

2. **Frontend (Prototype)**
   - Sends image to backend via REST API

3. **Backend (FastAPI)**
   - Receives image
   - Validates format
   - Preprocesses image

4. **AI Model (CNN)**
   - Performs inference
   - Outputs class probabilities

5. **Backend**
   - Converts probabilities to readable labels
   - Adds confidence score

6. **User**
   - Receives result with disclaimer

---

## 🧠 Model Workflow

Image (RGB)
→ Resize (224×224)
→ Normalization (0–1)
→ CNN Feature Extraction
→ Softmax Classification
→ Output Class & Confidence

---

## ⚙️ API Flow (`/predict`)

- Method: POST  
- Input: Image file (.jpg/.png)
- Output:
```json
{
  "prediction": "Premalignant",
  "confidence": 0.91,
  "disclaimer": "AI-based screening support only"
}
