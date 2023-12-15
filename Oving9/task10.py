import numpy as np

M=np.matrix([[0.742968407799, -0.358528304356, 0.494764366239, 0.323645446383],
[-0.430113787307, -0.158029298865, 1.44639897736, 0.946148256866],
[-0.471841853357, -1.14981041121, 2.47681915989, 1.03794009921],
[-0.499662304424, -1.21760483016, 1.68027872501, 1.98923433464]])

v=np.matrix([[9],[8],[7],[6]]); # En tilfeldig vektor
lambda_est = 0; # En initiell verdi for estimatet til den største egenverdien.
lambda_est_gammel = 1; # en hjelpevariabel.
while abs(lambda_est - lambda_est_gammel) > 0.0001: #Se beskrivelsen over.
    v_gammel = v; # En hjelpevariabel som lagrer siste estimat av egenvektoren.
    v=np.matmul(M,v); #
    lambda_est_gammel = lambda_est;
    lambda_est=v[0]/v_gammel[0];
    print("Estimat for største egenverdi: ",lambda_est);
    print("Estimat for tilhørende egenvektor: ");
    print(v);
    print();
    v=v/np.linalg.norm(v);