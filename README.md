# Farasa Desegmenter (Unsegment)
Simple Script to undo Farasa Segmentation

Tested on 106K words
Error rate:  0.074%
Error Count:  79

# Functions docs:

To import the functions use `from desegmentors import *`

* `desegmentword`: Word segmentor that takes a Farasa Segmented Word and removes the '+' signs    
```python
>>> desegment("ال+يومي+ة")
اليومية
>>> desegment("ل+ال+يومي+ة") #Handles Lam + Al-Ataarif
لليومية
```

* `desegment_line`: Simple wrapper over `desegmentword` that splits a string by the `sep` character
```python
>>> desegment_line('ال+دراس+ات ال+نظري+ة ل+ال+تصميم ال+حديث')
الدراسات النظرية للتصميم الحديث
````

* `desegment_arabert`: Use this function if sentence tokenization was done using `from arabert.preprocess_arabert import preprocess` with Farasa enabled.
AraBERT segmentation using Farasa adds a space after the '+' for prefixes, and after before the '+' for suffixes
```python
>>> desegment_arabert("ال+ دراس +ات ال+ نظري +ة ل+ ال+ تصميم ال+ حديث")
الدراسات النظرية للتصميم الحديث
```