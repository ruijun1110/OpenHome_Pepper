Welcome to OpenHome!

</head>
<body>

<h2>OpenHome v0.01 Setup Instructions</h2>

<p>Follow these steps to run the provided script for the first time:</p>

<h3><strong>Step 1: Install Python 3</strong></h3>
<ul>
  <li>Ensure you have <strong>Python 3</strong> installed on your system. Download it from <a href="https://www.python.org/downloads/">python.org</a>.</li>
</ul>

<h3><strong>Step 2: Install Homebrew (macOS/Linux)</strong></h3>
<ul>
  <li>If using macOS or Linux, install <strong>Homebrew</strong>, a package manager. Run in terminal:
    <pre><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code></pre>
  </li>
  <li>For more details, visit <a href="https://brew.sh/">brew.sh</a>.</li>
</ul>

<h3><strong>Step 3: Install Dependencies</strong></h3>
<ul>
  <li>Open terminal and install necessary Python libraries using pip3:
    <pre><code>pip3 install sounddevice soundfile numpy openai colorama datetime base64 pydub requests</code></pre>
  </li>
</ul>

<h3><strong>Step 4: Install a Specific Version of the OpenAI Library</strong></h3>
<ul>
  <li>Install version 0.28 of the OpenAI library:
    <pre><code>pip3 install openai==0.28</code></pre>
  </li>
</ul>

<h3><strong>Step 5: Update Your API Keys</strong></h3>
<ul>
  <li>Obtain your OpenAI and ElevenLabs API keys.</li>
  <li>Save them in text files within a folder named <code>api-keys</code> at your script's root directory. Name the files <code>openaiapikey2.txt</code> and <code>elabapikey.txt</code>.</li>
</ul>

<h3><strong>Step 6: Prepare Additional Files</strong></h3>
<ul>
  <li>Ensure necessary files such as <code>Activated.txt</code> in the <code>personalities</code> folder as this is the main personality. Other history files <code>user.txt</code> in the <code>history-files</code> folder are present.</li>
  <li>Create <code>temp-sound</code> and <code>history-files</code> directories if not existing.</li>
</ul>

<h3><strong>Step 7: Run the Script</strong></h3>
<ul>
  <li>Navigate to the directory where your script (<code>talk.py</code>) is located.</li>
  <li>Run the script using Python 3:
    <pre><code>python3 talk.py</code></pre>
  </li>
</ul>

<p><strong>Note:</strong> Ensure your microphone and speakers are working. If you encounter errors related to missing dependencies or files, double-check all necessary components.</p>

</body>
</html>
