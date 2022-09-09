def merge_sort(list):

    if len(list) <= 1:      #якщо список має 1 або < значень, повертаємо значення
        return list

    left_half, right_half = split(list)     #розділяємо список на дві частини

    left = merge_sort(left_half)    #присвоюємо значення
    right = merge_sort(right_half)      #присвоюємо значення

    return merge(left, right)       #повертаємо значення


def split(list):

    mid = len(list)//2      #визначаємо середину
    left = list[:mid]       #left знаення до mid
    right = list[mid:]      #right знаення після mid

    return left, right      #повертаємо значення


def merge(left, right):

    arr = []    #створюємо новий масив
    ind_l = 0   #почакові індекси
    ind_r = 0   #почакові індекси

    while ind_l < len(left) and ind_r < len(right):     #фільтруємо та розділяємо значення
        if left[ind_l] < right[ind_r]:     #перевіряємо значення
            arr.append(left[ind_l])
            ind_l += 1
        else:
            arr.append(right[ind_r])
            ind_r += 1

    while ind_l < len(left):
        arr.append(left[ind_l])
        ind_l += 1

    while ind_l < len(right):
        arr.append(right[ind_r])
        ind_r += 1

    return arr      #повертаємо результат сортування

    print(merge_sort([8, 6, 3, 4, 1, 0, 5, 7]))
