import math as m


# Método da Bissecção

# Método intervalar (para o utilizarmos é necessário fazer um isolamento das raízes)
# utilizado para encontrar a raiz de uma função num determinado intervalo. Método mais simples
# e mais seguro de implementar.
# Neste método, a redução do intervalo é realizada mediante o cálculo da função no ponto médio do intervalo,
# f ((x1 +x2)/2) . Se este valor não for nulo (porque, se fosse o caso, teríamos logo encontrado a raiz "exacta"),
# então ocorrerá necessariamente uma mudança de sinal em uma (e uma só) das metades do intervalo original; a redução
# desejada far-se-á substituindo o intervalo original por essa metade; deste modo, (x1 +x2)/2 substitui x1
# ou x2, conforme o caso, e o processo repete-se.


def bisection(a, b, it, error, function):
    middle = (b + a) / 2
    _it = 0
    while abs(b - a) > error and _it != it:
        # print(a, b, (b + a) / 2, function(a), function(b), function(middle), _it)
        middle = (b + a) / 2
        if function(a) * function(middle) < 0:
            b = middle
        else:
            a = middle
        _it += 1
    # print(a, b, (b + a) / 2, function(a), function(b), function(middle), _it)
    # print("Erro absoluto/Amplitude = {}" .format(a - b))
    # print("Erro relativo = {}" .format((a-b)/middle))
    return middle


# Método da corda

# Método intervalar (para o utilizarmos é necessário fazer um isolamento das raízes)
# utilizado para encontrar a raiz de uma função num determinado intervalo.
# A ideia por trás do método da corda, também chamado método da falsa posição ou regula falsi, é muito
# simples: ao tentar reduzir o intervalo, se um valor extremo for grande (em valor absoluto) e o outro for
# pequeno, então o zero encontra-se, provavelmente mais perto do valor pequeno que do grande. Uma
# maneira simples da implementar este conceito consiste em traçar uma reta que passa pelos pontos
# extremos do intervalo, (x1, f(x1)) e (x2, f(x2)) e utilizá-la como aproximação da função.
# Encontrado este novo ponto, calcula-se o valor f(x) e abandona-se o ponto antigo em que a função tiver
# o mesmo sinal que neste, tal como se fazia na bissecção.


def rope(a, b, it, error, function):
    _it = 0
    w = 0
    while abs(function(a) - function(b)) > error and _it != it:
        w = (a * function(b) - b * function(a)) / (function(b) - function(a))
        print(a, b, w, function(a), function(b), function(w), _it)
        if function(a) * function(w) < 0:
            b = w
        else:
            a = w
        _it += 1
    w = (a * function(b) - b * function(a)) / (function(b) - function(a))
    print(a, b, w, function(a), function(b), function(w), _it)
    return w


# Método de Newton

# Método não intervalar e que portanto necessinta de um guess inicial para começar os cálculos
# O método de Newton parte apenas de um valor plausível, embora eventualmente grosseiramente errado, da raiz
# Conceptualmente, pode ser considerado como apenas uma extensão, ou passagem ao limite, do método da secante
# e tem, portanto, todos os inconvenientes potenciais deste: em termos geométricos, consiste em substituir
# o gráfico da função não pela secante que liga os pontos extremos do intervalo, mas pela tangente no ponto
# considerado, usando o zero desta como nova aproximação à raiz.
# Quando funciona bem, o método da tangente é excelente, até porque, nas vizinhanças da raiz, tende, a
# cada iteração, a dobrar o número de algarismos exactos da solução. Porém, as suas limitações são muitas
# e muito severas.
# Um inconveniente óbvio do método da tangente é o de exigir o conhecimento da derivada da função, e o
# seu cálculo em cada iteração.
# Em suma, trata-se de um método indiscutivelmente útil, mas apenas para usar em terreno muito bem
# conhecido, e sempre com grande precaução.


