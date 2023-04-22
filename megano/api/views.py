from django.shortcuts import render
from django.http import JsonResponse
from random import randrange

def banners(request):
	data = [
		{
			"id": "123",
			"category": "55",
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"href": "/catalog/123",
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
      "id": "123",
      "title": "video card",
      "image": {
        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
        "alt": "string"
      },
      "href": "/catalog/123",
      "subcategories": [
        {
          "id": "123",
          "title": "video card",
          "image": {
            "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
            "alt": "string"
          },
          "href": "/catalog/123"
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
					 "category": '123',
					 "price": 500.67,
					 "count": 12,
					 "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
					 "title": "video card",
					 "description": "description of the product",
					 "href": "/catalog/123",
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
			"category": "55",
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"href": "/catalog/123",
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
			"category": "55",
			"price": 500.67,
			"count": 12,
			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
			"title": "video card",
			"description": "description of the product",
			"href": "/catalog/123",
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
				"id": "123",
				"price": 500.67,
				"salePrice": 200.67,
				"dateFrom": "2023-05-08",
				"dateTo": "2023-05-20",
				"title": "video card",
				"href": "/catalog/123",
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
	print(request.GET)
	return JsonResponse({ 'test': '' })
