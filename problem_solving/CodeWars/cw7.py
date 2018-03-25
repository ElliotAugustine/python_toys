# max_e 이상으로 중복되는 애들 제거
def delete_nth(order,max_e):
    new_order=[]
    for i in order:
        if new_order.count(i)<max_e:
            new_order.append(i)
    return new_order


def delete_nth2(order,max_e):
    return [x for i,x in enumerate(order) if order[:i].count(x) < max_e]