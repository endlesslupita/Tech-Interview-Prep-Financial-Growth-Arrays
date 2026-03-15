def square_growth(growthPercentages):
    for percentage in growthPercentages:
        squared_percentage = percentage ** 2
        squared_growth.append(squared_percentage)

    return squared_growth.sort()

if __name__ == '__main__':
    growthPercentages = [-3,-1,4,7]
    print(square_growth(growthPercentages))