def newton(guess, function, diff, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        # print(guess, new_guess, function(new_guess), _it)
        guess = new_guess
        new_guess = guess - (function(guess) / diff(guess))
        # _it += 1
    # print(guess, new_guess, function(guess), _it)
    return new_guess


# Método picard-peano

# Método não intervalar e que portanto necessinta de um guess inicial para começar os cálculos
# A ideia básica é a seguinte: suponhamos uma equação f(x) = 0 e, por não sabermos resolvê-la analiticamente,
# transformêmo-la de modo a dar-lhe a forma x = g(x)
# Se, por qualquer processo, tivermos obtido uma aproximação x0 da raiz e a substituirmos no segundo
# membro, obtemos um valor x1 = g(x0) que pode de novo ser utilizado para produzir x2 = g(x1) e assim
# sucessivamente: xn+1 = g(xn)
# Há, pois, para poder utilizar-se o método com segurança, que investigar as condições em que converge.
# Uma simples análise das figuras mostrará facilmente que a condição de convergência corresponde a ser
# |g'(x)| < 1
# Assim, encontrada a função g para um determinado guess, basta-nos aplicar o método que consiste em cada
# iteração obter um novo valor através da equação de convergência: xn+1 = g(xn).


def picard_peano(guess, g, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        # print(new_guess, g(new_guess), _it)
        guess = new_guess
        new_guess = g(guess)
        # _it += 1
    # print(new_guess, g(new_guess), _it)
    return new_guess


# Método de newton -> sistema de equações


def newton_system(guess_x, guess_y, function, gradient, error, it):
    _it = 0
    new_x = guess_x
    new_y = guess_y
    guess_x += error * 10
    guess_y += error * 10
    while (abs(new_x - guess_x) > 0 or abs(new_y - guess_y) > 0) and _it != it:
        # print(new_x, new_y, _it)
        guess_x = new_x
        guess_y = new_y
        new_x = guess_x - ((function[0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - function[1](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)) / (gradient[0][0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - gradient[1][0](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)))
        new_y = guess_y - ((function[1](guess_x, guess_y) * gradient[0][0](guess_x, guess_y) - function[0](guess_x, guess_y) * gradient[1][0](guess_x, guess_y)) / (gradient[0][0](guess_x, guess_y) * gradient[1][1](guess_x, guess_y) - gradient[1][0](guess_x, guess_y) * gradient[0][1](guess_x, guess_y)))
        # _it += 1
    # print(new_x, new_y, _it)
    return new_x, new_y


# Método picard-peano -> sistema de equações


def picard_peano_system(guess_x, guess_y, g, error, it):
    _it = 0
    new_x = guess_x
    new_y = guess_y
    guess_x += error * 10
    guess_y += error * 10
    while (abs(new_x - guess_x) > 0 or abs(new_y - guess_y) > 0) and _it != it:
        # print(new_x, new_y, _it)
        guess_x = new_x
        guess_y = new_y
        new_x = g[0](guess_x, guess_y)
        new_y = g[1](guess_x, guess_y)
        # _it += 1
    return new_x, new_y


# Eliminação gaussiana

# Através do máxima:
#   load("linearalgebra");
#   A: matrix([x,x,x], [x,x,x], [x,x,x]);
#   B: matrix([x], [x], [x]);
#   AB: addcol(A, B);
#   AB: echelon(AB);
#   AB: rowop(AB, linha, coluna, valor); (realizar até condensar, e obtém-se a solução)


# Estabilidade externa:

# DA: zeromatrix(3, 3) + error_da
# DB: zeromatrix(3, 1) + error_db
# X: col(AB, 4)
# BP: DB - DA.X
# AP: addcol(A, BP)
# (repetir o processo de cima (echelon e rowop) até à matriz estar condensada)
# Com a matrix condensada obtemos os valores da estabilidade externa para x, y, z


# Método de Cholesky

# A: matrix([x, x, x], [x, x, x], [x, x, x]);
# B: matrix([x], [x], [x]);
# [p, l, u]: get_lu_factors(lu_factor(transpose(A)));
# b: transpose(u);
# c: transpose(l);
# y: invert(b).B
# x : invert(c).y


# Método de gauss-jacobi

# O método converge porque em cada linha da matriz, o elemento da diagonal principal é superior à soma dos restantes.


def gauss_jacobi_3(x0, y0, z0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error) and _it != it:
        # print(x, y, z, _it)
        x0 = x
        y0 = y
        z0 = z
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x0 - matrix[1][2]*z0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x0 - matrix[2][1]*y0) / matrix[2][2]
        # _it += 1
    return x, y, z


def gauss_jacobi_4(x0, y0, z0, t0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    t = t0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    t0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error) and _it != it:
        # print(x, y, z, t, _it)
        x0 = x
        y0 = y
        z0 = z
        t0 = t
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0 - matrix[0][3]*t0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x0 - matrix[1][2]*z0 - matrix[1][3]*t0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x0 - matrix[2][1]*y0 - matrix[2][3]*t0) / matrix[2][2]
        t = (b[3] - matrix[3][0]*x0 - matrix[3][1]*y0 - matrix[3][2]*z0) / matrix[3][3]
        # _it += 1
    # print(x, y, z, t, _it)
    return x, y, z, t


# Método gauss-seidel

# O método converge porque em cada linha da matriz A, o módulo do elemento da diagonal principal é maior do que a soma
# dos restantes elementos da linha.


def gauss_seidel_3(x0, y0, z0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error) and _it != it:
        # print(x, y, z, _it)
        x0 = x
        y0 = y
        z0 = z
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x - matrix[1][2]*z0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x - matrix[2][1]*y) / matrix[2][2]
        # _it += 1
    return x, y, z


def gauss_seidel_4(x0, y0, z0, t0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    t = t0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    t0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error or abs(t - t0) > error) and _it != it:
        print(x, y, z, t, _it)
        x0 = x
        y0 = y
        z0 = z
        t0 = t
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0 - matrix[0][3]*t0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x - matrix[1][2]*z0 - matrix[1][3]*t0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x - matrix[2][1]*y - matrix[2][3]*t0) / matrix[2][2]
        t = (b[3] - matrix[3][0]*x - matrix[3][1]*y - matrix[3][2]*z) / matrix[3][3]
        _it += 1
    print(x, y, z, t, _it)
    return x, y, z, t


# Método dos trapézios

