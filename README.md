# OpenHome

👋 Hello, world!

I'm thrilled to introduce you to OpenHome - an open-source AI smart speaker project and a platform where your creativity can flourish.

Imagine a world where your smart speaker isn't just a device but a companion, one that adapts, learns, and grows with you. That's what we're building with OpenHome – a groundbreaking open-source AI smart speaker project designed to push the boundaries of technology and imagination.

At OpenHome, we believe in the power of community-driven development to create technology that's not only advanced but also accessible. Whether you're a seasoned developer, a curious beginner, or somewhere in between, OpenHome is your opportunity to contribute to an AI smart speaker that's as simple to get started with as it is powerful.

Our mission is clear – to build an AI smart speaker that's cutting edge, open, customizable, and versatile for every user. We're not just creating a product, we're creating an ecosystem where every idea counts and is integrated to one giant super brain.

# What sets OpenHome apart? Here, you'll find:

<li><b>Accessibility:</b></li> Easy-to-understand codebase and well-documented features for all skill levels.
<li><b>Innovation:</b></li>  A playground for your most creative ideas to take shape and evolve.
<li><b>Community:</b></li>  A supportive and collaborative space where questions are welcomed, and knowledge is shared.
<li><b>Open-Source:</b></li>  We're committed to being open-source and empowering people to create the technology they want.


## Project Architecture Overview
<b>The Heart of OpenHome:</b> A Dynamic, Ever-Evolving Core At the core of OpenHome is a unique and powerful loop that continuously evolves the personality of your smart speaker. This isn't just about responding to commands; it's about creating an experience that's deeply personal and constantly refreshing. Every interaction with OpenHome is a step towards a more nuanced and tailored experience.

<b>How It Works:</b> The Magic Behind the Scenes Dynamic Personality: OpenHome begins with a foundation of diverse personalities, each ready to provide a distinct interaction experience. But here's the twist – these personalities aren't static. They evolve with every conversation, adapting to your preferences, your style, and your world.

<b>Seamless Interactions:</b> Through our advanced audio module, OpenHome listens and understands, converting your spoken words into a digital format that it can process. This is where the conversation begins.

<b>Smart Processing:</b> Leveraging the power of OpenAI's GPT model, OpenHome intelligently processes your input. Whether it's a command, a query, or casual chatter, the system is designed to understand and respond in the most relevant way.

<b>Personalized Responses:</b> The heart of OpenHome beats in its ability to learn from each interaction. Using our DynamicPersonalityConstructor, the system crafts responses that aren't just accurate but also personalized, taking into account your history and preferences.

<b>Audible Magic:</b> What good is a smart response if it can't be enjoyed? Our text-to-speech module brings the conversation to life, turning text responses into natural, fluent speech.



## Install and configure

To get the project running locally first create and spin up a conda environment as follows:

```
conda create -n openhome python=3.10
conda activate openhome
```

Next install the required dependencies.

### Install dependencies

To install the required dependencies, run the following command:
```
python -m pip install -r requirements.txt 
```
Also install following:

```
sudo apt-get install libportaudio2
sudo apt install ffmpeg
sudo apt-get install portaudio19-dev
```
```
pip install PyAudio
```
## How to run the main pipeline?

To run the main pipeline, run the following command:

```
python main.py -p <Enter personality>
```

- `<Enter personality>`: Pass your desired personality

`Note: If you enter a name that do not exists in our personality list you will be given list of personalities to choose one from them.`
