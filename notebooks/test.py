import os
import sys
import threading
import time
from pprint import pprint

import debugpy
import numpy as np
import pandas as pd
import torch
import transformers
from transformers import LlamaForCausalLM, LlamaTokenizer
import json

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# pprint(f"Device: {device}")
# torch.cuda.empty_cache()


def handle_exception(args):
    print(
        f"Exception occurred in thread {args.thread.ident}: {args.exc_type.__name__}: {args.exc_value}"
    )

import dspy
from dspy.retrieve.you_rm import YouRM
from dspy.retrieve.clarifai_rm import ClarifaiRM
from dspy.primitives import Example

devset = [
    Example({
        "input": "What is the latest confirmed valuation of Runway. Include date, raised amount, the series name of the funding round and VCs",
    }),
    Example({
        "input": "What is the latest confirmed valuation of ElevenLabs. Include date, raised amount, the series name of the funding round and VCs",
    }),
    Example({
        "input": "What is the latest confirmed valuation of Pika. Include date, raised amount, the series name of the funding round and VCs",
    }),
    Example({
        "input": "What is the latest confirmed valuation of Writer. Include date, raised amount, the series name of the funding round and VCs",
    }),
    Example({
        "input": "What is the latest confirmed valuation of AI21 Labs. Include date, raised amount, the series name of the funding round and VCs",
    }),
]
devset = [x.with_inputs('input') for x in devset]
print(devset[:1])


def main():
    print("Start")

    gpt3_model = dspy.OpenAI('gpt-3.5-turbo-0125', max_tokens=1000)

    # ydc_ai = os.environ["YDC_API_KEY"]
    # user_id = os.environ["CLARIFAI_USER_ID"]
    clarifai_retriever=ClarifaiRM(clarifai_user_id=os.environ["CLARIFAI_USER_ID"], clarfiai_app_id=os.environ["CLARIFAI_APP_ID"], clarifai_pat=os.environ["CLARIFAI_PAT"], k=1)
    you_retriever = YouRM()

    dspy.settings.configure(lm=gpt3_model, rm=you_retriever)

    sentence = "disney again ransacks its archives for a quick-buck sequel ."

    classify = dspy.Predict('sentence -> sentiment')
    print(classify(sentence=sentence).sentiment)

    agent = dspy.ReAct("question -> answer", tools=[dspy.Retrieve(k=1)])

    # json_obj = json.dumps(clarifai_retriever)  # serialize to JSON
    # print(json_obj)

    # colbertv2_retriever = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')

    # you_retriever = YouRM()
    # result = you_retriever.forward('What is the latest confirmed valuation of Cohere. Include date, raised amount, the series name of the funding round and VCs')
    # print(result[:1])

    # # serializable_obj = colbertv2_retriever.dump_state()  # get serializable representation
    # # print(serializable_obj)
    # json_obj = json.dumps(clarifai_retriever)  # serialize to JSON
    # print(json_obj)

    # # gpt3_model = dspy.OpenAI('gpt-3.5-turbo-0125', max_tokens=1000)
    # # you_retriever = YouRM()
    # # dspy.configure(lm=gpt3_model, rm=you_retriever)

    # predictor = dspy.ReAct("question -> answer", tools=[dspy.Retrieve(k=1)])
    # predictor = dspy.Predict("input -> valuation, date", tools=[dspy.Retrieve(k=1)])
    predictor = dspy.Predict("input -> valuation", tools=[dspy.Retrieve(k=1)])
    # valuation, date = predictor(input = devset[0].input)

    print("End")


if __name__ == "__main__":
    # main_thread = threading.Thread(target=main)
    # main_thread.start()
    # main_thread.join()
    # multiprocessing.freeze_support()

    # threading.excepthook = handle_exception

    try:
        main()
    finally:
        debugpy.wait_for_client()
        print(f"Finalling threads")
        for t in threading.enumerate():
            print(f"Thread: ", t.getName)

        # print(f"Attempt to join threads to ensure all threads are finished")
        # for t in threading.enumerate():
        #     name = t.getName()
        #     print(f"About To Join : ", name)
        #     if name == "Thread-6":
        #         t.join()