# 	Para efetuarmos o cálculo numérico do valor de um integral definido, possuimos duas hipóteses:
# 		- Regra dos trapézios (ordem = 2)
# 		- Regra de simpsons (ordem = 4)
# 	Estes métodos consistem em substituir, em cada intervalo, o arco da curva pela sua corda, calculando em seguida a área sob a
# poligonal assim definida. Assim, começando pelo método dos trapézios, temos que o algortimo deste metodo consiste em
# somar o valor da função nos pontos inicial e final do intervalo à soma do dobro do valor da função nos valores entre estes.
# Para obter os valores em que utilizamos o dobro, é necessário definir um 'h' que é o valor que separa dois pontos consecutivos
# (passo de integração). Assim, por exemplo, se h fosse 0.1, iriamos somar o dobro da função em 0.1, com o dobro da função em 0.2, até
# chegar a xf.
#
# 	Um defeito óbvio da regra dos trapézios é o de cometer um erro sistemático em intervalos em que a segunda derivada da
# integranda mantém sinal constante. Para o evitar e para aumentar, na generalidade, a precisão da aproximação, foi
# criado um algoritmo novo, a regra de Simpson que, em vez de substituir a curva pelas cordas definidas por cada par de
# pontos consecutivos, a substitui pelas parábolas definidas por cada trio de pontos consecutivos. Deste modo, o
# algoritmo mais simplificado consiste em fazer exatamente o mesmo que se faz no método dos trapézios fazendo umas
# alterações na soma dos valores intermédios do intervalo. Em vez de se somar o dobro de todos os valores, definimos que
# somamos o quádruplo dos valores designados por ímpares com o dobro dos valores pares. Os elementos ímpares são os
# que são separados por um número ímpar de "h's" da posição inicial, enquanto que os elementos pares são separados por
# um número par de "h's". Por exemplo, a posição x0 + h, difere da posição inicial de apenas um h, logo é um elemento
# ímpar enquanto que o elemento x0 + 2*h difere da posição inicial de 2 h's sendo um elemento par.
#
# 	A ordem destes dois métodos representa a forma como o erro vai variar dependendo do valor do passo a tomar (dependendo
# do h). Ambos os método possuem um método de controlo do erro semelhante, calculamos o valor final para h definindo o
# resultado como S, de seguida calculamos o valor final para h/2, definindo o resultado como S', e fazemos o mesmo para
# h /4, definindo o resultado como S''. Deste modo, podemos concluir que o passo tomado foi o correto (ou seja, que
# utilizamos o melhor valor de h, quando ao fazermos: (S' - S)/(S'' - S') obtemos aproximadamente o valor de 2^ordem do
# método (4 para o método dos trapézios e 16 para o método de simpson)
#
# 	Assim podemos saber qual o erro absoluto esperado efetuando (S'' - S') / (2^(ordem do método) - 1) (com os valores de
# S'' e S' obtidos com o melhor passo a tomar, ou seja, quando no passo definido anteriormente obtemos o valor de
# 2^ordem do método).


def trap(x0, xf, h, function, it):
    _it = 1
    result = function(x0) + function(xf)
    x0 += h
    while x0 != xf and _it != it:
        result += 2*function(x0)
        x0 += h
        # _it += 1
    return result * h/2


def simpson(x0, xf, h, function, it):
    _it = 1
    result = function(x0) + function(xf)
    x0 += h
    while x0 != xf and _it != it:
        if _it % 2:
            result += 4 * function(x0)
        else:
            result += 2 * function(x0)
        x0 += h
        _it += 1
    return result * h/3


