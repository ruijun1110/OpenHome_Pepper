<h1>Welcome to OpenHome</h1>

<p>👋 Greetings, Innovators!</p>

<p>
    I'm thrilled to introduce you to <strong>OpenHome</strong> - an open-source AI smart speaker project and a platform where your creativity can flourish.

Imagine a world where your smart speaker isn't just a device but a companion, one that adapts, learns, and grows with you. That's what we're building with OpenHome – a groundbreaking open-source AI smart speaker project designed to push the boundaries of technology and imagination.
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
        <li><strong>Open-Source:</strong> We're committed to being open-source and empowering people to create the technology they want.</li>
    </ul>
</p>

<h2>Project Architecture Overview</h2>

<b>The Heart of OpenHome: A Dynamic, Ever-Evolving Core</b>
At the core of OpenHome is a unique and powerful loop that continuously evolves the personality of your smart speaker. This isn't just about responding to commands; it's about creating an experience that's deeply personal and constantly refreshing. Every interaction with OpenHome is a step towards a more nuanced and tailored experience.

<b>How It Works:</b> The Magic Behind the Scenes
Dynamic Personality: OpenHome begins with a foundation of diverse personalities, each ready to provide a distinct interaction experience. But here's the twist – these personalities aren't static. They evolve with every conversation, adapting to your preferences, your style, and your world.

<b>Seamless Interactions:</b> Through our advanced audio module, OpenHome listens and understands, converting your spoken words into a digital format that it can process. This is where the conversation begins.

<b>Smart Processing:</b> Leveraging the power of OpenAI's GPT model, OpenHome intelligently processes your input. Whether it's a command, a query, or casual chatter, the system is designed to understand and respond in the most relevant way.

<b>Personalized Responses:</b> The heart of OpenHome beats in its ability to learn from each interaction. Using our DynamicPersonalityConstructor, the system crafts responses that aren't just accurate but also personalized, taking into account your history and preferences.

<b>Audible Magic:</b> What good is a smart response if it can't be enjoyed? Our text-to-speech module brings the conversation to life, turning text responses into natural, fluent speech.



<h2>Main Script</h2>
<p><strong>run.py:</strong></p>
    <ul>
        <li>Entry point of the application.</li>
        <li>Orchestrates program flow, calling functions from other modules.</li>
        <li>Manages the main interaction loop.</li>
        <li>To start OpenHome, navigate to the /openhome directory and launch with the command: <code>python3 run.py</code>.</li>
    </ul>

<h2>Core Modules</h2>

<p><strong>process_command.py:</strong></p>
    <ul>
        <li>Determines if a specific command is triggered based on transcribed speech.</li>
        <li>Trigger words and capabilities are listed in the /capabilities directory.</li>
        <li>Commands must be stated and transcribed precisely to be recognized.</li>
        <li>Defaults to two-way conversation if no command is identified.</li>
    </ul>

<p><strong>audio_module.py:</strong></p>
    <ul>
        <li>Handles audio recording and transcription.</li>
        <li>Interacts with sound device for user input recording.</li>
    </ul>

<p><strong>chatgpt_module.py:</strong></p>
    <ul>
        <li>Manages interactions with OpenAI GPT model.</li>
        <li>Sends user input to the model and retrieves responses.</li>
    </ul>

<p><strong>greeting_module.py:</strong></p>
    <ul>
        <li>Facilitates initial user interaction, particularly on first run.</li>
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

<h2>Supporting Components</h2>
    <ul>
        <li><strong>api-keys (Directory):</strong> Stores API keys for external services.</li>
        <li><strong>personalities (Directory):</strong> Contains files for chatbot personalities.</li>
        <li><strong>history-files (Directory):</strong> Stores logs of conversations.</li>
        <li><strong>temp-sound (Directory):</strong> Temporary storage for sound files.</li>
        <li><strong>__pycache__ (Directory):</strong> Contains Python 3 cache files.</li>
    </ul>

<h2>Interactions</h2>
    <ul>
        <li>User interaction starts with run.py, which records speech and sends it to chatgpt_module.py.</li>
        <li>Responses are processed and sent back to the user through text_speech_module.py.</li>
        <li>First run initialization and greeting are managed by greeting_module.py.</li>
        <li>Data handling is centralized in file_management.py.</li>
    </ul>

<h2>General Architecture</h2>
    <ul>
        <li>Modular design for separation of concerns.</li>
        <li>Each module focuses on a specific task, reducing complexity.</li>
        <li>run.py coordinates all modules for a cohesive application experience.</li>
    </ul>

    <p>Welcome to OpenHome!</p>



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

<h3><strong>Step 4: Upgrade the OpenAI Library</strong></h3>
<ul>
  <li>Install the OpenAI library (This is a known area where some install/compatability issues occur):
    <pre><code>pip3 install --upgrade openai</code></pre>
<ui></ui>Verify the Package Version: Ensure you have the correct version of the openai package installed. You can check the version by running:</ul> <code>pip show openai </code>
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
  <li>Navigate to the directory where your script (<code>run.py</code>) is located.</li>
  <li>Run the script using Python 3:
    <pre><code>python3 run.py</code></pre>
  </li>
</ul>

<p><strong>Note:</strong> Ensure your microphone and speakers are working. If you encounter errors related to missing dependencies or files, double-check all necessary components.</p>

</body>
</html>
