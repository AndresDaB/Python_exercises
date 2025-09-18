def largest_element(arr, n):
    arr.sort(reverse = True)

    res = arr[:n]
    return res
if __name__ == "__main__":
    arr = [1, 20, 50, 78, 2, 5, 100]
    k = 3
    res = largest_element(arr, n)
    print(' '.join(map(str, res)))
