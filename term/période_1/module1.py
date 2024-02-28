# Créé par n.mohamed, le 05/09/2022 en Python 3.7
import copy
liste1=[i for i in range(5)]
x=liste1[:]
print(liste1,x)

x=[[1,2],[3,4]]
y=x[:]
"""commande pour liste"""

print(y)

y[0][1]=66



x=[[1,2],[3,4]]
y=copy.deepcopy(x
)
"""commande pour liste de liste"""


y[0][1]=66

print(x,y)

message = 'BioInfo'
msg_lst = message.split()
print([[m.upper(), len(m)] for m in msg_lst])

seq = 'ABCDEFGHIJKL'

seq_split = [seq[i:i+1] for i in range(1, 5, 2)]
print(seq_split)

