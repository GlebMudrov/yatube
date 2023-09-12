from django.core.paginator import Paginator

from .constants import AMOUNT_OF_PUBLICATIONS


def paginator_posts(post_list, request):
    paginator = Paginator(post_list, AMOUNT_OF_PUBLICATIONS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
