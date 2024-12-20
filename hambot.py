#!/usr/bin/env python
# coding: utf-8

# # Hamlet Sentence Generator
# 
# Who needs Shakespeare when we've got Python? In the following series of exercises, we will create a function that will generate Shakesepearan-sounding phrases. All of the words in our phrase generator come from Act 3, Scene 1 of Shakespeare's Hamlet. 
# 
# But we won't just be stringing random words together. To make our phrases sound (slightly) coherent, every new word in our phrase will be a word that followed the previous word in the original Shakespearean text.
# 
# We will accomplish this in three steps. First, we will tidy the text of the scene, breaking each sentence into an ordered list of the words in that sentence. Second, we will create a dictionary where the keys are words from the text, and the values are lists of the words that immediately follow the key words in the dialogue. Finally,  we will create a phrase generator that will use that dictionary by starting with a key word, randomly selecting a word from the list of words that follows it, adding that word to our phrase, and repeating the process.

# Here's the text of Hamlet Act 3, Scene 1. 

# In[11]:


hamlet_text = """

And can you by no drift of circumstance Get from him why he puts on this confusion Grating so harshly all his days of 
quiet With turbulent and dangerous lunacy? He does confess he feels himself distracted. But from what cause he will by 
no means speak. Nor do we find him forward to be sounded But with a crafty madness keeps aloof When we would bring 
him on to some confession Of his true state. Did he receive you well? Most like a gentleman. But with much forcing of 
his disposition. Niggard of question. but of our demands Most free in his reply. Did you assay him? To any pastime? 
Madam it so fell out that certain players We o'er-raught on the way. of these we told him. And there did seem in him a 
kind of joy To hear of it. they are about the court And as I think they have already order This night to play before 
him. 'Tis most true. And he beseech'd me to entreat your majesties To hear and see the matter. With all my heart. and 
it doth much content me To hear him so inclined. Good gentlemen give him a further edge And drive his purpose on to 
these delights. We shall my lord. Sweet Gertrude leave us too. For we have closely sent for Hamlet hither That he as 
'twere by accident may here Affront Ophelia. Her father and myself lawful espials Will so bestow ourselves that seeing 
unseen We may of their encounter frankly judge And gather by him as he is behaved If 't be the affliction of his love 
or no That thus he suffers for. I shall obey you. And for your part Ophelia I do wish That your good beauties be the 
happy cause Of Hamlet's wildness. so shall I hope your virtues Will bring him to his wonted way again To both your 
honours. Madam I wish it may. Ophelia walk you here. Gracious so please you We will bestow ourselves. Read on this 
book. That show of such an exercise may colour Your loneliness. We are oft to blame in this 'Tis too much proved that 
with devotion's visage And pious action we do sugar o'er The devil himself. O 'tis too true! How smart a lash that 
speech doth give my conscience! The harlot's cheek beautied with plastering art Is not more ugly to the thing that 
helps it Than is my deed to my most painted word. O heavy burthen! I hear him coming. let's withdraw my lord. To be 
or not to be. that is the question. Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous 
fortune Or to take arms against a sea of troubles And by opposing end them? To die. to sleep. No more. and by a sleep 
to say we end The heart-ache and the thousand natural shocks That flesh is heir to 'tis a consummation Devoutly to be 
wish'd. To die to sleep. To sleep. perchance to dream. ay there's the rub. For in that sleep of death what dreams may 
come When we have shuffled off this mortal coil Must give us pause. there's the respect That makes calamity of so long 
life. For who would bear the whips and scorns of time The oppressor's wrong the proud man's contumely The pangs of 
despised love the law's delay The insolence of office and the spurns That patient merit of the unworthy takes When he 
himself might his quietus make With a bare bodkin? who would fardels bear To grunt and sweat under a weary life But 
that the dread of something after death The undiscover'd country from whose bourn No traveller returns puzzles the 
will And makes us rather bear those ills we have Than fly to others that we know not of? Thus conscience does make 
cowards of us all. And thus the native hue of resolution Is sicklied o'er with the pale cast of thought And 
enterprises of great pith and moment With this regard their currents turn awry And lose the name of action. Soft you 
now! The fair Ophelia! Nymph in thy orisons Be all my sins remember'd. Good my lord How does your honour for this 
many a day? I humbly thank you. well well well. My lord I have remembrances of yours That I have longed long to 
re-deliver. I pray you now receive them. No not I. I never gave you aught. My honour'd lord you know right well you 
did. And with them words of so sweet breath composed As made the things more rich. their perfume lost Take these 
again. for to the noble mind Rich gifts wax poor when givers prove unkind. There my lord. Ha ha! are you honest? My 
lord? Are you fair? What means your lordship? That if you be honest and fair your honesty should admit no discourse 
to your beauty. Could beauty my lord have better commerce than with honesty? Ay truly. for the power of beauty will 
sooner transform honesty from what it is to a bawd than the force of honesty can translate beauty into his likeness. 
this was sometime a paradox but now the time gives it proof. I did love you once. Indeed my lord you made me believe 
so. You should not have believed me. for virtue cannot so inoculate our old stock but we shall relish of it. I loved 
you not. I was the more deceived. Get thee to a nunnery. why wouldst thou be a breeder of sinners? I am myself 
indifferent honest. but yet I could accuse me of such things that it were better my mother had not borne me. I am 
very proud revengeful ambitious with more offences at my beck than I have thoughts to put them in imagination to give 
them shape or time to act them in. What should such fellows as I do crawling between earth and heaven? We are arrant 
knaves all. believe none of us. Go thy ways to a nunnery. Where's your father? At home my lord. Let the doors be shut 
upon him that he may play the fool no where but in's own house. Farewell. O help him you sweet heavens! If thou dost 
marry I'll give thee this plague for thy dowry. be thou as chaste as ice as pure as snow thou shalt not escape 
calumny. Get thee to a nunnery go. farewell. Or if thou wilt needs marry marry a fool. for wise men know well enough 
what monsters you make of them. To a nunnery go and quickly too. Farewell. O heavenly powers restore him! I have 
heard of your paintings too well enough. God has given you one face and you make yourselves another. you jig you 
amble and you lisp and nick-name God's creatures and make your wantonness your ignorance. Go to I'll no more on't. 
it hath made me mad. I say we will have no more marriages. those that are married already all but one shall live. the 
rest shall keep as they are. To a nunnery go. O what a noble mind is here o'erthrown! The courtier's soldier's 
scholar's eye tongue sword. The expectancy and rose of the fair state The glass of fashion and the mould of form The 
observed of all observers quite quite down! And I of ladies most deject and wretched That suck'd the honey of his 
music vows Now see that noble and most sovereign reason Like sweet bells jangled out of tune and harsh. That 
unmatch'd form and feature of blown youth Blasted with ecstasy. O woe is me To have seen what I have seen see what I 
see! Love! his affections do not that way tend. Nor what he spake though it lack'd form a little Was not like madness. 
There's something in his soul O'er which his melancholy sits on brood. And I do doubt the hatch and the disclose Will 
be some danger. which for to prevent I have in quick determination Thus set it down. he shall with speed to England 
For the demand of our neglected tribute Haply the seas and countries different With variable objects shall expel 
This something-settled matter in his heart Whereon his brains still beating puts him thus From fashion of himself. 
What think you on't? It shall do well. but yet do I believe The origin and commencement of his grief Sprung from 
neglected love. How now Ophelia! You need not tell us what Lord Hamlet said. We heard it all. My lord do as you 
please. But if you hold it fit after the play Let his queen mother all alone entreat him To show his grief. let her 
be round with him. And I'll be placed so please you in the ear Of all their conference. If she find him not To England 
send him or confine him where Your wisdom best shall think. It shall be so. Madness in great ones must not unwatch'd 
go.

"""


