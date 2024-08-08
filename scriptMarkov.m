clear; close all;

%Inizializzo la matrice di transizione A
A=[8/17, 9/28, 8/11;
   0, 9/28, 2/11;
   9/17, 5/14, 1/11];

%Inizialializzo lo stato iniziale con valori "pseudocausali"
x0=rand(3,1);

%Normalizzo lo stato iniziale per renderlo stocastico
x0=x0/sum(x0);
