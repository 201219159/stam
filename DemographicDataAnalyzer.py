import pandas as pd

def calculate():
    # Load the data
    df = pd.read_csv('data.txt')
    
    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    
    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[higher_education]['salary'] == '>50K').mean() * 100
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = ~higher_education
    lower_education_rich = (df[lower_education]['salary'] == '>50K').mean() * 100
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
    
    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country = (country_earnings / country_counts).idxmax()
    highest_earning_country_percentage = (country_earnings / country_counts).max() * 100
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Example usage
if __name__ == "__main__":
    result = calculate()
    for key, value in result.items():
        print(f"{key}: {value}")