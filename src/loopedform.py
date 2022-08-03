URL = "https://www.rappler.com/page/{}"

target_title = "#important-title > p"
target_category = ".post-card__category"

form = {}

for u in range(3):
    form[URL.format(u+1)] = {
        "title" : ".post-card__title",
        "date" : ".post-card__timeago"
    }
