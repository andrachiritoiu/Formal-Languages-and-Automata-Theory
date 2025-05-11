# Tema-lab3
# Chirițoiu Andra-Florentina, grupa 134
#1.Transformarea automat finit -> expresie regulata
# Input: Un automat finit oarecare
# Output: Expresia regulata echivalenta cu automatul dat ca intrare
# ab*ab*a

# class NFA:
#     def __init__(self):
#         self.states = ['q1','q2','q3','q4','q5','q6']
#         self.alphabet=['a','b','lambda']
#         self.initial_state = 'q1'
#         self.final_states = ['q6']
#         self.transition = {
#             'q1': {'q1':[],'q2':['a'],'q3':[],'q4':[],'q5':[],'q6':[]},
#             'q2': {'q1':[],'q2':['b'],'q3':['lambda'],'q4':[],'q5':[],'q6':[]},
#             'q3': {'q1':[],'q2':[''],'q3':[],'q4':['a'],'q5':[],'q6':[]},
#             'q4': {'q1':[],'q2':[],'q3':[],'q4':['b'],'q5':['lambda'],'q6':[]},
#             'q5': {'q1':[],'q2':[],'q3':[],'q4':[],'q5':[],'q6':['a']},
#             'q6': {'q1':[],'q2':[],'q3':[],'q4':[],'q5':[],'q6':[]}
#         }
#
#     def concat(self):
#         for cheie in self.transition:
#             for transition in self.transition[cheie]:
#                 new_trans = ''
#                 if transition!='lambda':
#                     ok=0
#                     for simbol in self.transition[cheie][transition]:
#                         if(ok != 0):
#                             new_trans += '+'
#                         new_trans+=simbol
#                         ok+=1
#             if new_trans!='':
#                 self.transition[cheie][transition]=[new_trans]
#
#         # print(self.transition)
#
#     def verif_stare_initiala(self):
#         ok=0
#         # verif daca este o sageata spre starea initiala
#         for cheie in self.transition:
#             if( self.transition[cheie][self.initial_state]!=[]):
#                 ok=1
#         # si daca starea initiala este si finala
#         if self.initial_state in self.final_states or ok==1:
#             # adaugam o noua stare initiala
#             self.transition['q0']={}
#             self.transition['q0'][self.initial_state]='lambda'
#             self.initial_state='q0'
#
#         self.transition = dict(sorted(self.transition.items()))
#         # print(self.transition)
#
#     def verif_stare_finala(self):
#         ok = 0
#         sageata_finala=set()
#         # verif daca este o sageata care pleaca din starea finala
#         for cheie in self.final_states:
#             for state in self.transition[cheie]:
#              if self.transition[cheie][state]!=[]:
#                  sageata_finala.add(cheie)
#                  ok = 1
#         if len(sageata_finala) >= 1:
#             # adaugam o noua stare finala
#             for cheie in sageata_finala:
#                 self.transition[cheie]['qf'] = {}
#                 self.transition[cheie]['qf'] = 'lambda'
#             self.transition['qf']={}
#
#         # si daca sunt mai multe stari finale
#         if len(self.final_states) >= 2:
#             # adaugam o noua stare finala
#             for cheie in self.final_states:
#                 self.transition[cheie]['qf'] = {}
#                 self.transition[cheie]['qf'] = 'lambda'
#             self.transition['qf'] = {}
#             self.final_states = ['qf']
#
#         self.transition = dict(sorted(self.transition.items()))
#         # print(self.transition)
#
#
#     def eliminare_stari(self):
#         import copy
#         self.new_transition = dict()
#         self.new_transition = copy.deepcopy(self.transition)
#         print(self.new_transition)
#         for cheie in self.transition:
#             if cheie!=self.initial_state and cheie!=self.final_states:
#                 # stare de eliminat
#                 new_transition="".join(self.new_transition[self.initial_state][cheie])
#                 if self.transition[cheie]!={} and self.transition[cheie][cheie] != []:
#                     new_transition += ''.join(self.transition[cheie][cheie])
#                     new_transition += "*"
#                 # print(new_transition)
#
#                 for state in self.transition[cheie]:
#                     if state!=cheie:
#                         if  self.new_transition[cheie][state]!=[]:
#                             if   'lambda' not in self.new_transition[cheie][state]:
#                                 if  len(self.new_transition[cheie][state][0])==1:
#                                     self.new_transition[cheie][state]=new_transition+self.new_transition[cheie][state][0]
#                                 else:
#                                     self.new_transition[cheie][state] = new_transition + "("+ self.new_transition[cheie][state][0] + ")"
#                             else:
#                                 self.new_transition[cheie][state] = new_transition
#
#                 self.new_transition[self.initial_state] = self.new_transition[cheie]
#                 self.new_transition.pop(cheie)
#
#                 # elimin starea din toate dicitionarele
#                 for state in self.new_transition:
#                     if cheie in self.new_transition[state]:
#                         self.new_transition[state].pop(cheie)
#
#                 # print(self.new_transition)
#
#                 self.transition = copy.deepcopy(self.new_transition)
#
#         return new_transition
#
#
# if __name__ == "__main__" :
#     nfa = NFA()
#     nfa.concat()
#     nfa.verif_stare_initiala()
#     nfa.verif_stare_finala()
#     print(nfa.eliminare_stari())


