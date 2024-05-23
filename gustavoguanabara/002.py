import math
"""num = int(input())
raiz = int(math.sqrt(num))
print("A raiz de {} é igual a {} " .format(num,raiz)

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjascente: "))
hi = math.hypot(co,ca)
print("O valor da hipotenusa é {:.2f} ".format(hi))"""

angulo = float(input(("Digite o ângulo que você deseja: ")))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}" .format(angulo,seno))
print("O ângulo de {} tem o COSSENO de {:.2f}" .format(angulo,cos))
print("O ângulo de {} tem a TANGENTE de {:.2f}" .format(angulo,tan))