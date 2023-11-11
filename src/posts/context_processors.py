from .models import Post


def seo(request):
    last_word=None
    asd=request.build_absolute_uri()
    if asd[-1] == "/" and asd.split('/')[-3]=='post':
        last_word = asd.split('/')[-2]
        if Post.objects.filter(id=last_word):
            article = Post.objects.filter(id=last_word)
            if article is not None:
                return {
                    'seo': article,
                } 
    else:
        return {
                'seo':None,
            }
        

    
     
    


    