# Part1: Let's create a list of lists, named `hamsplits`, such that `hamsplits[i]` is a list of all the words in the `i`-th sentence of the text. The sentences should be stored in the order that they appear, and so should the words within each sentence.
# 
# Regarding how to break up the text into sentences and how to store the words, the guidelines are as follows:
# 
# * Sentences end with `'.'`, `'?'`, and `'!'`.
# * You should convert all letters to lowercase.
# * For each word, strip out any punctuation.
# 
# For instance, in the text above, the first and last sentences would be:
# 
# ```python
# hamsplits[0] == ['and', 'can', 'you', 'by', ..., 'dangerous', 'lunacy']
# hamsplits[-1] == ['madness', 'in', 'great', ..., 'not', 'unwatchd', 'go']
# ```

# In[12]:


hamsplitss = []
ht = ""

for c in hamlet_text.lower():
    if c in [".", "?", "!"]:
        ht += "|"
    elif c.isalpha() or c.isspace():
        ht += c

ht = "".join(ht.split("\n")).split("|")
for sentence in ht:
    hamsplitss.append(sentence.split())
    
hamsplits = hamsplitss[:-1]
hamsplits[1:3]


# Part 2: Now let's create a sequential pairs dictionary, called `hamdict`, with `key` being each word in `hamsplits` and `value` being the list of words that immediately following it. If no words ever follow the given word, then it should not appear as a key in `hamdict`.
# 
# For example, if `hamsplits == [ ['i', 'love', 'to', 'code'], ['gotta', 'love', 'python'] ]`, then
# 
# ```python
#     hamdict == {'i': ['love'], 'love': ['to', 'python'], 'to': ['code'], 'gotta': ['love']}
# ```
# 
# Notice that no words ever follow `'code'` nor `'python'`; therefore, they do not appear as keys in `hamdict`.

