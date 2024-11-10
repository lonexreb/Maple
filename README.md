MAPLE.AI
![WhatsApp Image 2024-11-10 at 07 10 45](https://github.com/user-attachments/assets/fb65531d-3697-406c-9e44-3a8ce9dad6af)

About the project:
## Inspiration
Learning shouldn't feel like navigating through a maze alone. While most educational tools simply provide answers, they miss what truly matters - how students feel and think during their learning journey.
Introducing Maple - an innovative learning companion that combines sophisticated AI with genuine understanding of student needs:
By focusing on both the 'what' and 'how' of learning, Maple transforms learning from a daunting subject into an engaging journey of discovery.

## What it does
**Smart Topic Navigation**: We break down challenging chemistry concepts into digestible pieces, building your understanding step by step.
**Empathetic Support**: Our advanced voice analysis technology recognizes when you're stuck, frustrated, or losing interest. Instead of just giving answers, Maple responds with the right balance of guidance and encouragement when you need it most.
**Growth-Focused Practice**: Through interactive quizzes, you'll not only track your progress but also discover your strengths and identify areas where you can improve, making each study session more rewarding than the last.

## How we built it
We build it using the following tools:
**Hume EVI**
Maple’s goal is to offer precise academic support while recognizing and adapting to students’ emotional states, promoting a nurturing and effective learning experience.
Hume's EVI model powers real-time speech-to-text and emotion detection, starting when a user activates the microphone. When the microphone is turned off, the model sends the text and the top five emotions detected to Accel, which then generates a suitable response using a fine-tuned LLM. Additionally, Maple’s frontend displays a mood gauge, giving users insight into their study habits and emotional trends.

**DataBricks**
We ran Wolfram MathWorld with Open source RAG using DBRX, LanceDB, and LLama-index with Huggingface Embeddings to create a knowledge base for our Model to prevent hallucinations. Further we also used databrick's chat UI library to finetune and create a more effecient chat space for our platform.

**Midnight**
We created a decentralized application (DApp) in Docker that securely handles sensitive student data. Midnight’s blockchain could ensure data integrity for storing user records, progress tracking, or credentials in a tamper-resistant way, while preserving privacy. 
## Challenges we ran into

## Accomplishments that we're proud of
We had to spend time quite some time integrating our backend and frontend effectively which was a very good learning experience. We also spent time on using KateX and MD to improve our responses. We also experimented with Hume EVI versions.

## What we learned
How important creating a knowledge base is to prevent hallucination. We also developed a clear and concise system architecture.

## What's next for Maple.ai
Including new features such as improving to Hume AI's EVI2 that utilises facial expressions, learning pattern recognition for the behaviors and study habits of the student, course notes summarization and overlapping common concepts, and finally improve our platform's knowledge base to many more topics.

![WhatsApp Image 2024-11-10 at 07 12 56](https://github.com/user-attachments/assets/67b4b3f7-df4c-488d-bb87-9b9382f6938d)

![WhatsApp Image 2024-11-10 at 07 12 56 (1)](https://github.com/user-attachments/assets/2dc0612f-bc5a-45cf-9888-6c9088798b62)



