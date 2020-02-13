from test_framework import generic_test

# 16.4 Compute the binomial coefficients
# k from n is the same with k from n-1 (the last nth missing)...
# ...plus k-1 from n-1 (in this part the last nth replaces the last kth)
def compute_binomial_coefficient(n, k):
    def compute_x_choose_y(x, y):
        if y in (0, x):
            x_choose_y[x][y] = 1
            return 1

        if x_choose_y[x][y] == -1:
            without_last_x = compute_x_choose_y(x-1, y)
            with_last_x = compute_x_choose_y(x-1, y-1)
            x_choose_y[x][y] = without_last_x + with_last_x
        return x_choose_y[x][y]

    x_choose_y = [[-1] * (k + 1) for _ in range(n + 1)]
    return compute_x_choose_y(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