def qc_value_s_t(method, h0, x0, xf, function, it, order):
    s = method(x0, xf, h0, function, it)
    s_ = method(x0, xf, h0 / 2, function, it)
    s__ = method(x0, xf, h0 / 4, function, it)
    qc = (s_ - s) / (s__ - s_)
    print(s, h0)
    print(s_, h0/2)
    print(s__, h0/4)
    while int(qc + 0.5) != 2**order:
        print(h0)
        h0 /= 2
        s = method(x0, xf, h0, function, it)
        s_ = method(x0, xf, h0 / 2, function, it)
        s__ = method(x0, xf, h0 / 4, function, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


# Cubatura


# Através da regra dos trapézios

def cubatura_t(x0, xf, y0, yf, function):
    hx = (xf - x0) / 2
    hy = (yf - y0) / 2
    soma_vertices = function(xf, y0) + function(xf, yf) + function(x0, y0) + function(x0, yf)
    soma_medios = function((xf - x0) / 2, y0) + function((xf - x0) / 2, yf) + function(x0, (yf - y0) / 2) + function(xf, (yf - y0) / 2)
    centro = function((xf - x0) / 2, (yf - y0) / 2)
    result = (hx * hy) / 4 * (soma_vertices + 2*soma_medios + 4*centro)
    print(result)


# As fórmulas da cubatura aplicam-se ao cálculo de integrais duplos. (através da regra de simpsons)


def cubatura_s(x0, xf, y0, yf, function):
    hx = (xf - x0) / 2
    hy = (yf - y0) / 2
    soma_vertices = function(xf, y0) + function(xf, yf) + function(x0, y0) + function(x0, yf)
    soma_medios = function((xf - x0) / 2, y0) + function((xf - x0) / 2, yf) + function(x0, (yf - y0) / 2) + function(xf, (yf - y0) / 2)
    centro = function((xf - x0) / 2, (yf - y0) / 2)
    result = (hx * hy) / 9 * (soma_vertices + 4*soma_medios + 16*centro)
    print(result)


# Método de Euler

# Este método elementar de integração numérica de equações diferenciais é conhecido por método de Euler
# e corresponde, obviamente, em termos analíticos, a utilizar a fórmula dos acréscimos finitos, isto é, um
# desenvolvimento em série de Taylor limitado à primeira ordem.

# O algoritmo para o método de Euler é então:
#   1. Calcular o incremento de y usando y'n que é a inclinação da curva no ponto (xn, yn), e ∆xn,
#       o incremento de x no intervalo n: ∆yn = f(xn, yn) * ∆xn
#   2. Calcular o ponto seguinte: xn+1 += ∆xn and yn+1 += ∆yn
# e repetir esses passos até cobrir por completo o intervalo que nos interessa.

# Trata-se, portanto, de um método de primeira ordem, no sentido de que o erro cometido no cálculo de y
# é proporcional a h, se este for suficientemente pequeno.
# Poderemos também aqui aplicar o critério do quociente de convergência, aplicado agora intervalo a
# intervalo com h = 2*h' = 4*h''. Em que: (S' - S)/(S'' - S') ~ 2
# E o erro absoluto = S'' - S'

# Resulta do que ficou dito que o método de Euler, embora extremamente simples de implementar e de
# controlar conceptualmente, tem muito pequena precisão (é de primeira ordem) e dá, portanto, origem a
# cálculos extremamente longos.

# Por outro lado, deve também ter ficado claro que a pequena precisão resulta da acumulação de atrasos
# nos intervalos em que o sinal da curvatura se mantém; a razão desta característica desfavorável prende-se
# claramente com o facto de usarmos, ao longo de cada passo, um valor da derivada que só vale para o seu
# extremo inicial.


def euler(x0, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        # print(x0, y, _it)
        y += function(x0, y) * h
        x0 += h
        # _it += 1
    # print(x0, y, _it)
    return y


# Runge-kutta

# Ao contrário dos métodos do tipo preditor-corrector, os métodos do tipo Runge-Kutta não dispõem do conforto um tanto
# duvidoso de uma "fórmula"para o erro, mas são mais expeditos ao nível da programação, nomeadamente porque não exigem
# técnicas separadas para o arranque (que, aliás, não ocorre apenas no início do intervalo, mas de todas as vezes que é
# necessários diminuir o passo).


# Rk2

# No caso mais simples, um método de Runge-Kutta de segunda ordem, muitas vezes designado por RK2,
# pode visualiza-se do seguinte modo (o raciocínio formal que lhe está subjacente não cabe no escopo do
# nosso curso):
#       1. Começa-se por calcular y' no início do intervalo: y'n = f(xn, yn)
#       2. A partir daí constrói-se uma estima de y' no meio do intervalo: y'a = f(xn + ∆xn/2, yn + ∆yn/2 * y'n)
#       3. Calcular o incremento de y usando y', e ∆xn, o incremento de x no intervalo n: ∆yn = y'a * ∆xn
#       4. Calcular o ponto seguinte: yn+1 = yn + ∆yn | xn+1 = xn + ∆xn
# e repetir esses passos até cobrir por completo o intervalo que nos interessa.

# A validade do valor de h escolhido em cada passo, deve utilizar-se a técnica do quociente de convergência, usando três
# cálculos de y para h, h/2, h/4 e verificando se a razão das diferenças sucessivas é aproximadamente igual a 2
# levantado à ordem do método (2^2 = 4), e, quando ele for cumprido, poderemos estimar o erro absoluto:
# erro = (S'' - S') / 3 (3 = 2^ordem - 1).


def rk2(x0, xf, y0, function, h, error, it):
    _it = 0
    while abs(xf - x0) > error and _it != it:
        # print(x0, y0, _it)
        y0 += h*function(x0 + h / 2, y0 + (h / 2) * function(x0, y0))
        x0 += h
        # _it += 1
    return y0


# Rk4

# Este método consiste em:
#       1. Começa-se por, usando y'n no início do passo de integração, calcular uma primeira estima δ1 para o incremento
#           de ∆yn: δ1 = ∆xn * f (xn , yn)
#       2. A partir desta estima, calcula-se uma primeira estima de y' no meio do passo e, a partir deste valor, uma
#           segunda estima δ2 para o incremento de ∆yn : δ2 = ∆xn * f(xn + ∆xn/2, yn + δ1/2)
#       3. Calcula-se uma segunda estima de y'n no meio do passo, usando a anterior, e a partir deste valor, uma
#           terceira estima δ3 para o incremento de ∆yn : δ3 = ∆xn * f(xn + ∆xn/2, yn + δ2/2)
#       4. Finalmente, obtém-se uma última estima de y'n no fim do passo, usando a anterior, e a partir deste valor, uma
#           quarta estima δ4 para o incremento de ∆yn : δ4 = ∆xn * f(xn + ∆xn, yn + δ3)
#       5. Calcula-se a média ponderada das diversas estimas δi estabelecendo os pesos de modo a garantir um erro
#           proporcional a (∆xn)^4 : ∆yn = δ1/6 + δ2/3 + δ3/3 + δ4/6
#       6. E usa-se essa média para calcular o valor do calcular o ponto seguinte (xn+1, yn+1) :
#           xn+1 = xn + ∆xn | yn+1 = yn + ∆yn
# e repetir esses passos até cobrir por completo o intervalo que nos interessa

# A validade do valor de h escolhido em cada passo, deve utilizar-se a técnica do quociente de convergência, usando três
# cálculos de y para h, h/2, h/4 e verificando se a razão das diferenças sucessivas é aproximadamente igual a 2
# levantado à ordem do método (2^4 = 16), e, quando ele for cumprido, poderemos estimar o erro absoluto:
# erro = (S'' - S') / 15 (15 = 2^ordem - 1).


def delta1(x, y, h, function):
    return h * function(x, y)


def delta2(x, y, h, function):
    return h * function(x + h/2, y + delta1(x, y, h, function) / 2)


def delta3(x, y, h, function):
    return h * function(x + h/2, y + delta2(x, y, h, function) / 2)


def delta4(x, y, h, function):
    return h * function(x + h, y + delta3(x, y, h, function))


def delta(x, y, h, function):
    return delta1(x, y, h, function)/6 + delta2(x, y, h, function)/3 + delta3(x, y, h, function)/3 + delta4(x, y, h, function)/6


def rk4(x, xf, y, function, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        # print(x, y, _it)
        y += delta(x, y, h, function)
        x += h
        # _it += 1
    # print(x, y, _it)
    return y


# Quociente de convergência e erro

# Se não tivermos os valores certos de x0 e xf, e tivermos de ir pelas iterações não esquecer de
# colocar it*2 em s_ e colocar it * 4 em s__


def qc_value_euler_rk(method, h0, x0, xf, y, function, it, order, error):
    s = method(x0, xf, y, function, h0, error, it)
    s_ = method(x0, xf, y, function, h0 / 2, error, it)
    s__ = method(x0, xf, y, function, h0 / 4, error, it)
    qc = (s_ - s) / (s__ - s_)
    print(s, h0)
    print(s_, h0/2)
    print(s__, h0/4)
    print(qc)
    while int(qc + 0.5) != 2**order:
        h0 /= 2
        s = method(x0, xf, y, function, h0, error, it)
        s_ = method(x0, xf, y, function, h0 / 2, error, it)
        s__ = method(x0, xf, y, function, h0 / 4, error, it)
        qc = (s_ - s) / (s__ - s_)

    error = (s__ - s_) / (2**order - 1)
    print("qc = {} | erro absoluto estimado = {} | h = {}" .format(qc, error, h0))
    print("erro relativo estimado = {}" .format(error / s__))


# Método de euler -> equações de ordem superior


def euler_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        # print(x, y, z, _it)
        y_old = y
        y += functions[0](x, y, z) * h
        z += functions[1](x, y_old, z) * h
        x += h
        # _it += 1
    # print(x, y, z, _it)
    return y, z


# Rk2 -> equações de ordem superior


def rk2_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        # print(x0, y0, _it)
        y_old = y
        y += h * functions[0](x + h / 2, y_old + (h / 2) * functions[0](x, y_old, z), z + (h / 2) * functions[1](x, y_old, z))
        z += h * functions[1](x + h / 2, y_old + (h / 2) * functions[0](x, y_old, z), z + (h / 2) * functions[1](x, y_old, z))
        x += h
        # _it += 1
    return y, z


# Rk4 -> equações de ordem superior


def delta1_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x, y, z)
    return h * function[1](x, y, z)


def delta2_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h/2, y + delta1_system(x, y, z, h, function, char) / 2, z + delta1_system(x, y, z, h, function, 'z') / 2)
    return h * function[1](x + h/2, y + delta1_system(x, y, z, h, function, 'y') / 2, z + delta1_system(x, y, z, h, function, char) / 2)


def delta3_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h/2, y + delta2_system(x, y, z, h, function, char) / 2, z + delta2_system(x, y, z, h, function, 'z') / 2)
    return h * function[1](x + h/2, y + delta2_system(x, y, z, h, function, 'y') / 2, z + delta2_system(x, y, z, h, function, char) / 2)


