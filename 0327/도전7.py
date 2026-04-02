persons = ["Kim", "Park", "Lee"]
restaurants = ["Korean", "American", "French"]
locations = ["서울", "부산", "대전"]

for person in persons:
    for restaurant in restaurants:
        for location in locations:
            print(person + "이 " + restaurant + " 식당을 " + location + "에서 방문")