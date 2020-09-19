
import numpy as np

def prob(n, p, r):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param r: so lan thanh cong ma dat duoc thi ngung
    :return: xác suất của sympol thứ n
    '''
    p = (np.math.factorial(n - 1) / (np.math.factorial(n - r) * (np.math.factorial(r - 1)))) * (p ** r) * ((1 - p) ** (n - r))
    return p


def infoMeasure(n, p, r):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param r: so lan thanh cong ma dat duoc thi ngung
    :return: lượng tin của sympol thứ n
    '''
    return -np.log2(prob(n, p, r))


def sumProb(N, p, r):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :param r: so lan thanh cong ma dat duoc thi ngung
    :return: tổng xác suất của các sympols

    Vì không gian mẫu có N sympol nên tổng xác suất của N sympol đó phải bằng 1.
    Thực nghiệm:
    - Khi N = 100 sumProb = 0.9999999999999999 ~ 1.0
    - Khi N = 1000 sumProb = 0.9999999999999999 ~ 1.0
    '''

    sumProp = 0
    for k in range(r, N + 1):
        sumProp += prob(k, p, r)

    return sumProp

def approxEntropy(N, p, r):
    '''

    :param N: tổng số sympol
    :param p:xác suất bernoulli
    :param r: so lan thanh cong ma dat duoc thi ngung
    :return: xấp xỉ entropy của nguồn thông tin

    Thực nghiệm:
    - Với N = 100, entropy = 4.150775320863947
    - Với N = 1000, entropy = 4.150775320863947
    '''

    entropy = 0
    for k in range(r, N + 1):
        entropy += prob(k, p, r) * infoMeasure(k, p, r)

    return entropy


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = prob(3, 0.5, 2)
    print(p)

    i = infoMeasure(3, 0.5, 2)
    print(i)

    sumP = sumProb(1000, 0.5, 10)
    print(sumP)

    entropy = approxEntropy(1000, 0.5, 10)
    print(entropy)

