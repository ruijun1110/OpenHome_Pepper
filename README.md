<h1>Welcome to OpenHome</h1>

<p>👋 Greetings, Innovators!</p>

<p>
    I'm thrilled to introduce you to <strong>OpenHome</strong> - an open-source AI smart speaker project and a platform where your creativity can flourish.
</p>

<p>
    At OpenHome, we believe in the power of community-driven development to create technology that's not only advanced but also accessible. Whether you're a seasoned developer, a curious beginner, or somewhere in between, OpenHome is your opportunity to contribute to an AI smart speaker that's as simple to get started with as it is powerful.
</p>

<p>
    Our mission is clear – to build an AI smart speaker that's cutting edge, open, customizable, and versatile for every user. We're not just creating a product, we're creating an ecosystem where every idea counts and is integrated to one giant super brain. 
</p>

<p>
    What sets OpenHome apart? Here, you'll find:
    <ul>
        <li><strong>Accessibility:</strong> Easy-to-understand codebase and well-documented features for all skill levels.</li>
        <li><strong>Innovation:</strong> A playground for your most creative ideas to take shape and evolve.</li>
        <li><strong>Community:</strong> A supportive and collaborative space where questions are welcomed, and knowledge is shared.</li>
    </ul>
</p>

<h2>Project Architecture Overview</h2>

<p><strong>talk3.py (Main Script):</strong></p>
<ul>
    <li>Entry point of the application. 
    <li>Orchestrates the program flow, calling functions from other modules.</li>
    <li>Manages the main interaction loop.</li>
    <li>To get started with OpenHome, navigate to the <code>/openhome</code> directory in your terminal and launch the application with the command: <code>python3 talk3.py</code>.</li>
</ul>

<p><strong>audio_module.py:</strong></p>
<ul>
    <li>Handles audio recording and transcription.</li>
    <li>Interacts with the sound device for user input recording.</li>
</ul>

<p><strong>chatgpt_module.py:</strong></p>
<ul>
    <li>Manages interactions with OpenAI GPT model.</li>
    <li>Sends user input to the model and retrieves responses.</li>
</ul>

<p><strong>greeting_module.py:</strong></p>
<ul>
    <li>Used for initial user interaction, especially on first run.</li>
    <li>Generates greeting based on user data using chatgpt_module.py and text_speech_module.py.</li>
</ul>

<p><strong>text_speech_module.py:</strong></p>
<ul>
    <li>Converts text to speech for outputting chatbot responses.</li>
    <li>Interacts with an external Text-to-Speech service.</li>
</ul>

<p><strong>file_management.py:</strong></p>
<ul>
    <li>Utility module for file operations.</li>
    <li>Handles reading from and writing to files.</li>
</ul>

<p><strong>Supporting Components:</strong></p>
<ul>
    <li><strong>api-keys (Directory):</strong> Stores API keys for external services.</li>
    <li><strong>personalities (Directory):</strong> Contains files for chatbot personalities.</li>
    <li><strong>history-files (Directory):</strong> Stores logs of conversations.</li>
    <li><strong>temp-sound (Directory):</strong> Temporary storage for sound files.</li>
    <li><strong>__pycache__ (Directory):</strong> Contains Python 3 cache files.</li>
    <li><strong>README.md:</strong> Overview, setup instructions, and essential information.</li>
</ul>

<p><strong>Interactions:</strong></p>
<ul>
    <li>User interaction starts with talk3.py, which records speech and sends it to chatgpt_module.py.</li>
    <li>Responses are processed and sent back to the user through text_speech_module.py.</li>
    <li>First run initialization and greeting are managed by greeting_module.py.</li>
    <li>Data handling is centralized in file_management.py.</li>
</ul>

<p><strong>General Architecture:</strong></p>
<ul>
    <li>Modular design for separation of concerns.</li>
    <li>Each module is focused on a specific task for reduced complexity.</li>
    <li>talk3.py coordinates all modules for a cohesive application experience.</li>
</ul>


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
  <li>This instance is sending data to Recursal for training. The file is currently using a pass through Recursal API key<li>
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
    <pre><code>python3 talk3.py</code></pre>
  </li>
</ul>

<p><strong>Note:</strong> Ensure your microphone and speakers are working. If you encounter errors related to missing dependencies or files, double-check all necessary components.</p>

</body>
</html>