def delta4_system(x, y, z, h, function, char):
    if char == 'y':
        return h * function[0](x + h, y + delta3_system(x, y, z, h, function, char), z + delta3_system(x, y, z, h, function, 'z'))
    return h * function[1](x + h, y + delta3_system(x, y, z, h, function, 'y'), z + delta3_system(x, y, z, h, function, char))


def delta_system(x, y, z, h, function, char):
    return delta1_system(x, y, z, h, function, char)/6 + delta2_system(x, y, z, h, function, char)/3 + delta3_system(x, y, z, h, function, char)/3 + delta4_system(x, y, z, h, function, char)/6


def rk4_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        # print(x, y, z, _it)
        y_old = y
        y += delta_system(x, y_old, z, h, functions, 'y')
        z += delta_system(x, y_old, z, h, functions, 'z')
        x += h
        # _it += 1
    # print(x, y, z, _it)
    return y, z


# Quociente de convergência e erro

# Se não tivermos os valores certos de x0 e xf, e tivermos de ir pelas iterações não esquecer de
# colocar it*2 em y_, z_ e colocar it * 4 em y__, z__


def qc_value_euler_rk_system(method, h0, x0, xf, y, z, functions, it, order, error):
    _y, _z = method(x0, xf, y, z, functions, h0, error, it)
    y_, z_ = method(x0, xf, y, z, functions, h0 / 2, error, it)
    y__, z__ = method(x0, xf, y, z, functions, h0 / 4, error, it)
    qcy = (y_ - _y) / (y__ - y_)
    qcz = (z_ - _z) / (z__ - z_)

    print(_y, h0)
    print(y_, h0/2)
    print(y__, h0/4)
    print(qcy)

    print(_z, h0)
    print(z_, h0/2)
    print(z__, h0/4)
    print(qcz)
    while int(qcy + 0.5) != 2**order or int(qcz + 0.5) != 2**order:
        h0 /= 2
        _y, _z = method(x0, xf, y, z, functions, h0, error, it)
        y_, z_ = method(x0, xf, y, z, functions, h0 / 2, error, it)
        y__, z__ = method(x0, xf, y, z, functions, h0 / 4, error, it)
        qcy = (y_ - _y) / (y__ - y_)
        qcz = (z_ - _z) / (z__ - z_)

    error_y = (y__ - y_) / (2**order - 1)
    error_z = (z__ - z_) / (2 ** order - 1)
    print("qcy = {} | erro absoluto estimado y = {} | h = {}" .format(qcy, error_y, h0))
    print("qcz = {} | erro absoluto estimado z = {} | h = {}" .format(qcz, error_z, h0))
    print("erro relativo estimado y = {}" .format(error / y__))
    print("erro relativo estimado z = {}".format(error / z__))


# Optimizações

# Pesquisa unidimensional

# O mais elementar problema de optimização consiste na pesquisa do extremo de uma função de uma só variável.
# Os critérios analíticos são bem conhecidos, mas são numerosos os casos em que, por falta de uma definição analítica
# conveniente da função objectivo, ou de algum ou alguns dos seus componentes, há que recorrer a métodos numéricos.

