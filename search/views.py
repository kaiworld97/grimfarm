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
        # print('page_number:',page_number)
        paginator = Paginator(post_list, 12)
        # print('paginator:',paginator)
        page_obj = paginator.get_page(page_number)
        # print('page_obj:',page_obj)

        if page_number:
            if int(page_number) <= paginator.num_pages:
                obj_list = paginator.get_page(page_number)
                print('obj_list:',obj_list)
                # print(obj_list.object_list)
                # a = obj_list.object_list
                aa = []
                for list in obj_list:
                    b = {}
                    b['owner'] = list.owner.nickname
                    b['title'] = list.title
                    b['img'] = list.img
                    b['buy_price'] = list.buy_price
                    b['pk'] = list.pk
                    b['proimg'] = list.owner.img
                    b['owner_pk'] = list.owner.id
                    aa.append(b)

                return JsonResponse(aa, status=200, safe=False)
        if len(post_list) == 0:

            return render(request, 'search/search.html', {'error': search, 'search': search, 'all': len(post_list)})

        ctx = {'page_obj': page_obj, 'all': len(post_list), 'search': search}
        return render(request, 'search/search.html', ctx)

    elif search == "":
        post_list = DrawingModel.objects.all()
        # 페이지 나누기
        page_number = request.GET.get('page')
        paginator = Paginator(post_list, 12)
        page_obj = paginator.get_page(page_number)

        if page_number:
            if int(page_number) <= paginator.num_pages:
                obj_list = paginator.get_page(page_number)
                # print(obj_list)

                # print(obj_list.object_list)
                # a = obj_list.object_list
                aa = []
                for list in obj_list:
                    b = {}
                    b['owner'] = list.owner.nickname
                    b['title'] = list.title
                    b['img'] = list.img
                    b['buy_price'] = list.buy_price
                    b['pk'] = list.pk
                    b['proimg'] = list.owner.img
                    b['owner_pk'] = list.owner.id
                    aa.append(b)

                return JsonResponse(aa, status=200, safe=False)
        if len(post_list) == 0:
            return render(request, 'search/search.html', {'error': search, 'search': search, 'all': len(post_list)})

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
