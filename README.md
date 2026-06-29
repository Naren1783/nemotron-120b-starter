# nemotron-120b-starter
Start generating AI responses with NVIDIA's Nemotron model in under 5 minutes using this simple Python quickstart.

# 🚀 nemotron-quickstart

Start generating AI responses with NVIDIA's Nemotron model in under 5 minutes using this simple Python quickstart. This project uses the standard OpenAI Python format to give you access to NVIDIA's massive `nemotron-3-super-120b-a12b` model for free!

---

## 🔥 Key Features

* **Power of a 120B Model:** Tap into a massive, state-of-the-art AI model.
* **OpenAI-Compatible:** Uses the exact same code structure as OpenAI tools, making it easy to learn.
* **100% Free Endpoint:** Built entirely using the free API access provided by the NVIDIA Developer Build playground.

---

## 🛠️ Step-by-Step Setup Guide

Follow these instructions exactly to get the AI running on your own computer. 

### Step 1: Install Python
If you don't already have Python on your computer, you need to install it.
1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Download the latest version for your operating system (Windows/Mac).
3. **Important for Windows Users:** When you open the installer, make sure to check the box at the very bottom that says **"Add Python to PATH"** before clicking Install.

### Step 2: Download This Project
1. Click the green **"<> Code"** button at the top right of this GitHub page.
2. Click **"Download ZIP"**.
3. Extract (unzip) the folder and move it to your Desktop so it is easy to find.

### Step 3: Get Your Free NVIDIA API Key
To connect to NVIDIA's servers, you need a digital "key".
1. Go to the [NVIDIA API Catalog](https://build.nvidia.com/explore/discover) and create a free account.
2. Find the **Nemotron-3-Super-120B** model.
3. Click the **Generate API Key** button.
4. Copy your unique key (it will look something like `nvapi-...`). Keep this secret!

### Step 4: Add Your Key to the Code
1. Open the extracted folder on your Desktop.
2. Right-click the `nemotron_test.py` file and open it with a text editor (Notepad, VS Code, or Notepad++).
3. Find this exact section of code (around line 5):
   ```python
   client = OpenAI(
     base_url = "[https://integrate.api.nvidia.com/v1](https://integrate.api.nvidia.com/v1)",
     api_key = "YOUR_API_KEY" # Replace with your active key
   )