# Uma ideia viável consiste em procurar, a partir de um ponto de partida dado, o sentido em que a função decresce. Em
# seguida dar-se-á um passo nesse sentido, e assim sucessivamente, até que se detecte um aumento na função, isto é, que
# o novo valor calculado seja mais alto que o anterior. Quando tal se verificar, abandonam-se os dois últimos pontos
# calculados e parte-se de novo do antepenúltimo, mas agora com um passo menor, por exemplo, metade do anterior. O
# processo prossegue até o mínimo ter sido localizado dentro da precisão pré-especificada.

# A grande vantagem deste método de pesquisa é permitir que a partir de um guess se obtenha um intervalo enquadrante do
# mínimo, que facilita a aplicação dos métodos expostos em seguida.

# Um intervalo aberto em ambos os extremos que contém um mínimo, tem no seu interior um ponto de ordenada inferior à dos
# extremos. Chamemos a esses três pontos a,b, c. O raciocínio reciproco, o conhecimento de três pontos de uma função em
# que o ponto interior tem ordenada inferior garante-nos a existência de pelo menos um mínimo no intervalo. Se
# adicionalmente a função for convexa nesse intervalo, então o mínimo é único.

# Regra Áurea

# O método da secção áurea utiliza esta condição. Com efeito, começando com o intervalo [x1, x2] em que se sabe estar o
# mínimo, escolhemos:
#       x3 -> de modo a ser x3 = x1 + A*(x2 − x1)
#       x4 -> de modo a ser x4 = x1 + B*(x2 - x1)
# Assim:
#   • se for f(x3) < f(x4) o mínimo está em [x1, x4] e o próximo passo implica x2 ← x4;
#   • se for f(x3) > f(x4) o mínimo está em x3, x2 e o próximo passo implica x1 ← x3;
# com B = (sqrt(5) - 1) / 2 e A = B^2


def aurea(x1, x2, function, error, it):
    _it = 0
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    while abs(x1 - x2) > error and _it != it:
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        # print(x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4), _it)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
        # _it += 1
    # print(x1, x2, _it)
    # print("Amplitude = {}".format(abs(x1 - x2)))
    return x1, x2


# Pesquisa multidimensional

# Método do Gradiente

# Ao contrário dos métodos analíticos, que tentam ir directamente ao valor desejado, os métodos numéricos, iterativos,
# baseiam-se no princípio de dar sucessivos passos descendentes até encontrar o ponto mais baixo possível.

# Sabendo que se seguirmos a direcção do gradiente local em sentido inverso seremos, então, conduzidos ao mínimo local,
# e dado que todos os caminhos de maior pendor levam ao mesmo ponto, nem sequer precisamos de ser muito exactos:
# acabaremos sempre por lá chegar, pelo menos aproximadamente.

# Uma propriedade fundamental do método do gradiente (e que deve ser comum a todos os bons métodos de optimização) é,
# portanto, a de ser autocorrector: mesmo que se cometa um erro no cálculo de um passo (e mesmo que esse erro implique a
# passagem para um ponto em que a função tem um valor mais alto que no anterior), os passos seguintes, desde que isentos
# de erro, corrigi-lo-ão, embora eventualmente à custa de atraso da convergência.

# O método do gradiente tem o ponto fraco de, nas vizinhanças do mínimo, df/dx ser muito pequeno e, devido aos erros de
# cálculo, apontar só vagamente para o mínimo.

# A técnica mais primária de aplicação da ideia do método do gradiente consiste em dar passos (usando o expoente(i) para
# indicar a sua ordem): xj^(i+1) = xj^(i) - h * f'/ dxj, (j = 1, 2, 3,..., n) em que h é o passo.

# O primeiro problema é, naturalmente, o de arbitrar um valor razoável para h, tendo em mente que não há necessidade de
# ser muito exacto, visto que todos os caminhos vão dar ao mínimo. Um modo simples de o resolver consiste em começar com
# um passo qualquer (por exemplo, com h = 1) e:
#   1. se f(x^(i+1)) < f(x^(i)), efectivar o passo e usar para o passo seguinte h = 2 * h;
#   2. se f(x^(i+1)) > f(x(i)), não efectivar o passo e fazer nova tentativa com h = h / 2;

# DESVANTAGENS:
#  É frequente apontar-se a esta técnica o inconveniente de, quando a variação de xj for demasiado pequena, a variação
# resultante da função ser pequena, o que pode conduzir a erro na estima da derivada por efeito dos erros de
# arredondamento (note-se que, neste caso, a subtracção é inevitável) e de, quando a variação for demasiado grande, se
# não estar a medir o gradiente local mas uma espécie de gradiente regional.


def gradient(x, y, h, gradient_xy, function, error, it):
    _it = 0
    x_old = x + error * 10
    y_old = y + error * 10
    while (abs(x - x_old) > error or abs(y - y_old) > error) and _it != it:
        # print(x, y, function(x, y), _it)
        x_old = x
        y_old = y
        x -= h * gradient_xy[0](x_old, y_old)
        y -= h * gradient_xy[1](x_old, y_old)
        if function(x, y) < function(x_old, y_old):
            h *= 2
        else:
            h /= 2
            x = x_old
            y = y_old
            x_old += error * 10
            y_old += error * 10
        # _it += 1
    # print(x, y, function(x, y), _it)
    return x, y


# Método da quádrica

# O método da quádrica não tem especial interesse como método independente, dado só ser aplicável nas vizinhanças
# imediatas do mínimo; adquire, no entanto, o seu pleno significado quando combinado com outros métodos menos eficientes
# nesta vizinhança, como o do gradiente.

# Este método estabelece-se em termos formais de modo muito simples:
#   seja f(x) a função a minimizar, seja ∇f(x) o seu gradiente e H(x) a sua matriz Hesseana.

