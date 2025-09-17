# Deepfake Detection (Image, Audio, Video)

## 📌 Overview
Deepfakes use advanced AI techniques to manipulate media by swapping faces, altering voices, or generating entirely synthetic content. These manipulations are often indistinguishable to the human eye and ear, leading to potential misuse in spreading misinformation, identity theft, and cyber fraud.  

This project presents a **multi-modal deepfake detection system** capable of analyzing **images, audio, and video**. The system leverages **deep learning, feature extraction, and lightweight classification** techniques to distinguish between real and fake media.

---

## 🎯 Motivation
- **Rise in Deepfake Threats** – Growing misuse in politics, fraud, and social manipulation.  
- **Lack of Awareness** – Most people cannot differentiate real vs. synthetic media.  
- **Real-Time Harm Potential** – Deepfakes can incite violence, damage reputations, or impersonate individuals.  
- **Research Gap** – Few systems detect **all three types** (image, audio, video) under a unified framework.  

---

## 🛠️ System Architecture
1. **Input Layer** – User uploads image, audio, or video (via PyQt5 GUI).  
2. **Preprocessing** – Cleans input (resize images, denoise audio, frame extraction for video).  
3. **Feature Extraction** –  
   - Images → Gabor filters  
   - Audio → MFCC (Mel-Frequency Cepstral Coefficients)  
   - Video → Frame-by-frame analysis using image module  
4. **Classification Module** – Uses nearest-neighbor model for real/fake prediction.  
5. **Output Layer** – Displays **REAL** or **FAKE** with confidence score.  

---

## 🧮 Mathematical Model
- **Image Module** – Detects textures, edges, blurry areas, converts features into vectors.  
- **Audio Module** – Extracts pitch, tone, MFCC features, sums across clip.  
- **Video Module** – Analyzes frames individually, smooths predictions, detects frame inconsistencies.  

---

## 📑 Proposed Algorithm
1. Load media (image/audio/video).  
2. Preprocess input.  
3. Extract features (Gabor filters, MFCCs, frame vectors).  
4. Compare with dataset (nearest-neighbor).  
5. Decide REAL/FAKE using probability score / majority voting.  
6. Display result on GUI.  

---

## ⚡ Features
✅ Multi-modal detection (Image + Audio + Video)  
✅ User-friendly GUI (PyQt5)  
✅ Lightweight algorithms for faster detection  
✅ Works with small datasets  

---

## 📉 Limitations
- Limited dataset generalization  
- Manual retraining needed for new deepfake techniques  
- No real-time (live) detection yet  
- Nearest-neighbor less accurate than advanced deep models  

---

## 🖥️ System Requirements
**Software**  
- OS: Windows 10/11  
- Python 3.7+  
- Libraries: OpenCV, Librosa, PyQt5, NumPy, SciPy, TensorFlow/Keras  

**Hardware**  
- CPU: Intel i5 or higher  
- RAM: 8 GB+  
- Storage: 500 MB free  
- GPU: NVIDIA (4–6 GB VRAM, CUDA support recommended)  

---

## 📂 Project Workflow
- **Agile SDLC Model**  
  - Requirement Analysis → Planning → Development (sprints) → Testing → Integration → Deployment  
- Modules tested incrementally and integrated into final system.  

---

## 🚀 Future Scope
- Extend to **real-time detection** (camera & microphone streams).  
- Improve accuracy using **transformers & ensemble deep learning models**.  
- Create **mobile/web-based applications** for wider accessibility.  
- Develop **automated retraining pipelines** with latest datasets.  

---

## 👨‍💻 Authors
- Aditya Chavan (B400360548)  
- Varad Dixit (B400360575)  
- Saidutt Bhagat (B400360517)  
- Pranav Dumbre (B400360580)  

---

## 📚 References
- Rössler, A. et al., *FaceForensics++: Learning to Detect Manipulated Facial Images*, ICCV, 2019.  
- Heidari, A. et al., *Deepfake Detection Using Deep Learning Methods: A Systematic and Comprehensive Review*, 2024.  
- Coccomini, D. A. et al., *Cross-Forgery Analysis of Vision Transformers and CNNs*, ACM, 2022.  
- Nguyen, H. T. et al., *Multi-modal Deepfake Detection with Hybrid CNN-RNNs*, 2023.  
- [More references from literature survey included in project report]  

---

⚡ *This project demonstrates a practical, lightweight approach to multi-modal deepfake detection, while paving the way for more robust AI-powered trust and security solutions.*  
