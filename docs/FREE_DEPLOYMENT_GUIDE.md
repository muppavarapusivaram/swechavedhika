# Free Cloud Deployment & Public Demo Guide for Swecha Vedika

This guide details two 100% free methods to deploy Swecha Vedika for demonstrations, SAMYAK-2026 evaluators, and external visitors.

---

## Method 1: Instant Public HTTPS Tunnel (Zero Signup, 1 Minute)
> **Best for SAMYAK-2026 Expo Live Demo**: Allows evaluators and visitors to immediately open your running application on their own mobile phones without cloud registration or server costs!

Since your project is already running locally in Docker, you can generate a secure, public HTTPS link in 30 seconds using Node's built-in `npx localtunnel`:

### Steps:
1. Ensure your local stack is running:
   ```bash
   docker compose up -d
   ```
2. Open a new PowerShell terminal and run:
   ```bash
   npx localtunnel --port 5173 --subdomain swechavedika
   ```
   *(If prompted to install `localtunnel`, type `y`)*.
3. You will receive a public HTTPS link:
   ```
   your url is: https://swechavedika.loca.lt
   ```
4. **How to Use at the Stall**:
   - Anyone on any device (phone, laptop) can open `https://swechavedika.loca.lt`.
   - On first visit, Localtunnel asks for a friendly verification IP (shown on your screen). Once entered, the full Swecha Vedika platform loads with video stage, WhatsApp simulator, and archive!

---

## Method 2: Permanent 24/7 Cloud Deployment (100% Free Forever)
To host the project permanently online 24/7 without needing your laptop powered on, use this standard free cloud stack:

| Component | Free Platform | Cost | Setup Time |
| :--- | :--- | :---: | :---: |
| **Frontend** | [Vercel](https://vercel.com) | $0 (Free Forever) | 2 Minutes |
| **Backend API** | [Render.com](https://render.com) | $0 (Free Tier) | 3 Minutes |
| **Database** | [Neon.tech](https://neon.tech) or [Supabase](https://supabase.com) | $0 (Free PostgreSQL 16) | 2 Minutes |
| **LiveKit WebRTC** | [LiveKit Cloud](https://cloud.livekit.io) | $0 (50GB free/month) | 1 Minute |

---

### Step-by-Step Instructions:

### Step 1: Create Free PostgreSQL 16 Database on Neon.tech
1. Go to **[https://neon.tech](https://neon.tech)** and sign in with your GitHub account.
2. Click **Create Project**, choose **PostgreSQL 16**, and select region **Asia (Singapore)**.
3. Copy the database connection string:
   ```
   postgresql://user:password@ep-xyz.ap-southeast-1.aws.neon.tech/neondb?sslmode=require
   ```
   *(Keep this string handy for Step 2)*.

---

### Step 2: Deploy Backend to Render.com
1. Go to **[https://render.com](https://render.com)** and sign in with GitHub.
2. Click **New +** $\rightarrow$ **Web Service**.
3. Select your repository: `muppavarapusivaram/swechavedhika`.
4. Fill in the settings:
   - **Name**: `swecha-vedika-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: **Free**
5. Under **Environment Variables**, add:
   - `DATABASE_URL`: *(Paste your Neon connection string from Step 1)*
   - `JWT_SECRET_KEY`: `supersecretjwtkey_swechavedika_2026`
   - `LIVEKIT_URL`: `wss://your-project.livekit.cloud`
   - `LIVEKIT_API_KEY`: `your_key`
   - `LIVEKIT_API_SECRET`: `your_secret`
6. Click **Deploy Web Service**! Render will deploy your API and give you a public URL like:
   `https://swecha-vedika-backend.onrender.com`

---

### Step 3: Deploy Frontend to Vercel
1. Go to **[https://vercel.com](https://vercel.com)** and sign in with GitHub.
2. Click **Add New...** $\rightarrow$ **Project**.
3. Select `muppavarapusivaram/swechavedhika`.
4. Configure the project:
   - **Root Directory**: Click edit and select **`frontend`**.
   - **Framework Preset**: **Vite** (auto-detected).
   - **Environment Variables**:
     - `VITE_BACKEND_URL`: `https://swecha-vedika-backend.onrender.com` *(From Step 2)*
     - `VITE_LIVEKIT_URL`: `wss://your-project.livekit.cloud`
5. Click **Deploy**!
6. In ~60 seconds, your frontend will be live on a custom URL:
   `https://swechavedhika.vercel.app`

---

### Step 4: Free LiveKit Cloud WebRTC Keys (Optional for Cloud Video)
1. Go to **[https://cloud.livekit.io](https://cloud.livekit.io)** and sign up for free (50GB free bandwidth/month).
2. Create a project named `swecha-vedika`.
3. Copy your **WebSocket URL** (`wss://swecha-vedika-xyz.livekit.cloud`), **API Key**, and **API Secret**.
4. Paste these into your Render and Vercel environment variables.

---

### Summary
* For the **SAMYAK-2026 Expo stall**, **Method 1 (`npx localtunnel`)** is the fastest and most stable because it runs directly off your local Docker machine without depending on external cloud cold-starts.
* For **Permanent Portfolio / Resume deployment**, **Method 2 (Vercel + Render + Neon)** runs 24/7 for $0 forever!
