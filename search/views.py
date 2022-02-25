from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

from drawing.models import DrawingModel


def search(request):
    search = request.GET.get('search', '')
    if search:
        search_list = DrawingModel.objects.filter(Q(author__username__icontains=search) |
                                                  Q(description__icontains=search))

        # 페이지 나누기
        page = request.GET.get('page')
        paginator = Paginator(search_list, 12)
        rooms = paginator.get_page(page)
        # if search_list:
        #     return render(request, 'search/search.html',
        #                   {'search_list': search_list, 'search': search, 'all': len(search_list)})
        # else:
        #     return render(request, 'search/search.html', {'error': search, 'search': search})

        if len(search_list) == 0:
            return render(request, 'search/search.html', {'error': search, 'search': search})
        else:
            return render(request, 'search/search.html',
                          {'search_list': search_list, 'search': search, 'all': len(search_list), 'page': rooms})

