
def default(request):
    total_amt = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            total_amt += int(item['qty'])*float(item['price'])
        return {
            'cart_data': request.session['cart_data_obj'],
            'total_cart_items': len(request.session['cart_data_obj']),
            'total_amt': total_amt
        }
    return {
        'cart_data': '',
        'total_cart_items': '',
        'total_amt': total_amt
    }