# In[13]:


# We now want to make a sequential pairs dictionary. 
from collections import defaultdict
hamdict = defaultdict(list)
for sen_words in hamsplits:
    for index in range(len(sen_words)):
        if int(index) + 1 in range(len(sen_words)):
            hamdict[sen_words[index]].append(sen_words[int(index) + 1])

        
hamdict = dict(hamdict)
hamdict['i']


# Part 3: Now it's time to build our folio! 
# 
# Below, write a function, `Hambot`, that takes a starter word from your dictionary and builds a Shakespearean-sounding phrase, returning it as a string. 
# 
# Our function should randomly select one of the words that follows your starter word, add it to our phrase, and then repeat the process with this new word. This process should continue until either your function reaches a word that is not a key in the dictionary, or the phrase reaches the specified length. The function should then return this phrase as a string (all lowercase, with no punctuation).
# 
# The function takes two optional parameters, `length` and `starter`. `length` is an integer which is the number of words long your output phrase should be. If the `length` parameter is not supplied, your function should default to attempting to produce a 5-word phrase.
# 
# `starter` is the first word to start the Shakespearean phrase.  If `starter` is not supplied, the function should choose a word at random from among the keys in your dictionary.
# 
# As an example, if your function starts with the word "some," the second word in your phrase would be either "confession" or "danger," the two words that follow "some." If it selected "confession," the third word would be "of," which is the only word that follows "confession." The fourth word would be randomly chosen from the 38 words that follow "of." In other words,
# 
# ```python
# hambot(4, "some")
# ```
# 
# .... should return a string like, `"some confession of circumstance"`.

# In[14]:


import random
def hambot(length = 5, starter = False):
    try:
        if starter not in hamdict.keys():
            starter == False

        if starter == False:
            starter = random.choice(random.choice(list(hamdict.values())))

        phrase = [starter]
        for index in range(int(length)-1):
            phrase.append(random.choice(hamdict[phrase[index]]))
    except KeyError:
        new_word = random.choice(random.choice(list(hamdict.values())))
    
    
    print( (",".join(phrase)).replace(",", " "))

return



