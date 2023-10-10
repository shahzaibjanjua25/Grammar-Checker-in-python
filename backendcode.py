import re
import spacy
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker

nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()
lemmatizer = WordNetLemmatizer()
irregular_words = {
    'arise': ['arise', 'arose', 'arisen', 'arising'],
    'awake': ['awake', 'awoke', 'awoken', 'awaking'],
    'be': ['am/is/are', 'was/were', 'been', 'being'],
    'bear': ['bear', 'bore', 'borne/born', 'bearing'],
    'beat': ['beat', 'beat', 'beaten', 'beating'],
    'become': ['become', 'became', 'become', 'becoming'],
    'begin': ['begin', 'began', 'begun', 'beginning'],
    'bend': ['bend', 'bent', 'bent', 'bending'],
    'bet': ['bet', 'bet', 'bet', 'betting'],
    'bind': ['bind', 'bound', 'bound', 'binding'],
    'bite': ['bite', 'bit', 'bitten', 'biting'],
    'bleed': ['bleed', 'bled', 'bled', 'bleeding'],
    'blow': ['blow', 'blew', 'blown', 'blowing'],
    'break': ['break', 'broke', 'broken', 'breaking'],
    'bring': ['bring', 'brought', 'brought', 'bringing'],
    'build': ['build', 'built', 'built', 'building'],
    'burn': ['burn', 'burnt/burned', 'burnt/burned', 'burning'],
    'burst': ['burst', 'burst', 'burst', 'bursting'],
    'buy': ['buy', 'bought', 'bought', 'buying'],
    'cast': ['cast', 'cast', 'cast', 'casting'],
    'catch': ['catch', 'caught', 'caught', 'catching'],
    'choose': ['choose', 'chose', 'chosen', 'choosing'],
    'cling': ['cling', 'clung', 'clung', 'clinging'],
    'come': ['come', 'came', 'come', 'coming'],
    'cost': ['cost', 'cost', 'cost', 'costing'],
    'creep': ['creep', 'crept', 'crept', 'creeping'],
    'cut': ['cut', 'cut', 'cut', 'cutting'],
    'deal': ['deal', 'dealt', 'dealt', 'dealing'],
    'dig': ['dig', 'dug', 'dug', 'digging'],
    'dive': ['dive', 'dove/dived', 'dived', 'diving'],
    'do': ['do', 'did', 'done', 'doing'],
    'draw': ['draw', 'drew', 'drawn', 'drawing'],
    'dream': ['dream', 'dreamt/dreamed', 'dreamt/dreamed', 'dreaming'],
    'drink': ['drink', 'drank', 'drunk', 'drinking'],
    'drive': ['drive', 'drove', 'driven', 'driving'],
    'eat': ['eat', 'ate', 'eaten', 'eating'],
    'fall': ['fall', 'fell', 'fallen', 'falling'],
    'feed': ['feed', 'fed', 'fed', 'feeding'],
    'feel': ['feel', 'felt', 'felt', 'feeling'],
    'fight': ['fight', 'fought', 'fought', 'fighting'],
    'find': ['find', 'found', 'found', 'finding'],
    'fly': ['fly', 'flew', 'flown', 'flying'],
    'forbid': ['forbid', 'forbade', 'forbidden', 'forbidding'],
    'forget': ['forget', 'forgot', 'forgotten', 'forgetting'],
    'forgive': ['forgive', 'forgave', 'forgiven', 'forgiving'],
    'freeze': ['freeze', 'froze', 'frozen', 'freezing'],
    'get': ['get', 'got', 'got/gotten', 'getting'],
    'give': ['give', 'gave', 'given', 'giving'],
    'go': ['go', 'went', 'gone', 'going'],
    'grow': ['grow', 'grew', 'grown', 'growing'],
    'hang': ['hang', 'hung', 'hung', 'hanging'],
    'have': ['have', 'had', 'had', 'having'],
    'hear': ['hear', 'heard', 'heard', 'hearing'],
    'hide': ['hide', 'hid', 'hidden', 'hiding'],
    'hit': ['hit', 'hit', 'hit', 'hitting'],
    'hold': ['hold', 'held', 'held', 'holding'],
    'hurt': ['hurt', 'hurt', 'hurt', 'hurting'],
    'keep': ['keep', 'kept', 'kept', 'keeping'],
    'kneel': ['kneel', 'knelt', 'knelt', 'kneeling'],
    'know': ['know', 'knew', 'known', 'knowing'],
    'lay': ['lay', 'laid', 'laid', 'laying'],
    'lead': ['lead', 'led', 'led', 'leading'],
    'lean': ['lean', 'leant/leaned', 'leant/leaned', 'leaning'],
    'leap': ['leap', 'leapt/leaped', 'leapt/leaped', 'leaping'],
    'learn': ['learn', 'learnt/learned', 'learnt/learned', 'learning'],
    'leave': ['leave', 'left', 'left', 'leaving'],
    'lend': ['lend', 'lent', 'lent', 'lending'],
    'let': ['let', 'let', 'let', 'letting'],
    'lie': ['lie', 'lay', 'lain', 'lying'],
    'light': ['light', 'lit/lighted', 'lit/lighted', 'lighting'],
    'lose': ['lose', 'lost', 'lost', 'losing'],
    'make': ['make', 'made', 'made', 'making'],
    'mean': ['mean', 'meant', 'meant', 'meaning'],
    'meet': ['meet', 'met', 'met', 'meeting'],
    'pay': ['pay', 'paid', 'paid', 'paying'],
    'put': ['put', 'put', 'put', 'putting'],
    'read': ['read', 'read', 'read', 'reading'],
    'ride': ['ride', 'rode', 'ridden', 'riding'],
    'ring': ['ring', 'rang', 'rung', 'ringing'],
    'rise': ['rise', 'rose', 'risen', 'rising'],
    'run': ['run', 'ran', 'run', 'running'],
    'say': ['say', 'said', 'said', 'saying'],
    'see': ['see', 'saw', 'seen', 'seeing'],
    'seek': ['seek', 'sought', 'sought', 'seeking'],
    'sell': ['sell', 'sold', 'sold', 'selling'],
    'send': ['send', 'sent', 'sent', 'sending'],
    'set': ['set', 'set', 'set', 'setting'],
    'shake': ['shake', 'shook', 'shaken', 'shaking'],
    'shed': ['shed', 'shed', 'shed', 'shedding'],
    'shine': ['shine', 'shone', 'shone', 'shining'],
    'shoot': ['shoot', 'shot', 'shot', 'shooting'],
    'share':['share','shared','shared','sharing'],
    'show': ['show', 'showed', 'shown', 'showing'],
    'shrink': ['shrink', 'shrank', 'shrunk', 'shrinking'],
    'shut': ['shut', 'shut', 'shut', 'shutting'],
    'sing': ['sing', 'sang', 'sung', 'singing'],
    'sink': ['sink', 'sank', 'sunk', 'sinking'],
    'sit': ['sit', 'sat', 'sat', 'sitting'],
    'sleep': ['sleep', 'slept', 'slept', 'sleeping'],
    'slide': ['slide', 'slid', 'slid', 'sliding'],
    'speak': ['speak', 'spoke', 'spoken', 'speaking'],
    'speed': ['speed', 'sped', 'sped', 'speeding'],
    'spell': ['spell', 'spelt/spelled', 'spelt/spelled', 'spelling'],
    'spend': ['spend', 'spent', 'spent', 'spending'],
    'spill': ['spill', 'spilt/spilled', 'spilt/spilled', 'spilling'],
    'spin': ['spin', 'spun', 'spun', 'spinning'],
    'spit': ['spit', 'spat', 'spat', 'spitting'],
    'split': ['split', 'split', 'split', 'splitting'],
    'spread': ['spread', 'spread', 'spread', 'spreading'],
    'spring': ['spring', 'sprang', 'sprung', 'springing'],
    'stand': ['stand', 'stood', 'stood', 'standing'],
    'steal': ['steal', 'stole', 'stolen', 'stealing'],
    'stick': ['stick', 'stuck', 'stuck', 'sticking'],
    'sting': ['sting', 'stung', 'stung', 'stinging'],
    'stink': ['stink', 'stank', 'stunk', 'stinking'],
    'stride': ['stride', 'strode', 'stridden', 'striding'],
    'strike': ['strike', 'struck', 'struck/stricken', 'striking'],
    'swear': ['swear', 'swore', 'sworn', 'swearing'],
    'sweep': ['sweep', 'swept', 'swept', 'sweeping'],
    'swim': ['swim', 'swam', 'swum', 'swimming'],
    'swing': ['swing', 'swung', 'swung', 'swinging'],
    'take': ['take', 'took', 'taken', 'taking'],
    'teach': ['teach', 'taught', 'taught', 'teaching'],
    'tear': ['tear', 'tore', 'torn', 'tearing'],
    'tell': ['tell', 'told', 'told', 'telling'],
    'think': ['think', 'thought', 'thought', 'thinking'],
    'throw': ['throw', 'threw', 'thrown', 'throwing'],
    'thrust': ['thrust', 'thrust', 'thrust', 'thrusting'],
    'understand': ['understand', 'understood', 'understood', 'understanding'],
    'wake': ['wake', 'woke', 'woken', 'waking'],
    'wear': ['wear', 'wore', 'worn', 'wearing'],
    'weep': ['weep', 'wept', 'wept', 'weeping'],
    'win': ['win', 'won', 'won', 'winning'],
    'wind': ['wind', 'wound', 'wound', 'winding'],
    'withdraw': ['withdraw', 'withdrew', 'withdrawn', 'withdrawing'],
    'write': ['write', 'wrote', 'written', 'writing']
}
def correct_verb_tense(token):
    base_form = lemmatizer.lemmatize(token.text, 'v').lower()
    past_form = base_form + 'ed' if token.text[-1] != 'e' else base_form + 'd'
    present_participle_form = base_form + 'ing'  if token.text[-1] != 'e' else base_form + 'ing'
    third_person_singular_form = base_form + 's'

    irregular_base_forms = [irregular_words[word][0] for word in irregular_words]
    irregular_past_forms = [irregular_words[word][1] for word in irregular_words]

    # Check if the verb is irregular and is already in the required form
    if token.text.lower() in irregular_base_forms:
        index = irregular_base_forms.index(token.text.lower())
        if irregular_words[token.text.lower()] == [base_form, irregular_past_forms[index], present_participle_form, third_person_singular_form]:
            # Verb is already in the correct form, no change needed
            return base_form, past_form, present_participle_form, third_person_singular_form

    if token.tag_ in ['VB', 'VBP']:
        return base_form, base_form, present_participle_form, third_person_singular_form
    elif token.tag_ == 'VBD':
        return past_form, past_form, past_form, past_form
    elif token.tag_ == 'VBG':
        return present_participle_form, present_participle_form, present_participle_form, present_participle_form
    elif token.tag_ == 'VBZ':
        return third_person_singular_form, third_person_singular_form, present_participle_form, third_person_singular_form
    elif token.tag_ in ['VB', 'MD'] and token.head.text.lower() == 'will':
        return base_form, base_form, base_form + 'ing', base_form + 's'
    elif token.tag_ == 'VBN':
        return past_form, past_form, past_form, past_form
    else:
        return base_form, base_form, present_participle_form, third_person_singular_form

def correct_paragraph(paragraph):
    doc = nlp(paragraph)
    corrected_tokens = []

    for token in doc:
        if token.pos_ == 'VERB':
            base, _, _, _ = correct_verb_tense(token)
            corrected_tokens.append(base)
        else:
            corrected_word = spell.correction(token.text)
            corrected_tokens.append(corrected_word if corrected_word is not None else token.text)

    corrected_text = ' '.join(corrected_tokens)
    corrected_text = re.sub(r'\s+([.,!?])', r'\1', corrected_text)
    corrected_text = corrected_text.replace(" '", "'").replace('  ', ' ').replace(' "','"')
    corrected_text = corrected_text.replace('“ ', '“').replace(' ”', '”').replace('( ', '(').replace(' )', ')')
    corrected_text = corrected_text.replace('it\'s', 'it\'s').replace('dont', "don't").replace('wont', "won't")
    return corrected_text

def correct_text(text):
    paragraphs = text.split('\n')
    corrected_paragraphs = [correct_paragraph(paragraph) for paragraph in paragraphs]
    corrected_text = '\n'.join(corrected_paragraphs)
    return corrected_text
