'''
Main prediction module for dgaintel package
'''
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


from tensorflow.keras.models import load_model
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

import config

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
SAVED_MODEL_PATH = os.path.join(DIR_PATH, 'trained_model_7_2_1.h5')

MODEL = load_model(SAVED_MODEL_PATH)
CHAR2IDX = {'-': 0, '.': 1, '0': 2, '1': 3, '2': 4, '3': 5,
            '4': 6, '5': 7, '6': 8, '7': 9, '8': 10, '9': 11,
            '_': 12, 'a': 13, 'b': 14, 'c': 15, 'd': 16, 'e': 17,
            'f': 18, 'g': 19, 'h': 20, 'i': 21, 'j': 22, 'k': 23,
            'l': 24, 'm': 25, 'n': 26, 'o': 27, 'p': 28, 'q': 29,
            'r': 30, 's': 31, 't': 32, 'u': 33, 'v': 34, 'w': 35,
            'x': 36, 'y': 37, 'z': 38}

count=0

def _inputs(domains):
    if isinstance(domains, list):
        return [domain.lower() for domain in domains]

    return [domains.lower()]

def _get_prediction(domain_name, prob=None):
    global count

    es = Elasticsearch(f"http://{config.SELKS_IP}:{config.SELKS_PORT}/")
    if not prob:
        prob = get_prob([domain_name], raw=True)

    count = count+1

    if prob == -1:
        # api = TheHiveApi(f"http://{config.THEHIVE_SERVER}:{config.THEHIVE_PORT}", config.THEHIVE_TOKEN) 
        # alert = Alert(
        #     title='DGA Detect', 
        #     description=f"\"{domain_name}\" is too long to predict.", 
        #     type='external', 
        #     source=f'instance-{str(datetime.now())}', 
        #     sourceRef='alert-ref',
        # ) 
   
        # api.create_alert(alert)
        pred = f"\"{domain_name}\" is too long to predict."

    elif prob >= 0.5:
        # api = TheHiveApi(f"http://{config.THEHIVE_SERVER}:{config.THEHIVE_PORT}", config.THEHIVE_TOKEN) 
        # alert = Alert(
        #     title='DGA Detect', 
        #     description=f"\"{domain_name}\" is DGA with probability {prob}.", 
        #     type='external', 
        #     source=f'instance-{str(datetime.now())}', 
        #     sourceRef='alert-ref',
        # ) 
   
        # api.create_alert(alert)
        pred = '\"{}\" is DGA with probability {:f}\n'.format(domain_name, prob)

    else:
        pred = '"{}" is genuine with probability {:f}\n'.format(domain_name, prob)

    doc = {
            'author': 'TuanQuynh',
            'text': pred,
            'timestamp': datetime.now() + timedelta(hours=7),
    }

    res = es.index(index="classify_domains", id=count, document=doc)
    return pred

def get_prob(domains, raw=False, internal=False):
    '''
    Core inference function; calls model on vectorized batch of domain names.
    Input: list of domains (list)
    Output: len(domains) == 1: single probability value
            raw=False: list of tuples of format (domain_name, probability)
            raw=True: np.ndarray of probabilities
    '''
    if not isinstance(domains, list):
        domains = _inputs(domains)

    for domain in domains:
        if len(domain) > 82:
            domains.remove(domain)
            print("Domain too long to predict!")
            _get_prediction(domain, prob=-1)


    vec = np.zeros((len(domains), 82))

    for i, domain in enumerate(domains):
        for j, char in enumerate(domain):
            vec[i, j] = CHAR2IDX[char] if char in CHAR2IDX else -1


    prob = MODEL(vec).numpy()
    prob = prob.transpose()[0]

    if not internal:
        if prob.shape[0] == 1:
            return prob.sum()

        if raw:
            return prob

    return list(zip(domains, list(prob)))

def get_prediction(domains, to_file=None, show=True):
    '''
    Wrapper for printing out/writing full predictions on a domain or set of domains
    Input: domain (str), list of domains (list), domains in .txt file (FileObj)
    Output: show to stdout
        show=False: list of prediction strings (list)
        to_file=<filename>.txt: writes new file at <filename>.txt with predictions
    '''
    raw_probs = get_prob(_inputs(domains), internal=True)
    preds = [_get_prediction(domain, prob=prob) for domain, prob in raw_probs]

    if to_file:
        assert os.path.splitext(to_file)[1] == ".txt"

        with open(os.path.join(os.getcwd(), to_file), 'w') as outfile:
            outfile.writelines(preds)
        return None

    if show:
        for pred in preds:
            print(pred.strip('\n'))
        return None

    return preds

def main():
    '''
    Main function for testing purposes.
    '''
    get_prediction(['microsoft.com',
                    'squarespace.com',
                    'hsfkjdshfjasdhfk.com',
                    'fdkhakshfda.com',
                    'foilfencersarebad.com',
                    'discojjfdsf.com',
                    'fasddafhkj.com',
                    'wikipedai.com'])

if __name__ == '__main__':
    main()
