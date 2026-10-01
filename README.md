\# 🌱 AgriIntel



\### AI-Powered Crop Disease Detection \& Agricultural Intelligence



AgriIntel is an AI-powered agricultural assistant that combines \*\*computer vision with real-time web search\*\* to help identify crop diseases and provide current agricultural information.



The system analyzes a crop or leaf image using a trained \*\*YOLO classification model\*\*, identifies the crop disease or condition, and then uses \*\*SerpApi\*\* to retrieve current agricultural information and relevant sources.



\---



\## 🚜 Problem



Crop diseases can significantly affect agricultural productivity. Farmers may have difficulty identifying diseases early and finding reliable, current information about disease management.



AgriIntel aims to provide a simple workflow:



\*\*Upload a crop image → Detect the disease → Find current agricultural information → Get management suggestions\*\*



\---



\## 💡 Solution



AgriIntel combines two components:



\### 1. AI Disease Detection



A trained YOLO model analyzes the uploaded crop or leaf image and predicts:



\- Crop

\- Disease / condition

\- Prediction confidence

\- Other possible conditions from the same crop



\### 2. Agricultural Intelligence using SerpApi



After detecting the disease, AgriIntel uses \*\*SerpApi\*\* to search for current agricultural information related to the detected crop and disease.



The retrieved results are filtered and ranked to prioritize relevant agricultural sources.



The application then presents:



\- Management information

\- Practical actions

\- Current agricultural sources

\- Source links for further reading



\---



\## 🔄 How It Works



```text

&#x20;               Crop / Leaf Image

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │   YOLO Model    │

&#x20;             │ Disease         │

&#x20;             │ Classification  │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;             Crop + Disease

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │    SerpApi      │

&#x20;             │ Current Web     │

&#x20;             │ Search          │

&#x20;             └────────┬────────┘

&#x20;                      │

&#x20;                      ▼

&#x20;            Relevant Agriculture

&#x20;                 Information

&#x20;                      │

&#x20;                      ▼

&#x20;             ┌─────────────────┐

&#x20;             │   AgriIntel     │

&#x20;             │ Management      │

&#x20;             │ Suggestions     │

&#x20;             │ Source Links    │

&#x20;             └─────────────────┘

