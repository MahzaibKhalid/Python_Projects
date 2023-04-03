from spellchecker import SpellChecker
corrector=SpellChecker()

word = input("Enter a word:")
if word in corrector:
    print("Correct")
else:
    correct_Word= corrector.correction(word)
    print("Correct Spelling is: ",correct_Word)
    