# Então a função: g(x) = f(xn) + (x−xn).∇f(xn) + (x−xn)^(2) * H(xn), constituirá uma boa aproximação a f(x) se xn for
# já próximo do mínimo x.
# Note-se de passagem que esta solução do método da quádrica corresponde à solução pelo método de Newton da aequação:
#   ∇f(x) = 0. E neste ponto teremos: ∇g(x) = ∇f(xn) + (x−xn)*H(xn) = 0, pelo que:
#           h = x−xn = −H^(−1)(xn) * ∇f(xn)


def quadratic(x, y, gradient_xy, hessian, error, it):
    x_old = x + 10 * error
    y_old = y + 10 * error
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        det = hessian[0][0](x_old, y_old) * hessian[1][1](x_old, y_old) - hessian[1][0](x_old, y_old) * hessian[0][1](x_old, y_old)
        x -= (hessian[1][1](x_old, y_old) * gradient_xy[0](x_old, y_old) - hessian[0][1](x_old, y_old) * gradient_xy[1](x_old, y_old)) / det
        y -= (hessian[0][0](x_old, y_old) * gradient_xy[1](x_old, y_old) - hessian[0][1](x_old, y_old) * gradient_xy[0](x_old, y_old)) / det
        # _it += 1
    return x, y


# Método de Levenberg-Marquardt || Misturado com a respota à pergunta do gráfico

# 	Para a resolução deste exercício, opatria pela utilização do método Levenberg-Marquardt.
# 	Este método consiste numa combinação dos métodos do gradiente e da quadrática no mesmo passo, fazendo:
# 	      	h = hquad + λ.hgrad
# em que hquad e hgrad são, respectivamente, os vectores de passo dos métodos do gradiente e da quádrica e λ é um
# parâmetro a determinar pela própria evolução do processo, segundo a seguinte lógica:
# 	      • começa-se com um valor elevado de λ (em relação à norma de hquad) , isto é, começa-se virtualmente segundo o
#   	    gradiente e continua-se decrementando o valor de λ enquanto os novos pontos calculados conduzirem a valores
#           decrescentes da função objectivo; assim, o método aproxima-se progressivamente do da quádrica quando é bem
# 		    sucedido;
# 	      • porém, cada vez que o novo ponto seja mal sucedido (isto é, corresponda a um incremento da
# 		    função objectivo), o ponto é ignorado, o valor de λ é incrementado e faz-se nova tentativa.
#
# 	Deste modo, no decorrer de uma pesquisa típica, o valor de λ oscila várias vezes ao sabor das irregularidades da
# superfície até que, chegado às vizinhanças do mínimo, tende a decrescer indefinidamente; esta circunstância permite
# determinar o ponto de paragem do algoritmo.
#
# 		Concebido inicialmente para resolver problemas de mínimos quadrados onde resulta particularmente
# económico pela facilidade, característica deste tipo particular de problema, no cálculo das derivadas e da
# quádrica osculadora, o método pode, ser estendido a casos mais gerais, embora à custa de
# trabalho de cálculo maior que no caso particularmente fácil dos mínimos quadrados.
#
# 	Curiosamente, o método torna-se especialmente vantajoso nas situações difíceis como as de existência de depressões
# alongadas, porque aí a quádrica detecta muito facilmente o alongamento. Deste modo, o algoritmo, por ingénuo que
# pareça, é um dos mais rápidos e eficazes que se conhecem.
#
# 	Porém, são frequentes os casos em que condições físicas ou matemáticas nos forçam a reduzir a busca a valores
# das variáveis que satisfazem determinadas condições. Como podemos ver, este gráfico possui duas concavidades, o que
# traz algumas dificuldades à utilização deste método, pois como método míope, isto é, puramente local, corre sempre o
# risco de se encaminhar para um mínimo local e dele não poder sair, que é ainda agravada pelo facto evidente de não
# haver critério local capaz de distinguir um mínimo local de um global.


def levenberg(x, y, h, g, lam, f, error):
    x_old = x + 10 * error
    y_old = y + 10 * error
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        det = h[0][0](x_old, y_old)*h[1][1](x_old, y_old) - h[1][0](x_old, y_old)*h[0][1](x_old, y_old)
        quad1 = (h[1][1](x_old, y_old)*g[0](x_old, y_old) - h[0][1](x_old, y_old)*g[1](x_old, y_old)) / det
        quad2 = (h[0][0](x_old, y_old)*g[1](x_old, y_old) - h[0][1](x_old, y_old)*g[0](x_old, y_old)) / det
        x -= (quad1 + lam*g[0](x_old, y_old))
        y -= (quad2 + lam*g[1](x_old, y_old))
        if f(x, y) < f(x_old, y_old):
            lam /= 2
        else:
            lam *= 2
    return x, y


# Pergunta gráfico convexo

