from statistics import mean,median

def reader(filename):
    with open(filename,"r",encoding="utf-8") as file:
        data = file.read()
        return data

def main():
    data = reader("app-data/play-store.csv").splitlines()
    ratings = []

    for row in data[1:]:
        items = row.split(",")
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
    #print(type(data))
    #print(len(data))
    
main()