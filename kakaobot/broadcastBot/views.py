from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def product(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons' : ['사슴', '잉어', '해마']
        })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    product_name = received_json_data['content']
    day = datetime.date.today()
    delivery = day + datetime.timedelta(days=4)
    delivery_date = delivery.strftime("%m월 %d일")

    return JsonResponse({
        'message' : {
            'text' : '문의 주신 상품은 ' + product_name + '입니다. 지금 주문하시면 배송은' + delivery_date + ' 도착 예정입니다.',
            'photo' : {
                "url" : "https://s.pstatic.net/shopping.phinf/20170811_6/b2b4135d-2eb1-4435-8823-063b13b00eb9.jpg",
                'width' : 188,
                'height' : 234
            }
        },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : ['잉어', '사슴', '해마']
        }
    })
