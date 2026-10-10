# Deploying AgriIntel to Render

This guide outlines how to deploy AgriIntel on [Render](https://render.com) in just a few clicks.

---

## What Has Been Configured

1. **`Procfile`**: Directs Render's Gunicorn WSGI server to run `backend.server:app`.
2. **`render.yaml`**: Official Render Blueprint file for 1-click deployment with Python 3.11.
3. **`Dockerfile` & `.dockerignore`**: Container build configuration (for Docker-based deployment).
4. **`requirements.txt`**: Configured with `--extra-index-url https://download.pytorch.org/whl/cpu` to install lightweight CPU PyTorch (~150MB instead of ~1GB CUDA binary), keeping builds fast and well under free tier resource limits.
5. **`models/best.pt`**: Production YOLOv11 model weights (3.3MB) copied into `models/` and un-ignored in `.gitignore` so git commits it directly.

---

## Option A: Blueprint Deploy (Recommended — 1 Click)

1. Push your repository to GitHub:
   ```bash
   git add .
   git commit -m "Configure Render deployment for AgriIntel"
   git push origin main
   ```
2. Log in to your [Render Dashboard](https://dashboard.render.com).
3. Click **New +** $\rightarrow$ **Blueprint**.
4. Select your `AI-Crop-Disease-Detector` repository.
5. Render will detect [render.yaml](file:///c:/Users/LOQ/Desktop/AI-Crop-Disease-Detector/render.yaml) automatically.
6. Enter your `SERPAPI_KEY` when prompted in the environment variables.
7. Click **Apply**. Render will build and deploy your app!

---

## Option B: Manual Web Service Setup

1. On [dashboard.render.com](https://dashboard.render.com), click **New +** $\rightarrow$ **Web Service**.
2. Connect your GitHub repository.
3. Configure the service settings:
   - **Name**: `agriintel`
   - **Environment**: `Python 3`
   - **Region**: Any (e.g., Oregon or Frankfurt)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn backend.server:app --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120`
4. In **Environment Variables**, add:
   - `PYTHON_VERSION`: `3.11.9`
   - `SERPAPI_KEY`: *(Your SerpApi Key)*
5. Click **Create Web Service**.

---

## Verifying Deployment

Once deployed, Render will provide a public URL like `https://agriintel.onrender.com`.
You can verify it by opening:
- `https://agriintel.onrender.com/` — Full Web UI
- `https://agriintel.onrender.com/api/health` — Health and model status check
