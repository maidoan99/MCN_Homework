
import numpy as np

def prob(n, p):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :return: xác xuất của sympol thứ n
    '''

    p = 1 / (2 ** n)
    return p


def infoMeasure(n, p):
    '''

    :param n: sympol thứ n
    :param p: xác suất bernoulli
    :return: lượng thông tin của sympol của thứ n
    '''
    return -np.log2(prob(n, p))


def sumProb(N, p):
    '''

    :param N: tổng số sympols
    :param p: xác suất bernoulli
    :return: tổng xác xuất của tất cả sympols

    Vì không gian mẫu có N sympol nên tổng xác suất của N sympol đó phải bằng 1.
    Thực nghiệm:
    - Khi N = 100 sumProb = 1.0
    - Khi N = 1000 sumProb = 1.0
    '''

    sumProp = 0
    for k in range(1, N + 1):
        sumProp += prob(k, p)

    return sumProp

def approxEntropy(N, p):
    '''

    :param N: tổng số sympols
    :param p: xác suất bernoulli
    :return: giá trị xấp xỉ entropy của nguồn thông tin

    Thực nghiệm:
    - Với N = 100, entropy = 1.9999999999999998 ~ 2
    - Với N = 1000, entropy = 1.9999999999999998 ~ 2
    '''

    sumInfo = 0
    for k in range(1, N + 1):
        sumInfo += prob(k, p) * infoMeasure(k, p)

    return sumInfo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = prob(2, 0.5)
    print(p)

    i = infoMeasure(2, 0.5)
    print(i)

    sumProp = sumProb(1000, 0.5)
    print(sumProp)

    entropy = approxEntropy(1000, 0.5)
    print(entropy)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