# O método numérico mais vantajoso a utilizar seria o método Lavenberg-Marquerdt, pois este método é uma mistura dos métodos do gradiente
# e da quadrática.
# Deste modo, este método, torna-se vantajoso para em situações difíceis como em gráficos como este, de depresões alongadas, pois,
# o método da quadrática deteta facilmente o alongamento. Deste modo, o algoritmo escolhido é aquele que é mais rápido e mais eficaz que se
# conhece.
# Concebido inicialmente para resolver problemas de mínimos quadrados onde resulta particularmente
# económico pela facilidade, característica deste tipo particular de problema, no cálculo das derivadas e da
# quádrica osculadora, o método pode, ser estendido a casos mais gerais, embora à custa de
# trabalho de cálculo maior que no caso particularmente fácil dos mínimos quadrados.
# Assim, através deste método:
#   • começa-se com um valor elevado de λ (em relação à norma de hquad) , isto é, começa-se virtualmente segundo o gradiente e continua-se
#       decrementando o valor de λ enquanto os novos pontos
#       calculados conduzirem a valores decrescentes da função objectivo; assim, o método aproxima-se
#       progressivamente do da quádrica quando é bem sucedido;
#   • porém, cada vez que o novo ponto seja mal sucedido (isto é, corresponda a um incremento da
#       função objectivo), o ponto é ignorado, o valor de λ é incrementado e faz-se nova tentativa.
# Deste modo, no decorrer de uma pesquisa típica, o valor de λ oscila várias vezes ao sabor das irregularidades da superfície
# até que, chegado às vizinhanças do mínimo, tende a decrescer indefinidamente; esta circunstância permite determinar o ponto de paragem
# do algoritmo.

# Posto isto, um dos problemas deste método é que, frequentemente, existem casos onde as condições físicas ou matemáticas nos forçam
# a reduzir a busca a valores das variáveis que satisfazem determinadas condições.
# Pela análise do gráfico podemos concluir que esta função, não se trata de uma função convexa. Deste modo, como método de Lavenberg-Marquerdt
# não se econtra capaz de distinguir mínimos locais, de mínimos absolutos, a utilização deste método neste problema pode levar a que a função encontre
# este mínimo local e fique lá "presa", não possuindo a capacidade de ultrapassar o mínimo local e prosseguir em direção ao mínimo absoluto.

# O problema central específico da optimização não convexa pode, portanto, definido como o de encontrar
# um método de geração de alternativas que permita o atingimento do óptimo absoluto, sem encalhe em
# óptimos locais. Como se sabe, o único método actualmente disponível consiste em uma combinação de
# uma técnica de Monte Carlo do tipo aceitação-rejeição(para geração de sucessivos pontos de partida, ou
# guesses iniciais, dentro do praticável) combinado com uma técnica do tipo anterior(para melhoramento
# do guess inicial).


# Resíduo da equação ao fim de uma iteração é a diferença entre o valor da iteração atual e da iteração anterior


# Pergunta dos inteiros e floats
# Quanto à primeira hipótese, como estamos perante uma sucessão de números inteiros, temos
#a vantagem de não termos de lidar com erros de arredondamentos, pois os números não possuem casas decimais.
# Por outro lado, e por serem inteiros, iriamos precisar de uma ordem de grandeza bastante elevada a nível do passo
# de integração para podermos obter um resultado com bastante precisão.
#	Neste caso, e por serem floats, já não iriamos precisar de uma elevada ordem de grandeza a nível do passo de inte-
# gração para obtermos um resultado com alguma precisão. Por outro lado, e ao contrário do exemplo anterior, já iriamos ter
# problemas com os erros de arredondamentos pois os valores já possuem casas decimais.
# 	Tal como no exemplo anterior, neste caso não teriamos o problema da ordem de grandeza do passo de integração, pois
# como estamos a trabalhar com floats conseguimos obter um resultado com bastante precisão com uma ordem de grandeza menor.
# Porém, iremos ter de lidar com erros de arredondamentos, pois tal como no exemplo anterior, estamos a lidar com valores com casas
# decimais e o facto de a cada iteração multiplicarmos o valo por um número inteiro só intensifica os erros de iteração para iteração.
#	O último caso, é o melhor caso pois permite-nos ter um passo com uma pequena ordem de grandeza e preciso, e por outro lado, sem erros
# de arredondamentos associados pois o passo é sempre representável na linguagem da máquina.


# Possibilidade de duas equações

# Começando por iniciar a equação que queremos resolver, temos as seguintes possibilidades:
# 	. m é par:
# 		. R é positivo -> equação com duas soluções possíveis (um positiva e outra negativa)
# 		. R é nulo -> equação com apenas uma solução (x = 0)
# 		. R é negativo -> equação com 0 soluções (impossível)
# 	. m é ímpar:
# 		. R é positivo -> solução com apenas uma solução (positiva)
# 		. R é nulo -> solução com apenas uma solução (x = 0)
# 		. R é negativo -> solução com apenas uma solução (negativa)
#
# Assim, como no método de Newton (método não intervalar) teremos de escolher um guess inicial para começar a
# iterar sobre o mesmo até chegar ao resultado, temos que se este não for bem escolhido o método pode divergir.
# E dada esta equação temos:
# 	. Se m é par/ímpar e R é nulo -> se o valor do guess inicial for mal escolhido o sistema pode divergir
# por completo
# 	. Se m é ímpar e R é positivo/negativo -> se o valor do guess inicial for mal escolhido (demasiado distante
# da raiz do sistema), este pode divergir por completo.
# 	. Se m é par e R é positivo -> Se o valor do guess inicial for mal escolhido o sistema pode divergir para a
# outra raiz (que não é a procurada) ou se for muito distante das duas, pode diverdir por completo.
# Assim, como temos de ter cuidado com a nossa equação e o guess inicial escolhido, a fórmula recorrente escolhida deve ser aquela
# que é mais compacta e com menos probabilidades de divergir, e, deste modo, a melhor opção seria a fórmula a), pois é um polinómio
# (contínua, enquanto que a fórmula b) não é contínua em todos os pontos) e mais compacta que a opção b).

# Não esquecer:
# Erro absoluto bisecção: abs(raiz que deu - ultimo a)
# Erro relativo-bisecção: erro_abs / abs(ultimo a)
#
#
# Erro relativo estimado = (S''-S')/(2^ordem - 1 * S'')



