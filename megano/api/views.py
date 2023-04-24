from django.shortcuts import render
from django.http import JsonResponse
from random import randrange
import json

def banners(request):
	data = [
		{
			"id": "123",
			"category": 55,
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"freeDelivery": True,
			"images": [
				"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg"
			],
			"tags": [
				"string"
			],
			"reviews": 5,
			"rating": 4.6
		},
	]
	return JsonResponse(data, safe=False)

def categories(request):
	data = [
		{
      "id": 56,
      "title": "video card",
      "image": {
        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
        "alt": "string"
      },
      "subcategories": [
        {
          "id": 57,
          "title": "video card",
          "image": {
            "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
            "alt": "string"
          },
        }
      ]
    }
	]
	return JsonResponse(data, safe=False)


def catalog(request):
	data = {
		 "items": [
				 {
					 "id": "123",
					 "category": 123,
					 "price": 500.67,
					 "count": 12,
					 "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
					 "title": "video card",
					 "description": "description of the product",
					 "freeDelivery": True,
					 "images": [
						 "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg"
					 ],
					 "tags": [
						 "string"
					 ],
					 "reviews": 5,
					 "rating": 4.6
				 }
		 ],
		 "currentPage": randrange(1, 4),
		 "lastPage": 3
	 }
	return JsonResponse(data)

def productsPopular(request):
	data = [
		{
			"id": "123",
			"category": 55,
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"freeDelivery": True,
			"images": [
				"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
			],
			"tags": [
				"string"
			],
			"reviews": 5,
			"rating": 4.6
		}
	]
	return JsonResponse(data, safe=False)

def productsLimited(request):
	data = [
		{
			"id": "123",
			"category": 55,
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"freeDelivery": True,
			"images": [
				"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
			],
			"tags": [
				"string"
			],
			"reviews": 5,
			"rating": 4.6
		}
	]
	return JsonResponse(data, safe=False)

def sales(request):
	data = {
		'items': [
			{
				"id": 123,
				"price": 500.67,
				"salePrice": 200.67,
				"dateFrom": "2023-05-08",
				"dateTo": "2023-05-20",
				"title": "video card",
				"images": [
					"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
				]
			}
		],
		'currentPage': randrange(1, 4),
		'lastPage': 3,
	}
	return JsonResponse(data)

def basket(request):
	if(request.method == "GET"):
		print('[GET] /api/basket/')
		data = [
			{
				"id": 123,
				"category": 55,
				"price": 500.67,
				"count": 12,
				"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
				"title": "video card",
				"description": "description of the product",
				"freeDelivery": True,
				"images": [
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
				],
				"tags": [
					"string"
				],
				"reviews": 5,
				"rating": 4.6
			},
			{
				"id": 124,
				"category": 55,
				"price": 201.675,
				"count": 5,
				"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
				"title": "video card",
				"description": "description of the product",
				"freeDelivery": True,
				"images": [
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
				],
				"tags": [
					"string"
				],
				"reviews": 5,
				"rating": 4.6
			}
		]
		return JsonResponse(data, safe=False)

	elif (request.method == "POST"):
		body = json.loads(request.body)
		id = body['id']
		count = body['count']
		print('[POST] /api/basket/   |   id: {id}, count: {count}'.format(id=id, count=count))
		data = {
			"id": id,
			"category": 55,
			"price": 500.67,
			"count": 13,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"freeDelivery": True,
			"images": [
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
			],
			"tags": [
				"string"
			],
			"reviews": 5,
			"rating": 4.6
		}
		return JsonResponse(data)

	elif (request.method == "DELETE"):
		body = json.loads(request.body)
		id = body['id']
		print('[DELETE] /api/basket/')
		data = [
			{
			"id": id,
			"category": 55,
			"price": 500.67,
			"count": 11,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"freeDelivery": True,
			"images": [
						"https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
			],
			"tags": [
				"string"
			],
			"reviews": 5,
			"rating": 4.6
			}
		]
		return JsonResponse(data, safe=False)

def orders(request):
	if (request.method == "POST"):
		data = [
			{
			"id": 123,
			"category": 55,
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"freeDelivery": True,
			"images": [
				"string"
			],
			"tags": [
				"string"
			],
				"reviews": 5,
				"rating": 4.6
			}
		]
		return JsonResponse(data, safe=False)