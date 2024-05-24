from django.shortcuts import render


def streamlit_view(request):
    return render(request, 'streamlit.html')



# from django.shortcuts import render

# def index(request):
#     search_results = []

#     if request.method == 'POST':
#         search_query = request.POST.get('search_query', '')
#         if search_query:
#             # Perform search logic here and populate search_results based on the search query
#             # For demonstration purposes, let's just pass the search query back to the template
#             search_results = [{'name': search_query, 'price': 'Sample Price'}]

#     # Render the 'front/index.html' template with the search_results
#     return render(request, 'front/index.html', {'search_results': search_results})


# from django.shortcuts import render

# def index(request):
#     if request.method == 'POST':
#         search_query = request.POST.get('search_query', '')
#         print(search_query)  # For demonstration, you can print the value to the console

#     return render(request, 'stock/index.html')


# views.py
# from django.shortcuts import render
# from bs4 import BeautifulSoup
# import requests
# from . import views
# from django.shortcuts import render

# def stock(request):
#     # Your view logic here
#     return render(request, 'index.html')

# def stock(request):
#     search_results = []

#     if request.method == 'POST':
#         search_query = request.POST.get('search_query', '')
#         if search_query:
#             amazon_url = f'https://www.amazon.in/s?k={search_query}=buydekhke-21&ref=nb_sb_noss_2'
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#             response = requests.get(amazon_url, headers=headers)
#             soup = BeautifulSoup(response.text, 'html.parser')

#             products = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vfqvn2hakys5029j0ai82q2x60 s-latency-cf-section puis-card-border')
#             for product in products:
#                 name = product.find('span', class_='a-size-medium a-color-base a-text-normal')
#                 price = product.find('span', class_='a-price-whole')
#                 if name and price:
#                     search_results.append({'name': name.text, 'price': price.text})

#     return render(request, 'index.html', {'search_results': search_results})
