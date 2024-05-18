#views.py
# from django.http import HttpResponse
# from django.shortcuts import render

# # Create your views here.
# def MEMBERS(request):
#     return  render(request,'Members/Members.html')



from django.shortcuts import render

def MEMBERS(request):
    members_data = [
        {'name': 'Member 1', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/alamin.jpg'},
        {'name': 'Member 2', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/hamid.jpg'},
         {'name': 'Member 3', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/jamal.jpg'},
        {'name': 'Member 4', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/kader.jpg'},
         {'name': 'Member 5', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/mahibul.jpg'},
        {'name': 'Member 6', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/mizan.jpg'},
         {'name': 'Member 7', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/nizam.jpg'},
        {'name': 'Member 8', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/rony.jpg'},
         {'name': 'Member 9', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/sayed.jpg'},
        {'name': 'Member 10', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/Shahalam.jpg'},
         {'name': 'Member 11', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/shahjahan.jpg'},
        {'name': 'Member 12', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/tamjid.jpg'},
         {'name': 'Member 13', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/tawsif.jpg'},
        {'name': 'Member 14', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/topu.jpg'},
         {'name': 'Member 15', 'address': 'Address 1', 'fb_link': 'https://www.facebook.com/member1', 'image_url': '/static/images/yousuf.jpg'},
        {'name': 'Member 16', 'address': 'Address 2', 'fb_link': 'https://www.facebook.com/member2', 'image_url': '/static/images/rafi.jpg'},
            
    ]

    return render(request, 'Members/Members.html', {'members': members_data})
