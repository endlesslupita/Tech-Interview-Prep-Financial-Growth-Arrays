def square_growth_naive(growthPercentages):
    squared_growth_array = []
    squared_growth_stack = []

    while growthPercentages:
        if abs(growthPercentages[0]) > abs(growthPercentages[-1]):
            popped_percent = growthPercentages.pop(0)
            squared_percent = popped_percent ** 2
            squared_growth_stack.append(squared_percent) = 
        else:
            popped_percent = growthPercentages.pop()
            squared_percent = popped_percent ** 2
            squared_growth_stack.append(squared_percent)

    squared_growth = squared_growth_stack.reverse()

    return squared_growth

# def square_growth(growthPercentages):
#     squared_growth = []
#     for percentage in growthPercentages:
#         squared_percentage = percentage ** 2
#         squared_growth.append(squared_percentage)

#     squared_growth.sort()
#     return squared_growth

if __name__ == '__main__':
    growthPercentages = [-3, -1, 4, 7]
    print(square_growth(growthPercentages))