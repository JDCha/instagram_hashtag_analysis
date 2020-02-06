import instaloader


L = instaloader.Instaloader(download_pictures=False,
                            download_video_thumbnails=False,
                            download_videos=False,
                            download_geotags=True,
                            download_comments=False,
                            save_metadata=False)

def get_it(nameOfExercise):
    # Get instance
    numbers_of_loop = 1000
    while numbers_of_loop > 0:
        for post in L.get_hashtag_posts(nameOfExercise):
            # post is an instance of instaloader.Post
            L.download_post(post, target='#'+nameOfExercise)
            numbers_of_loop-=1
            # print(numbers_of_loop)
            if numbers_of_loop ==0:
                break
        print("loop ended for " + nameOfExercise)

kinds_of_exercise = \
["자이로토닉","필라테스","요가","빈야사","발레","키네시스","기구필라테스","매트필라테스","소도구필라테스", "플라잉필라테스","헬스","핫요가","플라잉","플라잉요가",
"하타요가","아쉬탕가","인요가","요가쿠아","번지요가","에이리얼후프","발레핏","수영","등산","조깅","크로스핏","사이클","스피닝",
"타바타","복싱","파운드핏","드럼스틱","주짓수","번지피트니스","폴댄스","방송댄스","에어로빅","뮤직복싱","번지댄스","줌바","힙레",
"재즈댄스","살사","바차타","라틴댄스","탱고","펜싱","검도","암벽등반","필록싱","다빈치바디보드","점핑피트니스","트램폴린","볼링",
"수상스키","서핑","패들보드","아쿠아바이크","패들핏","아쿠아로빅","아쿠아테크","PT"]

print(len(kinds_of_exercise))

for item in kinds_of_exercise:
    get_it(item)
