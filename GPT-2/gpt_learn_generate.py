import gpt_2_simple as gpt2
import os

#https://towardsdatascience.com/how-to-make-a-gpt2-twitter-bot-8669df60e60a

model_name = "117M"

if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

sess = gpt2.start_tf_sess()

num_steps = 100 #TODO: set this to Ceiling(Word Count/Line Count) of the training data file

text_path = "TRAINING DATA"

gpt2.finetune(sess, 
              text_path,
              model_name=model_name,
              steps=num_steps
             )

# session: The session is just the current Tensorflow session
# dataset: This is the path to a text file to load in and use for training, more on this later.
# model_name: The name of the GPT2 model to use can be 117M, 124M, or 355M. 124M works well on my 1080Ti GPU.
# steps" The number of steps for the model to take. This number should be high enough to step through your whole data set at least once but not so high that you over fit. When fine tuning GPT2 on a relatively small data set I like to do one to two epochs. Then I test to make sure that what it generates wasn’t directly from the training set.


length = 100
destination_path = ""
temperature = 0.5
prefix = ""

text = gpt2.generate(
    sess,
    length=length,
    temperature=temperature,
    destination_path=destination_path,
    prefix=prefix,
    return_as_list=True
)
# sess: is the tensorflow session we want to use
# checkpoint_dir: is the path to the saved checkpoints from our finetuning
# temperature: is and value greater than 0 I like to play around between .8 and 2. The lower the temperature the more consistent and predictable your outputs the higher the temperature the more wild, fun, and possibly nonsensical they will be.
# destination_path: is a path to where you want the text to be saved. If you just want to return it inline make this None
# prefix: is a fun one. It can be a string of text that is used to seed the model. So if you started with “thou shall not” then the model will write the next words as if it had started with “thou shall not.”
# return_as_list: will cause the function to return the text instead of just printing it out.