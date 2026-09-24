# Um matemático italiano da idade média conseguiu modelar o ritmo de crescimento da população de coelhos (1) 
# através de uma seqüência de números naturais que passou a ser conhecida como seqüência de Fibonacci (2).

n = int(input('Digite o valor de n: '))

F = 1
Fant = 0
Finic = 1
seq = []

while Finic <= n:
    if Finic == 1:
        F = 1
    
    if Finic != 1:
        F = Fant + F
        Fant = F - Fant

    seq.append(F)
    Finic = Finic + 1

print(seq)
print('Sequência de Fibonacci até Fn.\n')