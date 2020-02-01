from statistics import mean,median

def reader(filename):
    with open(filename,"r",encoding="utf-8") as file:
        data = file.read()
        return data

def main():
    data = reader("app-data/imdb-data.tsv").splitlines()
    ratings = []

    for row in data:
        items = row.split("\t")
        try:
            value= float(items[2])
            if value <= 5:
                ratings.append(value)
        except ValueError:
            pass

    print('Max: {}').format(max(ratings))
    print('Min: {}').format(min(ratings))
    print('Mean: {}').format(mean(ratings))
    print('Mean: {}').format(median(ratings))
   # print(type(data))
    #print(len(data))
    
main()