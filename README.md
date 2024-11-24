# Code-test
Code test for text analysis- DocLegal.ai

I have chosen the second task -- Text summarization.

To use my model you can download the python file of text summarization.py in the repository.
After you download it. Run the following commany in your command line interface with your own text you want to summarize.

python TextSummarization.py "Your own text"

Example:

python TextSummarization.py "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.Colloquially, the term artificial intelligence is often used to describe machines (or computers) that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving."

The output should give something like this(the latter part of the output is the summary):

summary: Summarize the following text: Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.Colloquially, the term artificial intelligence is often used to describe machines (or computers) that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving. The term artificial intelligence is used to distinguish the field from cognitive science, which studies the human mind, and from computational intelligence, which studies methods that are inspired by biological systems and materials. The term artificial intelligence is also used to distinguish the field from

________________________________________________________________________________________________________________________

Explanation of the Approach: 
In my approach, I used prompt engineering on a pre-trained language model (meta-llama/Llama-3.2-3B) on the Hugging Face Transformers library to implement. Reason for choosing this model is that the meta-llama/Llama-3.2-3B model is designed for generating coherent and high-quality text outputs, making it ideal for summarization tasks.

Potential Improvements or Extensions:
For potential imporvements or extension, I would replace the generic text-generation model with a summarization-specific model like t5-small, bart-large, or a fine-tuned version of LLaMA specifically trained on summarization datasets.This would reduce reliance on prompt engineering and yield more precise summaries.
