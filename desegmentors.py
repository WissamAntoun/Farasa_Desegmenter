def desegmentword(orig_word: str) -> str:
    """
    Word segmentor that takes a Farasa Segmented Word and removes the '+' signs
    
    Example:
    >>> desegment("ال+يومي+ة")
    اليومية
    """
    word = orig_word.replace("ل+ال+","لل")
    if "ال+ال" not in orig_word:
        word = word.replace("ل+ال","لل")
    word = word.replace("+","")
    word = word.replace("للل","لل")
    return word

def desegment_line(line: str ,sep: str = ' ') -> str:
    """
    Simple wrapper over `desegmentword` that splits a string by the sep character

    """
    return " ".join([desegmentword(word) for word in line.split(sep)])

def desegment_arabert(line: str) -> str:
    """
    Use this function if sentence tokenization was done using 
    `from arabert.preprocess_arabert import preprocess` with Farasa enabled

    AraBERT segmentation using Farasa adds a space after the '+' for prefixes,
    and after before the '+' for suffixes

    Example:
    >>> desegment_arabert('ال+ دراس +ات')
    الدراسات
    """
    line = line.replace("+ ","+")
    line = line.replace(" +","+")
    return desegment_line(line)


