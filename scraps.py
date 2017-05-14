import json

def a():
	with open('four_square_a.txt','r') as f:
	    r = json.load(f)

	here = r['items'][0]['venue']['categories']
	all_items = r['items']
	set_of_categories = set()

	for i in all_items:
	    the_cat = i['venue']['categories'][0]['shortName']
	    set_of_categories.add(the_cat)
	    print(set_of_categories)


	print(set_of_categories)

def b():
        with open('categories_data.txt') as f:
            categories = json.load(f)

        #return categories

        set_of_food_cats = set()
        for cat in categories:
            
            #print(cat[0])
            #print(cat['name'])
            if cat['name'] == 'Food':
                #return(cat)
                for subcat in cat['categories']:
                    #print(subcat)
                    #return(subcat)
                    #print('adding:{}'.format(subcat['id']))
                    set_of_food_cats.add(subcat['id'])

        #print(set_of_food_cats)
        return(set_of_food_cats)


if __name__ == '__main__':
    t = b()
