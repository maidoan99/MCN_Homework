
import numpy as np

def prob(n, p, N):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param N: tổng số đồng xu được tung
    :return: xác xuất của sympol thứ n
    '''

    p = (np.math.factorial(N) / (np.math.factorial(n) * (np.math.factorial(N - n)))) * (p ** n) * ((1 - p) ** (N - n))
    return p


def infoMeasure(n, p, N):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param N: tổng số đồng xu được tung
    :return: lượng tin của sympol thứ n
    '''

    return -np.log2(prob(n, p, N))


def sumProb(N, p):
    '''

    :param N: tổng số sympol
    :param p:xác suất bernoulli
    :return: tổng xác suất của tất cả các sympols

    Vì không gian mẫu có N sympol nên tổng xác suất của N sympol đó phải bằng 1.
    Thực nghiệm:
    - Khi N = 100 sumProb = 1.0000000000000002 ~ 1
    - Khi N = 1000 sumProb = 1.0
    '''

    sumProp = 0
    for k in range(1, N + 1):
        sumProp += prob(k, p, N)

    return sumProp

def approxEntropy(N, p):
    '''

    :param N: tổng số sympol
    :param p:xác suất bernoulli
    :return: xấp xỉ entropy của nguồn thông tin

    Thực nghiệm:
    - Với N = 100, entropy = 4.369011409223017
    - Với N = 1000, entropy = 6.029987607045884
    '''

    entropy = 0
    for k in range(0, N + 1):
        entropy += prob(k, p, N) * infoMeasure(k, p, N)

    return entropy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = prob(2, 0.5, 2)
    print(p)

    i = infoMeasure(2, 0.5, 3)
    print(i)

    sumP = sumProb(1000, 0.5)
    print(sumP)

    entropy = approxEntropy(1000, 0.5)
    print(entropy)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
