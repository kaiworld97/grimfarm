from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from drawing.models import DrawingModel


def search(request):
    search = request.GET.get('search', '')
    if search:
        post_list = DrawingModel.objects.filter(Q(author__username__icontains=search) |
                                                Q(title__icontains=search))

        # 페이지 나누기
        page_number = request.GET.get('page')
        paginator = Paginator(post_list, 12)
        page_obj = paginator.get_page(page_number)
        print("page_number :", page_number)
        # page_number = int(page_number)
        print(paginator.num_pages)

        if page_number:
            if int(page_number) <= paginator.num_pages:
                obj_list = paginator.get_page(page_number)

                obj_list = obj_list.object_list.values("title", "owner", "buy_price")

                print(list(obj_list))

                return JsonResponse(list(obj_list), status=200, safe=False)
        ctx = {'page_obj': page_obj, 'all': len(post_list), 'search': search}
        return render(request, 'search/search.html', ctx)

        # if post_list:
        #     return render(request, 'search/search.html',
        #                   {'search_list': search_list, 'search': search, 'all': len(search_list)})
        # else:
        #     return render(request, 'search/search.html', {'error': search, 'search': search})

        # if len(post_list) == 0:
        #     return render(request, 'search/search.html', {'error': search, 'search': search})
        # else:
        #     return render(request, 'search/search.html',
        #                   {'post_list': post_list, 'search': search, 'all': len(post_list), 'page_obj': page_obj})
