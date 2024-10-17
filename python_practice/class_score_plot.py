import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('C:\\Users\\Kstone\\mypractice\\class_score_kr.csv')
    class_en = read_data('C:\\Users\\Kstone\\mypractice\\class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points

    plt.title('Scatter plot score')
    plt.scatter(midterm_kr, final_kr, s=20, label = 'Korean', color = 'red')
    plt.scatter(midterm_en, final_en, s=30, marker='+', label = 'English', color = 'blue')
    plt.xlabel('Midterm score')
    plt.ylabel('Final score')
    plt.grid()
    plt.legend()

    # TODO) Plot total scores as a histogram

    plt.figure()
    plt.title('Histogram score')
    plt.hist(total_kr, bins=20, range=(0, 100), color='red', label='Korean')
    plt.hist(total_en, bins=20, range=(0, 100), color='slateblue', label='English', alpha = 0.5)
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')
    plt.legend()

    plt.show()