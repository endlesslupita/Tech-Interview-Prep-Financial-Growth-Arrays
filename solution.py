def square_growth_naive(growthPercentages):

    squared_growth_stack = []

    while growthPercentages:
        if abs(growthPercentages[0]) > abs(growthPercentages[-1]):
            popped_percent = growthPercentages.pop(0)
            squared_percent = popped_percent ** 2
            squared_growth_stack.append(squared_percent)
        else:
            popped_percent = growthPercentages.pop()
            squared_percent = popped_percent ** 2
            squared_growth_stack.append(squared_percent)

    squared_growth_stack.reverse()
    squared_growth = squared_growth_stack

    return squared_growth
##################
def square_growth(growthPercentages):
    
    list_length = len(growthPercentages)
    squared_growth = [0] * list_length
    fill = list_length - 1
    while growthPercentages:
        if abs(growthPercentages[0]) > abs(growthPercentages[-1])
            squared_percentage = growthPercentages[0] ** 2
        else:
            squared_percentage = growthPercentage[-1] ** 2
        squared_growth[fill] = squared_percentage
        fill - 1

    return squared_growth

if __name__ == '__main__':
    growthPercentages = [-3, -1, 4, 7]
    print(square_growth_naive(growthPercentages))
    #print(square_growth(growthPercentages))