# 2. Transformare expresie regulata-> automat finit
# Input: o expresie regulata oarecare
# E = (a|b)*abb
# Output:  automatul finit echivalent expresiei regulate date la intrare
# (automatul nu trebuie sa fie neaparat determinist). Intrucat un automat
# poate avea diverse forme echivalente, este acceptata orice solutie
# echivalenta cu automatul finit determinist minimal corespunzator
# expresiei regulate.


class REGEX:
    def __init__(self):
        self.regex="(a|b)*abb"
        self.states = []
        self.alphabet = []
        self.initial_state = ''
        self.final_states = []
        self.transition = {}
        self.simboluri=['|', '*', '(', ')']


    def NFA(self):
        self.initial_state='q0'
        self.states=self.initial_state
        self.transition[self.initial_state]={}
        last_index=0
        last_transition=self.initial_state
        new_state=last_transition
        i=0
        while i<len(self.regex):
            if self.regex[i]=='(':
                j=i
                while self.regex[j]!=')':
                    j+=1

                # fara paranteze
                transition=self.regex[i+1:j]
                i = j
                new_state = 'q' + str(last_index + 1)
                last_index += 1
                self.states += new_state
                self.transition[last_transition] = {}
                for k in transition:
                    if k not in self.simboluri:
                        if k not in self.alphabet:
                            self.alphabet+=k

                        if new_state in self.transition[last_transition]:
                            self.transition[last_transition][new_state].append(k)
                        else:
                            self.transition[last_transition][new_state]=[k]

                # print(self.transition)
                i+=1

            elif self.regex[i]=='*':
                self.transition[new_state] = {}
                self.transition[new_state][last_transition]=["lambda"]
                if 'lambda' not in self.alphabet:
                    self.alphabet+="lambda"
                i+=1
                last_transition=new_state
                # print(self.transition)

            else:
                new_state = 'q' + str(last_index + 1)
                last_index += 1
                self.states += new_state
                self.transition[new_state] = {}


                if self.regex[i] not in self.simboluri:
                    if self.regex[i] not in self.alphabet:
                        self.alphabet += self.regex[i]

                    if new_state in self.transition[last_transition]:
                        self.transition[last_transition][new_state].append(self.regex[i])
                    else:
                        self.transition[last_transition][new_state] = [self.regex[i]]

                    last_transition=new_state
                    self.final_states=new_state
                    i+=1

        return self.transition

if __name__ == "__main__" :
    nfa = REGEX()
    print("Expresia regulata este: ", end=" ")
    print(nfa.regex)
    print("Automatul finit echivalent oentru acesta expresie regulata este: ")
    print(nfa.NFA())



# #forma poloneza
# class REGEX:
#     def __init__(self):
#         self.regex="a*(a+b+((ab*)(l+a)))"
#         self.precedence={'+':1, '.':2, '*':3}
#         self.new_regex=[]
#         self.simboluri=['+', '*', '(', ')', '.']
#         self.stack=[]
#         self.regex_transf=""
#         self.polishform=""
#         self.initial_state = ''
#         self.final_states = []
#         self.transition = {}
#
#     def concat(self):
#         for i in range(len(self.regex)-1):
#             # ab
#             if self.regex[i] not in self.simboluri and self.regex[i+1] not in self.simboluri:
#                 self.new_regex.append(self.regex[i])
#                 self.new_regex.append(".")
#             # a(
#             elif self.regex[i] not in self.simboluri and self.regex[i+1]=="(":
#                 self.new_regex.append(self.regex[i])
#                 self.new_regex.append(".")
#             #)a  *a
#             elif self.regex[i] in [")","*"] and self.regex[i+1] not in self.simboluri:
#                 self.new_regex.append(self.regex[i])
#                 self.new_regex.append(".")
#             # )(  *(
#             elif self.regex[i] in [")", "*"] and self.regex[i + 1] in ["(", "*"]:
#                 self.new_regex.append(self.regex[i])
#                 self.new_regex.append(".")
#             else:
#                 self.new_regex.append(self.regex[i])
#
#         self.new_regex.append(self.regex[-1])
#
#         self.regex_transf="".join(self.new_regex)
#         # print(self.regex_transf)
#
#         self.regex_transf=self.regex_transf[::-1]
#
#         self.regex=self.regex_transf
#         self.new_regex=[]
#
#         for i in range(len(self.regex)):
#             if self.regex[i]=="(":
#                 self.new_regex.append(")")
#             elif self.regex[i]==")":
#                 self.new_regex.append("(")
#             else:
#                 self.new_regex.append(self.regex[i])
#
#         self.regex_transf="".join(self.new_regex)
#         print(self.regex_transf)
#
#     def polish_notation(self):
#         for i in self.regex_transf:
#             if i == '(':
#                 self.stack.append(i)
#             elif i==')':
#                 while self.stack and self.stack[-1]!='(':
#                     self.polishform+=self.stack.pop()
#                 self.stack.pop()
#
#             elif i=='+' or i=="*" or i=='.':
#                 while self.stack and  self.stack[-1]!='(' and self.precedence[self.stack[-1]]>=self.precedence[i]:
#                     self.polishform += self.stack.pop()
#                 self.stack.append(i)
#             else:
#                 self.polishform+=i
#
#         # golim stiva
#         while self.stack:
#             self.polishform+=self.stack.pop()
#
#         self.polishform=self.polishform[::-1]
#         print(self.polishform)
#
#
# if __name__ == "__main__" :
#     nfa = REGEX()
#     nfa.concat()
#     nfa.polish_notation()


